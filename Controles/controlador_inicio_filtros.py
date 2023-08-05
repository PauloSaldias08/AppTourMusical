class ControladorInicioFiltros:
    def __init__(self, app):
        self.app = app

    def mostrar_filtros(self):
        self.app.cambiar_frame(self.app.vista_filtros)