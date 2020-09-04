# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from walle.service.rbac.role import Permission
from flask_socketio import SocketIO
async_mode = 'threading'

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
mail = Mail()

permission = Permission()
# socketio = SocketIO(engineio_logger=True, logger=True, cors_allowed_origins=[])
socketio = SocketIO(message_queue='redis://192.168.10.106:6379/0', channel='walle', engineio_logger=False, logger=True, 
                    cors_allowed_origins=[], async_mode=async_mode)
