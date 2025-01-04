import wx

class LogoutView(wx.Dialog):
    """Vista para confirmar el cierre de sesión."""

    def __init__(self, controller):
        super().__init__(None, title="Cerrar Sesión", size=(300, 150))
        self.controller = controller

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(panel, label="¿Estás seguro de que deseas cerrar sesión?")
        button_box = wx.BoxSizer(wx.HORIZONTAL)

        yes_button = wx.Button(panel, label="Sí")
        no_button = wx.Button(panel, label="No")

        yes_button.Bind(wx.EVT_BUTTON, self.on_confirm)
        no_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        button_box.Add(yes_button, flag=wx.ALL, border=10)
        button_box.Add(no_button, flag=wx.ALL, border=10)

        vbox.Add(label, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        vbox.Add(button_box, flag=wx.ALIGN_CENTER)

        panel.SetSizer(vbox)

    def on_confirm(self, event):
        """Llama al controlador para confirmar cierre de sesión."""
        self.controller.handle_logout()

    def on_cancel(self, event):
        """Cierra el diálogo sin cerrar sesión."""
        self.Close()
