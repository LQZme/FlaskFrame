from web.controllers.Index import index_route
from web.controllers.user.User import user_route
from application import app
from web.interceptors.AuthInterceptor import *

app.register_blueprint(index_route, url_prefix='/')
app.register_blueprint(user_route, url_prefix='/user')
