from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from common.libs.Helper import IsActive
import os


class Application(Flask):
    def __init__(self,
                 import_name,
                 static_folder=None,
                 template_folder=None,
                 root_path=None
                 ):
        super().__init__(
            import_name=import_name,
            static_folder=static_folder,
            template_folder=template_folder,
            root_path=root_path
        )
        self.config.from_object('config.base_setting')
        self.config.from_object('config.local_setting')


app = Application(__name__,
                  static_folder=os.getcwd()+'/web/static',
                  template_folder=os.getcwd()+'/web/templates',
                  root_path=os.getcwd())

db = SQLAlchemy(app)


app.add_template_global(IsActive.isActive, 'isActive')
