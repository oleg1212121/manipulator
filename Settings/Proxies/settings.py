import random


def __proxy_list():
    return [

    ]


def __proxy_options():
    proxy = random.choice(__proxy_list())
    parts = proxy.split('@')
    proxy_username, proxy_password = parts[0].split(':')
    proxy_address, proxy_port = parts[1].split(':')

    proxy_url_http = f"http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}"
    proxy_url_https = f"https://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}"
    proxy_url_socks5 = f"socks5://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}"

    return {
        "Proxy": {
            "http": proxy_url_socks5,
            "https": proxy_url_socks5,
            "SOCKS5": proxy_url_socks5,
            "verify_ssl": False,
            "no_proxy": "localhost,127.0.0.1",
        },
    }


proxies = {
    'list': __proxy_list(),
    'options': __proxy_options()
}

