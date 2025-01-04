import wx
from components.AdminDashboard.MVC.Controller.admin_controller import AdminController
class AdminView(wx.Frame):
    def __init__(self, parent,app_facade):
        super().__init__(parent, title="Dashboard - Administrador", size=(800, 600))
        self.controller = AdminController(self,app_facade) 

        self.init_ui()
        
    def init_ui(self):
        """Inicializa los elementos gráficos de la ventana."""
        panel = wx.Panel(self)

        # Layout principal
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Botón "Gestionar Usuarios"
        self.manage_users_button = wx.Button(panel, label="Gestionar Usuarios", size=(200, 50))
        main_sizer.Add(self.manage_users_button, 0, wx.ALIGN_CENTER | wx.TOP, 50)

        # Botón "Cerrar Sesión"
        self.logout_button = wx.Button(panel, label="Cerrar Sesión", size=(200, 50))
        main_sizer.Add(self.logout_button, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        # Panel inferior para copyright
        bottom_panel = wx.Panel(panel, size=(-1, 50))
        bottom_panel.SetBackgroundColour("#007ACC")

        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        copyright_label = wx.StaticText(bottom_panel, label="ElectroPlus Sistema de Administración © 2024")
        copyright_label.SetForegroundColour(wx.WHITE)
        bottom_sizer.Add(copyright_label, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        bottom_panel.SetSizer(bottom_sizer)

        main_sizer.AddStretchSpacer()
        main_sizer.Add(bottom_panel, 0, wx.EXPAND | wx.BOTTOM, 0)

        # Configurar eventos
        self.manage_users_button.Bind(wx.EVT_BUTTON, self.controller.handle_manage_users)
        self.logout_button.Bind(wx.EVT_BUTTON, self.controller.handle_logout)

        panel.SetSizer(main_sizer)
        self.Centre()

    def show_message(self, message, title="Información"):
        """Muestra un cuadro de diálogo con un mensaje."""
        wx.MessageBox(message, title, wx.OK | wx.ICON_INFORMATION)
