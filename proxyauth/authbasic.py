import os


def enable_proxy(proxy_with_port):
    proxy = proxy_with_port
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['httpS_proxy'] = proxy

