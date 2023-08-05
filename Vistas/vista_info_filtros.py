import tkinter as tk
from Modelos.evento import Evento

class VistaInfoFiltros(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un historial.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.filtro_label = tk.Label(self, text="")
        self.filtro_label.pack(pady=50)
        self.filtro_label.config(justify=tk.LEFT)
        self.boton_regresar_filtro = tk.Button(
            self,
            text="Regresar a la lista de nombres",
            command=self.controlador.regresar_filtros,
        )
        self.boton_regresar_filtro.pack(pady=10)

    def mostrar_info_filtro(self, filtro):
        """
        Muestra la información del evento recibido como parámetro.
        """
        info = f"Nombre: {filtro.nombre}\nGenero: {filtro.genero}\nArtista: {filtro.artista}"
        self.filtro_label["text"] = info

import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

class VistaPrincipal:
    def __init__(self, root, seleccionar_local_callback=None, seleccionar_ubicacion_callback=None):
        self.root = root
        self.seleccionar_local_callback = seleccionar_local_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.frame_mapa = tk.Frame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='right')

        self.frame_locales = tk.Frame(self.root, width=300, height=600)
        self.frame_locales.pack(side='left', fill='both', expand=True)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.7892121, -65.4102818) #Lugar donde empezara la ubicacion de maps
        self.mapa.set_zoom(16) #Seteo del zoom inicial
        self.mapa.pack(side='right')

        # Listbox para los locales
        self.lista_locales = tk.Listbox(self.frame_locales)
        self.lista_locales.bind('<<ListboxSelect>>', seleccionar_local_callback)
        self.lista_locales.pack(fill='both', expand=True)

    def agregar_local(self, local):
        nombre = local.nombre
        self.lista_locales.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)