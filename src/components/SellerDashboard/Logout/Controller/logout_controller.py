import wx
from components.SellerDashboard.Logout.View.logout_view import LogoutView

class LogoutController:
    """Controlador para gestionar el cierre de sesión."""

    def __init__(self):
        self.view = LogoutView(self)

    def show_view(self):
        """Muestra la ventana de confirmación de cierre de sesión."""
        self.view.ShowModal()

    def handle_logout(self):
        """Lógica para cerrar sesión."""
        wx.MessageBox("Sesión cerrada correctamente", "Información", wx.OK | wx.ICON_INFORMATION)
        self.view.Destroy()
