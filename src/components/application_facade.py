import wx
from components.Login.MVC.View.login_view import LoginView
from components.AdminDashboard.MVC.View.admin_view import AdminView
from db.Scripts.CreateDB import initialize_db
from utils.config import DATABASE_PATH

class ApplicationFacade:

    def __init__(self, db_path):
        self.db_path = db_path
        self.rol_user = None
        self.app = wx.App(False)
        # Crear la vista y el controlador del login
        self.login_view = LoginView(None, self.db_path, self)
        self.admin_view = AdminView(None,self)
    
    def run(self):
        """Ejecuta la aplicación."""
        initialize_db()
        self.login_view.Show()
        if self.login_view.ShowModal() == wx.ID_OK:
            print("Rol del usuario:", self.rol_user)
            if self.rol_user == "administrador":
                self.admin_view.Show()
        self.app.MainLoop()