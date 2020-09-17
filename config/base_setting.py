import os

DEBUG = False

SERVER_PORT = 5050

SECRET_KEY = "sfsdfsdgsdgsd"

PROJECT_TITLE = "后台管理系统"

SUPPORT = "LQZme"

PAGE_SIZE = 1

PAGE_DISPLAY = 4

# 登录后需要忽视的URL
IGNORE_URLS = [
    '^/user/login'
]


# 登录前需要忽视的URL
IGNORE_CHECK_LOGIN_URLS = [
    '^/static'
]
