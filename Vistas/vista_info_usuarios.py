import tkinter as tk

class VistaInfoUsuarios(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un historial.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.usuario_label = tk.Label(self, text="")
        self.usuario_label.pack(pady=50)
        self.usuario_label.config(justify=tk.LEFT)
        self.boton_regresar_usuario = tk.Button(
            self,
            text="Regresar a la lista de usuarios",
            command=self.controlador.regresar_usuarios,
        )
        self.boton_regresar_usuario.pack(pady=10)

    def mostrar_info_usuario(self, usuario):
        """
        Muestra la información del usuario recibido como parámetro.
        """
        info = f"Nombre: {usuario.nombre}\nApellido: {usuario.apellido}\nEventos asistidos: {usuario.historial_eventos}"
        self.usuario_label["text"] = info