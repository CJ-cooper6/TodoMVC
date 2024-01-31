from flask import Blueprint

bp = Blueprint("api", __name__)

from . import todo_item, login, user_center  # 要把使用蓝图对象的视图文件，导入到创建蓝图对象的文件中，在创建蓝图对象的下面导入
