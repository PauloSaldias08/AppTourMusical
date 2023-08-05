class ControladorInicioUsuarios:
    def __init__(self, app):
        self.app = app

    def mostrar_usuarios(self):
        self.app.cambiar_frame(self.app.vista_usuarios)