import tkinter as tk

class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un evento.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.evento_label = tk.Label(self, text="")
        self.evento_label.pack(pady=50)
        self.evento_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar a la lista de eventos",
            command=self.controlador.regresar_eventos,
        )
        self.boton_regresar.pack(pady=10)

    def mostrar_info_evento(self, evento):
        """
        Muestra la información del evento recibido como parámetro.
        """
        info = f"Nombre: {evento.nombre}\nGénero: {evento.genero}\nArtista: {evento.artista}\nHora de inicio: {evento.hora_inicio}\nHora de finalizacion: {evento.hora_fin}\nImagen del lugar: {evento.descripcion}"
        self.evento_label["text"] = info
