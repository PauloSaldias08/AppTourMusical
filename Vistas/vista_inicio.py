import tkinter as tk
from tkinter.font import Font


class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.controlador1 = controlador
        self.controlador2 = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="App de musica", font=titulo_font)
        self.titulo.grid(row=0, column=1, pady=5)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(size=12)

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text="Aquí puedes ver y seleccionar tus eventos musicales favoritos con información detallada.",
            font=descripcion_font,
            wraplength=300,
        )
        self.descripcion.grid(row=1, column=1, pady=50)

        # Crea el botón para ir a eventos y lo agrega a la vista
        self.boton_eventos = tk.Button(
            self, text="Ir a eventos", command=self.controlador.mostrar_eventos
        )
        self.boton_eventos.grid(row=2, column=0, pady=10)
        # Crea el botón para ir a historial y lo agrega a la vista
        self.boton_usuarios = tk.Button(
            self, text="Usuarios registrados", command=self.controlador1.mostrar_usuarios
        )
        self.boton_usuarios.grid(row=2, column=1, pady=10)
         # Crea el botón para ir a filtros y lo agrega a la vista
        self.boton_filtros = tk.Button(
            self, text="Filtrar por nombre de evento", command=self.controlador2.mostrar_filtros
        )
        self.boton_filtros.grid(row=2, column=2, pady=10)
