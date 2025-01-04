import wx


class GestionarUsuariosView(wx.Frame):
    """Vista para la gestión de usuarios."""

    def __init__(self, parent, controller=None):
        super().__init__(parent, title="Gestionar Usuarios", size=(600, 400))
        self.controller = controller  # Guardar el controlador

        # Configuración inicial de la vista
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Etiqueta de título
        self.title = wx.StaticText(self.panel, label="Gestión de Usuarios")
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.title.SetFont(font)
        self.sizer.Add(self.title, 0, wx.ALIGN_CENTER | wx.TOP, 10)

        # Tabla para mostrar usuarios
        self.user_list = wx.ListCtrl(self.panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.user_list.InsertColumn(0, "ID", width=50)
        self.user_list.InsertColumn(1, "Nombre", width=150)
        self.user_list.InsertColumn(2, "Tipo", width=100)
        self.user_list.InsertColumn(3, "Contraseña", width=150)
        self.sizer.Add(self.user_list, 1, wx.EXPAND | wx.ALL, 10)

        # Botones de acción
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.add_button = wx.Button(self.panel, label="Agregar Usuario")
        self.edit_button = wx.Button(self.panel, label="Editar Usuario")
        self.delete_button = wx.Button(self.panel, label="Eliminar Usuario")
        button_sizer.Add(self.add_button, 0, wx.RIGHT, 5)
        button_sizer.Add(self.edit_button, 0, wx.RIGHT, 5)
        button_sizer.Add(self.delete_button, 0, wx.RIGHT, 5)
        self.sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        # Configurar el layout del panel
        self.panel.SetSizer(self.sizer)

        # Asociar eventos a los botones
        self.add_button.Bind(wx.EVT_BUTTON, self.controller.handle_add_user)
        self.edit_button.Bind(wx.EVT_BUTTON, self.controller.handle_edit_user)
        self.delete_button.Bind(wx.EVT_BUTTON, self.controller.handle_delete_user)

    def populate_users(self, users):
        """Llena la tabla con los usuarios."""
        self.user_list.DeleteAllItems()
        for user in users:
            self.user_list.Append(user)

    def get_selected_user(self):
        """Obtiene el ID del usuario seleccionado."""
        selected = self.user_list.GetFirstSelected()
        if selected != -1:
            return self.user_list.GetItemText(selected)
        return None
