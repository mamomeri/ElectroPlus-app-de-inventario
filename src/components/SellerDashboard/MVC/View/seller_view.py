import wx

class SellerView(wx.Frame):
    """Vista del Dashboard del Vendedor."""

    def __init__(self, controller):
        super().__init__(None, title="Dashboard - Vendedor", size=(800, 600))
        self.controller = controller

        panel = wx.Panel(self)

        # Botones
        logout_btn = wx.Button(panel, label="Cerrar Sesión", pos=(20, 20))
        register_sale_btn = wx.Button(panel, label="Registrar Venta", pos=(20, 70))
        view_inventory_btn = wx.Button(panel, label="Ver Inventario", pos=(20, 120))

        # Bind eventos
        logout_btn.Bind(wx.EVT_BUTTON, lambda event: self.controller.handle_logout())
        register_sale_btn.Bind(wx.EVT_BUTTON, lambda event: self.controller.handle_register_sale())
        view_inventory_btn.Bind(wx.EVT_BUTTON, lambda event: self.controller.handle_view_inventory())

        self.Centre()
