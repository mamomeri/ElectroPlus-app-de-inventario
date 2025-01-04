import wx
from components.Login.MVC.Controller.login_controller import LoginController

class LoginView(wx.Dialog):
    def __init__(self, parent, db_path, app_facade):
        super().__init__(parent, title="Inicio de Sesión", size=(400, 300))
        self.controller = LoginController(self, db_path, app_facade)
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz de usuario."""
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Campos de texto para usuario y contraseña
        self.username_input = wx.TextCtrl(panel)
        self.password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        sizer.Add(wx.StaticText(panel, label="Usuario:"), 0, wx.ALL, 10)
        sizer.Add(self.username_input, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(wx.StaticText(panel, label="Contraseña:"), 0, wx.ALL, 10)
        sizer.Add(self.password_input, 0, wx.EXPAND | wx.ALL, 10)

        # Botón de inicio de sesión
        login_button = wx.Button(panel, label="Iniciar Sesión")
        login_button.Bind(wx.EVT_BUTTON, self.controller.on_login)  # Evento delegado al controlador

        sizer.Add(login_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)
        self.Centre()

    def get_user_input(self):
        """Obtiene el usuario y la contraseña ingresados."""
        return self.username_input.GetValue(), self.password_input.GetValue()

    def show_error(self, message):
        """Muestra un mensaje de error."""
        wx.MessageBox(message, "Error", wx.OK | wx.ICON_ERROR)