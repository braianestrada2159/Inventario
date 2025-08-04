from tkinter import ttk
import tkinter as tk

# Función para configurar los estilos de la aplicación
def configure_styles():
    style = ttk.Style()
    style.theme_use('clam')
    
    # Colores principales
    primary_color = '#2c3e50'
    secondary_color = '#3498db'
    success_color = '#27ae60'
    danger_color = '#e74c3c'
    light_bg = '#ecf0f1'
    dark_text = '#2c3e50'
    
    # Configuración general
    style.configure('.', 
                font=('Segoe UI', 10),
                background=light_bg,
                foreground=dark_text)
    
    # Configurar estilo de botones
    style.configure('TButton', 
                font=('Segoe UI', 10, 'bold'),
                padding=8,
                borderwidth=1,
                relief='raised',
                background=secondary_color,
                foreground='white')
    
    # Cambiar color de fondo del botón al pasar el mouse
    style.map('TButton',
            background=[('active', primary_color), ('pressed', primary_color)],
            relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
    
    # Botones de éxito (guardar, confirmar)
    style.configure('Success.TButton', 
            background=success_color)
    
    # Botones de peligro (eliminar, cancelar)
    style.configure('Danger.TButton', 
            background=danger_color)
    
    # Configurar estilo de labels
    style.configure('TLabel', 
            font=('Segoe UI', 10),
            padding=5)
    
    # Configurar estilo de títulos
    style.configure('Title.TLabel',
            font=('Segoe UI', 18, 'bold'),
            foreground=primary_color)
    
    # Configurar estilo de entries
    style.configure('TEntry', 
            font=('Segoe UI', 10),
            padding=6,
            relief='solid',
            borderwidth=1)
    
    # Configurar estilo del Treeview
    style.configure("Treeview",
            font=('Segoe UI', 9),
            rowheight=28,
            background='white',
            fieldbackground='white',
            foreground=dark_text)
    
    # Configurar encabezados del Treeview
    style.configure("Treeview.Heading",
            font=('Segoe UI', 10, 'bold'),
            background=primary_color,
            foreground='white',
            padding=5)
    
    # Cambiar color de fondo del encabezado al pasar el mouse
    style.map('Treeview.Heading',
            background=[('active', secondary_color)])
    
    # Configurar estilo de los frames
    style.configure('TFrame',
            background=light_bg)
    
    # Configurar estilo de los frames tipo tarjeta
    style.configure('Card.TFrame',
            background='white',
            relief='raised',
            borderwidth=1,
            padding=10)
    
    return style