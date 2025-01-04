import wx
from utils.config import DATABASE_PATH
from components.Login.MVC.View.login_view import LoginView
from components.Login.MVC.Controller.login_controller import LoginController

class AdminController:
    def __init__(self, view, app_facade):
        self.view = view  # Guardar la referencia a la vista
        self.app_facade = app_facade
    def handle_manage_users(self, event):
        """Maneja la apertura de la pantalla Gestionar Usuarios."""
        from components.AdminDashboard.GestionarUsuarios.MVC.Controller.gestionar_usuarios_controller import GestionarUsuariosController
        GestionarUsuariosController(self.view)

    def handle_logout(self, event):
        """Cerrar sesión y redirigir al login."""
        confirm = wx.MessageBox("¿Está seguro de cerrar sesión?", "Confirmar", wx.YES_NO | wx.ICON_QUESTION)
        if confirm == wx.YES:
            self.view.Close()
            self.app_facade.login_view.ShowModal()