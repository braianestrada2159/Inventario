import tkinter as tk
from tkinter import ttk
from .styles import configure_styles

# Clase que representa la vista principal de la aplicación
class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.style = configure_styles()
        
        # Limpiar ventana existente
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Configurar la ventana principal
        self._setup_main_window()
        self._create_widgets()
        
    # Configura la ventana principal
    def _setup_main_window(self):
        """Configura la ventana principal"""
        self.root.title("Sistema de Gestión de Inventario")
        self.root.state('zoomed')
        self.root.configure(bg=self.style.lookup('TFrame', 'background'))

    # Crea todos los widgets de la interfaz   
    def _create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        # Frame principal con padding
        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_frame = ttk.Frame(main_frame, style='TFrame')
        title_frame.pack(pady=(20, 40))
        
        ttk.Label(title_frame, text="Sistema de Gestión de Inventario", 
                style='Title.TLabel').pack()
        
        # Marco para los botones con estilo de tarjeta
        button_frame = ttk.Frame(main_frame, style='Card.TFrame')
        button_frame.pack(pady=20, padx=100, fill=tk.BOTH, expand=True)
        
        # Configurar grid para centrar los botones
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)
        
        # Botones del menú principal
        ttk.Button(button_frame, text="Registrar nuevo Producto", 
            command=self.controller.mostrar_registro_producto,
            style='Success.TButton').grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        
        # Consultar productos
        ttk.Button(button_frame, text="Consultar Productos", 
            command=self.controller.mostrar_consulta_productos,
            style='TButton').grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        
        # Actualizar productos
        ttk.Button(button_frame, text="Actualizar Producto", 
            command=self.controller.mostrar_actualizacion_producto,
            style='TButton').grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        
        # Eliminar productos
        ttk.Button(button_frame, text="Eliminar Productos", 
            command=self.controller.mostrar_eliminacion_producto,
            style='Danger.TButton').grid(row=1, column=1, padx=20, pady=20, sticky='nsew')