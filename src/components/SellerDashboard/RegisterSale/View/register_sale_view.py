import wx

class RegisterSaleView(wx.Frame):
    """Vista para registrar una nueva venta."""

    def __init__(self, controller):
        super().__init__(None, title="Registrar Venta", size=(400, 300))
        self.controller = controller

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.sale_info = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        save_button = wx.Button(panel, label="Guardar Venta")
        save_button.Bind(wx.EVT_BUTTON, self.on_save)

        vbox.Add(self.sale_info, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(save_button, flag=wx.ALL | wx.ALIGN_CENTER, border=10)

        panel.SetSizer(vbox)

    def on_save(self, event):
        """Llama al controlador para guardar la venta."""
        sale_data = self.sale_info.GetValue()
        self.controller.handle_save_sale(sale_data)
