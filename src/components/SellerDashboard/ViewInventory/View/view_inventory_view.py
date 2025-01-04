import wx

class ViewInventoryView(wx.Frame):
    """Vista para mostrar el inventario."""

    def __init__(self, controller):
        super().__init__(None, title="Ver Inventario", size=(500, 400))
        self.controller = controller

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.inventory_list = wx.ListBox(panel)
        refresh_button = wx.Button(panel, label="Actualizar Inventario")
        refresh_button.Bind(wx.EVT_BUTTON, self.on_refresh)

        vbox.Add(self.inventory_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(refresh_button, flag=wx.ALL | wx.ALIGN_CENTER, border=10)

        panel.SetSizer(vbox)

    def on_refresh(self, event):
        """Llama al controlador para actualizar el inventario."""
        self.controller.handle_refresh_inventory()
