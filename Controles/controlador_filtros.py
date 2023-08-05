class ControladorFiltros:
    def __init__(self, app, modelo_filtro):
        self.app = app
        self.modelo_filtro = modelo_filtro

    def obtener_filtros(self):
        return self.modelo_filtro

    def seleccionar_filtro(self):
        """
        Obtiene el índice del filtro seleccionado y llama a la vista de
        información para mostrar la información del filtro.
        """
        indice = self.app.vista_filtros.obtener_filtro_seleccionado()
        if indice is not None:
            filtro = self.modelo_filtro[indice]
            self.app.vista_info_filtros.mostrar_info_filtro(filtro)
            self.app.cambiar_frame(self.app.vista_info_filtros)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
