var config = {
  mode: "fixed_servers",
  rules: {
    singleProxy: {
      scheme: "http",
      host: "91.239.130.17",
      port: 44443
    },
    bypassList: ["localhost"]
  }
};

chrome.proxy.settings.set({
  value: config,
  scope: "regular"
}, function() {});

function callbackFunc(details) {
  return {
    authCredentials: {
      username: "mr663133qug",
      password: "MWusOuhIhr_country-pl_session-qqglftpy_lifetime-50m"
    }
  };
}

chrome.webRequest.onAuthRequired.addListener(
  callbackFunc, {
    urls: ["<all_urls>"]
  },
  ['blocking']
);