import wx
from components.SellerDashboard.RegisterSale.View.register_sale_view import RegisterSaleView

class RegisterSaleController:
    """Controlador para gestionar el registro de ventas."""

    def __init__(self):
        self.view = RegisterSaleView(self)

    def show_view(self):
        """Muestra la ventana de registro de ventas."""
        self.view.Show()

    def handle_save_sale(self, sale_data):
        """Procesa la lógica de guardado de una venta."""
        # Aquí se conectaría con el modelo para guardar los datos.
        wx.MessageBox(f"Venta registrada:\n{sale_data}", "Información", wx.OK | wx.ICON_INFORMATION)
