import tkinter as tk
from tkinter import ttk, messagebox
from app import get_resource_path
from .styles import configure_styles

# Clase que representa la vista de productos
class ProductoView:
    def __init__(self, parent, controller, window_type):
        self.parent = parent
        self.controller = controller
        self.window_type = window_type
        self.style = configure_styles()
        
        self._setup_window()
        self._create_back_button()
        
    # Configura la ventana según el tipo (registro, consulta, actualización, eliminación)
    def _setup_window(self):
        self.window = tk.Toplevel(self.parent)
        self.window.title(f"Sistema de Inventario - {self.window_type.capitalize()}")
        self.window.state('zoomed')
        self.window.configure(bg=self.style.lookup('TFrame', 'background'))
        
        # Configurar el icono
        try:
            icon_path = get_resource_path('assets/inventario.ico')
            self.window.iconbitmap(icon_path)
        except Exception as e:
            print(f"No se pudo cargar el icono: {e}")

    # Crea el botón de regreso al menú principal
    def _create_back_button(self):
        """Crea el botón de regreso al menú principal"""
        back_frame = ttk.Frame(self.window, style='TFrame')
        back_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Botón de regreso
        ttk.Button(back_frame, text="← Menú Principal", 
                command=self.controller.mostrar_menu_principal,
                style='TButton').pack(side=tk.LEFT, padx=5, pady=5)
    
    # Muestra el formulario de registro de productos
    def mostrar_formulario_registro(self):
        """Muestra el formulario para registrar nuevos productos"""
        main_frame = ttk.Frame(self.window, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
        
        # Marco del formulario con estilo de tarjeta
        form_frame = ttk.Frame(main_frame, style='Card.TFrame')
        form_frame.pack(pady=20, padx=100, fill=tk.X)
        
        # Título del formulario
        ttk.Label(form_frame, text="Registrar Nuevo Producto", 
                style='Title.TLabel').grid(row=0, columnspan=2, pady=(10, 20))
        
        # Campos del formulario
        ttk.Label(form_frame, text="Nombre:", style='TLabel').grid(row=1, column=0, padx=15, pady=10, sticky=tk.E)
        self.nombre_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.nombre_entry.grid(row=1, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para descripción
        ttk.Label(form_frame, text="Descripción:", style='TLabel').grid(row=2, column=0, padx=15, pady=10, sticky=tk.E)
        self.descripcion_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.descripcion_entry.grid(row=2, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para precio
        ttk.Label(form_frame, text="Precio:", style='TLabel').grid(row=3, column=0, padx=15, pady=10, sticky=tk.E)
        self.precio_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.precio_entry.grid(row=3, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para cantidad
        ttk.Label(form_frame, text="Cantidad:", style='TLabel').grid(row=4, column=0, padx=15, pady=10, sticky=tk.E)
        self.cantidad_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.cantidad_entry.grid(row=4, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para categoría
        ttk.Label(form_frame, text="Categoría:", style='TLabel').grid(row=5, column=0, padx=15, pady=10, sticky=tk.E)
        self.categoria_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.categoria_entry.grid(row=5, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Botón para guardar
        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.pack(pady=20)
        
        # Botón para guardar el producto
        ttk.Button(button_frame, text="Guardar Producto", 
                command=self.controller.guardar_producto,
                style='Success.TButton').pack(pady=10, ipadx=20, ipady=5)
    
    # Muestra la lista de productos en un Treeview
    def mostrar_lista_productos(self, productos):
        """Muestra la lista de productos en un Treeview con estilo mejorado"""
        main_frame = ttk.Frame(self.window, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título de la sección
        ttk.Label(main_frame, text="Lista de Productos", 
                style='Title.TLabel').pack(pady=(0, 20))
        
        # Contenedor del Treeview con scrollbar
        tree_container = ttk.Frame(main_frame, style='Card.TFrame')
        tree_container.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
        
        # Treeview con estilo mejorado
        self.tree = ttk.Treeview(tree_container, 
                                columns=("ID", "Nombre", "Descripción", "Precio", "Cantidad", "Categoría"), 
                                show="headings",
                                style='Treeview')
        
        # Configurar columnas
        columns = [
            ("ID", 50, tk.CENTER),
            ("Nombre", 150, tk.W),
            ("Descripción", 250, tk.W),
            ("Precio", 80, tk.E),
            ("Cantidad", 80, tk.CENTER),
            ("Categoría", 120, tk.W)
        ]
        
        # Configurar encabezados y columnas
        for col, width, anchor in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=anchor)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_container, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Insertar datos
        for producto in productos:
            self.tree.insert("", "end", values=producto)
        
        # Botón de actualizar
        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.pack(pady=20)
        
        # Botón para actualizar la lista de productos
        ttk.Button(button_frame, text="Actualizar Lista", 
                command=self.controller.actualizar_lista_productos,
                style='TButton').pack(pady=5, ipadx=15, ipady=3)
    
    # Muestra el formulario para actualizar un producto
    def mostrar_formulario_actualizacion(self):
        """Muestra el formulario para buscar producto a actualizar"""
        main_frame = ttk.Frame(self.window, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        
        # Marco del formulario con estilo de tarjeta
        form_frame = ttk.Frame(main_frame, style='Card.TFrame')
        form_frame.pack(pady=20, padx=100)
        
        # Título
        ttk.Label(form_frame, text="Actualizar Producto", 
                style='Title.TLabel').grid(row=0, columnspan=2, pady=(10, 20))
        
        # Campo para buscar por ID
        ttk.Label(form_frame, text="ID del Producto:", style='TLabel').grid(row=1, column=0, padx=15, pady=10, sticky=tk.E)
        self.id_entry = ttk.Entry(form_frame, style='TEntry', width=30)
        self.id_entry.grid(row=1, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Botón de búsqueda
        button_frame = ttk.Frame(form_frame, style='TFrame')
        button_frame.grid(row=2, columnspan=2, pady=20)
        
        # Botón para buscar producto
        ttk.Button(button_frame, text="Buscar Producto", 
                command=self.controller.buscar_producto_para_actualizar,
                style='TButton').pack(ipadx=15, ipady=3)
    
    # Muestra el formulario de edición con los datos del producto
    def mostrar_formulario_edicion(self, producto):
        """Muestra el formulario de edición con los datos del producto"""
        # Limpiar la ventana
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Guardar el ID del producto actual
        self.current_product_id = producto[0]

        # Volver a crear el botón de regreso
        self._create_back_button()
        
        # Marco principal
        main_frame = ttk.Frame(self.window, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
        
        # Marco del formulario
        form_frame = ttk.Frame(main_frame, style='Card.TFrame')
        form_frame.pack(pady=20, padx=100, fill=tk.X)
        
        # Título
        ttk.Label(form_frame, text=f"Editando Producto ID: {producto[0]}", 
                style='Title.TLabel').grid(row=0, columnspan=2, pady=(10, 20))
        
        # Campos del formulario con los datos actuales
        ttk.Label(form_frame, text="Nombre:", style='TLabel').grid(row=1, column=0, padx=15, pady=10, sticky=tk.E)
        self.nombre_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.nombre_entry.insert(0, producto[1])
        self.nombre_entry.grid(row=1, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para descripción
        ttk.Label(form_frame, text="Descripción:", style='TLabel').grid(row=2, column=0, padx=15, pady=10, sticky=tk.E)
        self.descripcion_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.descripcion_entry.insert(0, producto[2])
        self.descripcion_entry.grid(row=2, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para precio
        ttk.Label(form_frame, text="Precio:", style='TLabel').grid(row=3, column=0, padx=15, pady=10, sticky=tk.E)
        self.precio_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.precio_entry.insert(0, producto[3])
        self.precio_entry.grid(row=3, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para cantidad
        ttk.Label(form_frame, text="Cantidad:", style='TLabel').grid(row=4, column=0, padx=15, pady=10, sticky=tk.E)
        self.cantidad_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.cantidad_entry.insert(0, producto[4])
        self.cantidad_entry.grid(row=4, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Campo para categoría
        ttk.Label(form_frame, text="Categoría:", style='TLabel').grid(row=5, column=0, padx=15, pady=10, sticky=tk.E)
        self.categoria_entry = ttk.Entry(form_frame, style='TEntry', width=40)
        self.categoria_entry.insert(0, producto[5] if producto[5] else "")
        self.categoria_entry.grid(row=5, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Botón para guardar cambios
        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.pack(pady=20)
        
        # Botón para guardar los cambios
        ttk.Button(button_frame, text="Guardar Cambios", 
                command=self.controller.guardar_actualizacion,
                style='Success.TButton').pack(pady=10, ipadx=20, ipady=5)
    
    # Muestra el formulario para eliminar un producto
    def mostrar_formulario_eliminacion(self):
        """Muestra el formulario para eliminar producto"""
        main_frame = ttk.Frame(self.window, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        
        # Marco del formulario con estilo de tarjeta
        form_frame = ttk.Frame(main_frame, style='Card.TFrame')
        form_frame.pack(pady=20, padx=150)
        
        # Título
        ttk.Label(form_frame, text="Eliminar Producto", 
                style='Title.TLabel').grid(row=0, columnspan=2, pady=(10, 20))
        
        # Campo para ingresar ID
        ttk.Label(form_frame, text="ID del Producto:", style='TLabel').grid(row=1, column=0, padx=15, pady=10, sticky=tk.E)
        self.id_entry = ttk.Entry(form_frame, style='TEntry', width=30)
        self.id_entry.grid(row=1, column=1, padx=15, pady=10, sticky=tk.W)
        
        # Botón para confirmar eliminación
        button_frame = ttk.Frame(form_frame, style='TFrame')
        button_frame.grid(row=2, columnspan=2, pady=20)
        
        # Botón para buscar producto a eliminar
        ttk.Button(button_frame, text="Eliminar Producto", 
                command=self.controller.confirmar_eliminacion,
                style='Danger.TButton').pack(ipadx=15, ipady=3)
    
    # Métodos para obtener datos del formulario
    def obtener_datos_producto(self):
        """Obtiene los datos del formulario de producto"""
        return {
            'nombre': self.nombre_entry.get(),
            'descripcion': self.descripcion_entry.get(),
            'precio': self.precio_entry.get(),
            'cantidad': self.cantidad_entry.get(),
            'categoria': self.categoria_entry.get()
        }
    
    # Método para obtener el ID del producto
    def obtener_id_producto(self):
        """Obtiene el ID del producto del campo de entrada"""
        return self.id_entry.get()
    
    # Métodos para mostrar mensajes
    def mostrar_error(self, mensaje):
        """Muestra un mensaje de error con estilo"""
        messagebox.showerror("Error", mensaje, parent=self.window)
    
    # Muestra un mensaje de éxito
    def mostrar_info(self, mensaje):
        """Muestra un mensaje informativo con estilo"""
        messagebox.showinfo("Información", mensaje, parent=self.window)
    
    # Método para confirmar eliminación
    def confirmar_eliminacion(self):
        """Muestra diálogo de confirmación para eliminar"""
        return messagebox.askyesno(
            "Confirmar Eliminación",
            "¿Está seguro que desea eliminar este producto?",
            parent=self.window
        )
    
    # Cierra la ventana actual
    def cerrar_ventana(self):
        """Cierra la ventana actual"""
        self.window.destroy()