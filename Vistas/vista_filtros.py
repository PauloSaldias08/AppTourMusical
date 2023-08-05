import tkinter as tk

class VistaFiltros(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la lista de los filtros.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        self.titulo = tk.Label(self, text="Lista de nombres de los principales eventos")
        self.titulo.pack(pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        # Asocia el nombre del evento al doble clic a la función seleccionar_filtro
        self.listbox.bind("<Double-Button-1>", self.seleccionar_filtro)

        self.listbox.pack(pady=10)
        self.actualizar_filtros()

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = tk.Button(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.pack(pady=10)

    def actualizar_filtros(self):
        """
        Actualiza la lista de filtros con los filtros obtenidos del controlador.
        """
        filtros = self.controlador.obtener_filtros()
        self.listbox.delete(0, tk.END)
        for filtro in filtros:
            self.listbox.insert(tk.END, filtro.nombre)

    def obtener_filtro_seleccionado(self):
        """
        Retorna el índice del filtro seleccionado en la lista.
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_filtro(self, ev):
        """
        Obtiene el índice del evento seleccionado y llama al controlador para
        mostrar la información del evento.
        """
        self.controlador.seleccionar_filtro()