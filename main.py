from db.db import init_db
from models.menu import Menu

init_db()
menu = Menu()
menu.menu_principal()