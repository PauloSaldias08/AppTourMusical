import tkinter as tk
from Modelos.evento import Evento
from Modelos.usuario import Usuario
from Vistas.vista_inicio import VistaInicio
from Vistas.vista_eventos import VistaEventos
from Vistas.vista_usuarios import VistaUsuarios
from Vistas.vista_info import VistaInfo
from Vistas.vista_info_usuarios import VistaInfoUsuarios
from Vistas.vista_info_filtros import VistaInfoFiltros
from Vistas.vista_filtros import VistaFiltros
from Controles.controlador_inicio import ControladorInicio
from Controles.controlador_eventos import ControladorEventos
from Controles.controlador_usuarios import ControladorUsuarios
from Controles.controlador_info import ControladorInfo
from Controles.controlador_info_usuarios import ControladorInfoUsuarios
from Controles.controlador_filtros import ControladorFiltros
from Controles.controlador_info_filtros import ControladorInfoFiltros

from Controles.controlador_info_filtros import ControladorPrincipal

class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Primer ventana - Aplicación de Musica")
        self.geometry("600x600")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        eventos = Evento.cargar_de_json("Data/eventos.json")
        usuarios = Usuario.cargar_de_json("Data/usuarios.json")
        filtros = Evento.cargar_de_json("Data/eventos.json")

        controlador_inicio = ControladorInicio(self)
        controlador_eventos = ControladorEventos(self, eventos)
        controlador_info = ControladorInfo(self)

        controlador_inicio_usuarios = ControladorInicio(self)
        controlador_usuarios = ControladorUsuarios(self, usuarios)
        controlador_info_usuarios = ControladorInfoUsuarios(self)

        controlador_inicio_filtros = ControladorInicio(self)
        controlador_filtros = ControladorFiltros(self, filtros)
        controlador_info_filtros = ControladorInfoFiltros(self)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_eventos = VistaEventos(self, controlador_eventos)
        self.vista_info = VistaInfo(self, controlador_info)

        self.vista_inicio_usuarios = VistaInicio(self, controlador_inicio_usuarios)
        self.vista_usuarios = VistaUsuarios(self, controlador_usuarios)
        self.vista_info_usuarios = VistaInfoUsuarios(self, controlador_info_usuarios)

        self.vista_inicio_filtros = VistaInicio(self, controlador_inicio_filtros)
        self.vista_filtros = VistaFiltros(self, controlador_filtros)
        self.vista_info_filtros = VistaInfoFiltros(self, controlador_info_filtros)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_info)

        self.ajustar_frame(self.vista_inicio_usuarios)
        self.ajustar_frame(self.vista_usuarios)
        self.ajustar_frame(self.vista_info_usuarios)

        self.ajustar_frame(self.vista_inicio_filtros)
        self.ajustar_frame(self.vista_filtros)
        self.ajustar_frame(self.vista_info_filtros)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()

root = tk.Tk()
root.title("Segunda ventana - App de musica")
controlador = ControladorPrincipal(root)
root.mainloop()
    
