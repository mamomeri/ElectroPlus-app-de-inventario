import wx
from components.SellerDashboard.ViewInventory.View.view_inventory_view import ViewInventoryView

class ViewInventoryController:
    """Controlador para gestionar la visualización de inventario."""

    def __init__(self):
        self.view = ViewInventoryView(self)

    def show_view(self):
        """Muestra la ventana de inventario."""
        self.view.Show()

    def handle_refresh_inventory(self):
        """Lógica para refrescar el inventario (mock)."""
        wx.MessageBox("Inventario actualizado", "Información", wx.OK | wx.ICON_INFORMATION)
