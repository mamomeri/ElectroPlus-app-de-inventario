import wx
from components.AdminDashboard.GestionarUsuarios.MVC.Model.gestionar_usuarios_model import GestionarUsuariosModel
from components.AdminDashboard.GestionarUsuarios.MVC.View.gestionar_usuarios_view import GestionarUsuariosView


class GestionarUsuariosController:
    def __init__(self, parent):
        self.model = GestionarUsuariosModel()
        self.view = GestionarUsuariosView(parent, self)
        self.refresh_user_list()
        self.view.Show()

    def refresh_user_list(self):
        """Actualiza la tabla con los datos de los usuarios."""
        users = self.model.fetch_users()
        formatted_users = [(str(user[0]), user[1], user[2], user[3]) for user in users]  # ID, Nombre, Tipo, Contraseña
        self.view.populate_users(formatted_users)

    def handle_add_user(self, event):
        """Maneja el evento para agregar un nuevo usuario."""
        with wx.TextEntryDialog(self.view, "Ingrese los datos del nuevo usuario en el formato: nombre,tipo (empleado,administrador),contraseña",
                                "Agregar Usuario") as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                try:
                    data = dialog.GetValue().split(",")
                    if len(data) == 3:
                        nombre, tipo, contraseña = data
                        self.model.add_user(nombre, tipo, contraseña)
                        self.refresh_user_list()
                        wx.MessageBox("Usuario agregado exitosamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
                    else:
                        wx.MessageBox("Formato incorrecto. Use: nombre,tipo (empleado,administrador),contraseña", "Error", wx.OK | wx.ICON_ERROR)
                except Exception as e:
                    wx.MessageBox(f"Error al agregar usuario: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)

    def handle_edit_user(self, event):
        """Maneja la acción de editar un usuario existente."""
        selected = self.view.user_list.GetFirstSelected()  # Obtiene el índice seleccionado
        if selected == -1:
            wx.MessageBox("Seleccione un usuario para editar.", "Advertencia", wx.ICON_WARNING)
            return

        # Obtiene los datos del usuario seleccionado
        user_id = self.view.user_list.GetItem(selected, 0).GetText()
        nombre = self.view.user_list.GetItem(selected, 1).GetText()
        tipo = self.view.user_list.GetItem(selected, 2).GetText()
        contraseña = self.view.user_list.GetItem(selected, 3).GetText()

        # Diálogo para ingresar nuevos datos
        with wx.TextEntryDialog(self.view,
                                f"Edite los datos del usuario en el formato actual: nombre,tipo(empleado,administrador),contraseña\nActual: {nombre},{tipo},{contraseña}",
                                "Editar Usuario") as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                try:
                    data = dialog.GetValue().split(",")
                    if len(data) == 3:
                        new_nombre, new_tipo, new_contraseña = data
                        self.model.update_user(user_id, new_nombre, new_tipo, new_contraseña)
                        self.refresh_user_list()
                        wx.MessageBox("Usuario actualizado exitosamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
                    else:
                        wx.MessageBox("Formato incorrecto. Use: nombre,tipo,contraseña", "Error", wx.OK | wx.ICON_ERROR)
                except Exception as e:
                    wx.MessageBox(f"Error al editar usuario: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)

    def handle_delete_user(self, event):
        """Maneja la acción de eliminar un usuario existente."""
        selected = self.view.user_list.GetFirstSelected()
        if selected == -1:
            wx.MessageBox("Seleccione un usuario para eliminar.", "Advertencia", wx.ICON_WARNING)
            return

        user_id = self.view.user_list.GetItem(selected, 0).GetText()
        confirm = wx.MessageBox(f"¿Está seguro de eliminar al usuario con ID {user_id}?", "Confirmar",
                                wx.YES_NO | wx.ICON_WARNING)
        if confirm == wx.YES:
            try:
                self.model.delete_user(user_id)
                self.refresh_user_list()
                wx.MessageBox("Usuario eliminado exitosamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
            except Exception as e:
                wx.MessageBox(f"Error al eliminar usuario: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
