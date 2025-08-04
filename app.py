import tkinter as tk
import os
import sys
from models.producto_model import ProductoModel
from controllers.producto_controller import ProductoController

# Configuración de la base de datos
DB_CONFIG = {
    'db_name': 'inventario_db',
    'db_user': 'postgres',
    'db_password': 'Medellin12345',
    'db_host': 'localhost',
    'db_port': '5432'
}

# Función para obtener la ruta absoluta de los recursos
def get_resource_path(relative_path):
    """Obtiene la ruta absoluta al recurso, funciona para desarrollo y para ejecutables empaquetados"""
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Punto de entrada de la aplicación
def main():
    try:
        # Inicializar la aplicación
        root = tk.Tk()
        
        # Configurar el título de la aplicación
        root.title("Sistema de Gestión de Inventario")
        
        # Configurar el icono de la aplicación
        try:
            icon_path = get_resource_path('assets/inventario.ico')
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Advertencia: No se pudo cargar el icono - {e}")
            # Opcional: Puedes usar un icono por defecto de tkinter aquí
        
        # Crear modelo de base de datos
        model = ProductoModel(**DB_CONFIG)
        
        # Crear controlador principal
        controller = ProductoController(model, root)
        
        # Mostrar la vista principal
        controller.mostrar_menu_principal()
        
        # Configurar el comportamiento al cerrar la ventana
        def on_closing():
            if messagebox.askokcancel("Salir", "¿Está seguro que desea salir de la aplicación?"):
                model.cerrar_conexion()
                root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Ejecutar el bucle principal de la aplicación
        root.mainloop()
    
    # Manejo de excepciones para errores críticos
    except Exception as e:
        # Mostrar errores críticos al usuario
        error_msg = f"Error al iniciar la aplicación: {str(e)}"
        print(error_msg)
        tk.messagebox.showerror("Error", error_msg)
    finally:
        # Asegurarse de cerrar la conexión a la base de datos
        if 'model' in locals():
            model.cerrar_conexion()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    from tkinter import messagebox
    main()