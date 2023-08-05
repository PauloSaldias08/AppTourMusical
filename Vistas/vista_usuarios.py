import tkinter as tk

class VistaUsuarios(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la lista de los usuarios.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        self.titulo = tk.Label(self, text="Usuarios registrados, haga doble clic en usuario para observar su historial")
        self.titulo.pack(pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        # Asocia el historial de doble clic a la función seleccionar_historial
        self.listbox.bind("<Double-Button-1>", self.seleccionar_usuario)

        self.listbox.pack(pady=10)
        self.actualizar_usuarios()

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = tk.Button(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.pack(pady=10)

    def actualizar_usuarios(self):
        """
        Actualiza la lista de usuarios con los usuarios obtenidos del controlador.
        """
        usuarios = self.controlador.obtener_usuarios()
        self.listbox.delete(0, tk.END)
        for usuario in usuarios:
            self.listbox.insert(tk.END, usuario.nombre)

    def obtener_usuario_seleccionado(self):
        """
        Retorna el índice del historial seleccionado en la lista.
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_usuario(self, e):
        """
        Obtiene el índice del evento seleccionado y llama al controlador para
        mostrar la información del evento.
        """
        self.controlador.seleccionar_usuario()