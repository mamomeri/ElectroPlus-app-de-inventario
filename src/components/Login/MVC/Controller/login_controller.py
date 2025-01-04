from components.Login.MVC.Model.user_model import UserModel
import wx

class LoginController:
    def __init__(self, view, db_path, app_facade):
        self.view = view
        self.model = UserModel(db_path)
        self.app_facade = app_facade

    def on_login(self, event):
        """Maneja el evento de inicio de sesión."""
        username, password = self.view.get_user_input()
        user_role = self.model.validate_user(username, password)

        if user_role:
            self.app_facade.rol_user = user_role
            
            self.view.EndModal(wx.ID_OK)  # Cierra la ventana si las credenciales son correctas
        else:
            self.view.show_error("Usuario o contraseña incorrectos.")  # Muestra error