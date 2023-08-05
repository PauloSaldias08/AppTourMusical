class ControladorUsuarios:
    def __init__(self, app, modelo_usuario):
        self.app = app
        self.modelo_usuario = modelo_usuario

    def obtener_usuarios(self):
        return self.modelo_usuario

    def seleccionar_usuario(self):
        """
        Obtiene el índice del usuario seleccionado y llama a la vista de
        información para mostrar la información del usuario.
        """
        indice = self.app.vista_usuarios.obtener_usuario_seleccionado()
        if indice is not None:
            usuario = self.modelo_usuario[indice]
            self.app.vista_info_usuarios.mostrar_info_usuario(usuario)
            self.app.cambiar_frame(self.app.vista_info_usuarios)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)