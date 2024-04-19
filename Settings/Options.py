import pyautogui


settings = {
    "links": [
        'https://visa.vfsglobal.com/blr/ru/pol/attend-centre/Minsk',
        'https://visa.vfsglobal.com/blr/ru/pol/book-an-appointment',
        'https://visa.vfsglobal.com/blr/ru/pol/login'
    ],
    "images_folder": "Images\\",
    "email_not_robot": "Images\\not_robot.PNG",
    "login_not_robot": "Images\\ishuman.PNG",
}

coordinates = {
    'email_input': [900, 400],
    'password_input': [900, 485],
    'login_submit': [950, 625],
    'login_checkbox': [770, 470],
    "browser": [560, 1060],
    # "resize": [1005,305],
    "mailbox": [850,640],
    "email": [400,220],
    "start_copy": [1110,485],
    "end_copy": [1166,485],
    # "close": [1895,13],
    "keyboard_region": [690, 700, 1230, 1030],
    "approval_submit": [950, 500],
    "approval_input": [950, 430],
    "appointment_button": [1270, 240],
    "refresh_button": [92, 62]
}

animation = {
    "fast_duration": 0.2,
    "pre_middle_duration": 0.6,
    "middle_duration": 1.2,
    "slow_duration": 3,
    "short_sleep": 5,
    "middle_sleep": 10,
    "long_sleep": 20,
    "XL_sleep": 30,
    'animation': pyautogui.easeOutQuad
}

symbols = {
    '1': ['1.PNG', True, None, 0.95, True],
    '2': ['2.PNG', True, None, 0.95, True],
    '3': ['3.PNG', True, None, 0.95, True],
    '4': ['4.PNG', True, None, 0.95, True],
    '5': ['5.PNG', True, None, 0.95, True],
    '6': ['6.PNG', True, None, 0.95, True],
    '7': ['7.PNG', True, None, 0.95, True],
    '8': ['8.PNG', True, None, 0.95, True],
    '9': ['9.PNG', True, None, 0.95, True],
    '0': ['0.PNG', True, None, 0.95, True],
    'L': ['L.PNG', True, 'shift', 0.9, True],
    'K': ['K.PNG', True, 'shift', 0.9, True],
    'Z': ['Z.PNG', True, 'shift', 0.9, True],
    'v': ['v.PNG', True, None, 0.9, True],
    'f': ['f.PNG', True, None, 0.93, True],
    's': ['s.PNG', True, None, 0.9, True],
    '!': ['!.PNG', True, 'shift', 0.9, True],
    'backspace': ['backspace.PNG', True, None, 0.9, True],

    # '11': ['ApprovalKeyboard\\1.PNG', True, None, 0.9, True],
    # '22': ['ApprovalKeyboard\\2.PNG', True, None, 0.9, True],
    # '33': ['ApprovalKeyboard\\3.PNG', True, None, 0.9, True],
    # '44': ['ApprovalKeyboard\\4.PNG', True, None, 0.9, True],
    # '55': ['ApprovalKeyboard\\5.PNG', True, None, 0.9, True],
    # '66': ['ApprovalKeyboard\\6.PNG', True, None, 0.9, True],
    # '77': ['ApprovalKeyboard\\7.PNG', True, None, 0.9, True],
    # '88': ['ApprovalKeyboard\\8.PNG', True, None, 0.9, True],
    # '99': ['ApprovalKeyboard\\9.PNG', True, None, 0.9, True],
    # '00': ['ApprovalKeyboard\\0.PNG', True, None, 0.9, True],
}

approval_keyboard = {
    "1": [790,870],
    "2": [960,870],
    "3": [1130,870],
    "4": [790,915],
    "5": [960,915],
    "6": [1130,915],
    "7": [850,960],
    "8": [960,960],
    "9": [1130,960],
    "0": [960, 1000],
    "backspace": [790, 1000],
}
