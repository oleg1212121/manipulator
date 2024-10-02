import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Manipulations.MailboxReader.EmailParser import EmailParser


class GmailReader:

    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        self.SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

    def process(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        # If there are no (valid) Credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "./MailboxReader/gmail-Credentials.json", self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the Credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            # Call the Gmail API
            service = build("gmail", "v1", credentials=creds)
            results = service.users().messages().list(
                userId="me",
                maxResults=2,
                includeSpamTrash=True,
                q='from:<donotreply@vfshelpline.com> is:unread'
            ).execute()
            messages = results.get("messages", [])

            if not messages:
                print("No messages found.")
                return []

            # get last email
            last_email = service.users().messages().get(userId='me', id=messages[0]['id']).execute()
            text = last_email['snippet']

            parser = EmailParser()
            codes = parser.search(text)

            # mark email as 'read'
            post_data = {
                "addLabelIds": [
                    "TRASH"
                ],
                "removeLabelIds": [
                    "UNREAD", "INBOX"
                ]
            }
            service.users().messages().modify(userId='me', id=messages[0]['id'], body=post_data).execute()

            return codes

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")
            return []

