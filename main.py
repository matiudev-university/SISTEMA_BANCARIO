from db.init_db import db_init
from models.menu import Menu

db_init()
menu = Menu()
menu.menu_principal()