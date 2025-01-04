from components.SellerDashboard.RegisterSale.Controller.register_sale_controller import RegisterSaleController
from components.SellerDashboard.ViewInventory.Controller.view_inventory_controller import ViewInventoryController
from components.SellerDashboard.Logout.Controller.logout_controller import LogoutController
from components.SellerDashboard.MVC.View.seller_view import SellerView

class SellerController:
    """Controlador principal del Dashboard del Vendedor."""

    def __init__(self):
        self.view = SellerView(self)

    def handle_logout(self):
        controller = LogoutController()
        controller.show_view()

    def handle_register_sale(self):
        controller = RegisterSaleController()
        controller.show_view()

    def handle_view_inventory(self):
        controller = ViewInventoryController()
        controller.show_view()
