# 🗃️ Sistema de Gestión de Inventario  

## Descripción 📋  
Sistema de gestión de inventario desarrollado con **Python** y **Tkinter** para la interfaz gráfica, con conexión a base de datos **PostgreSQL**. Permite realizar operaciones CRUD completas sobre productos.

---

## Características principales ✨  
- 🖥️ Interfaz gráfica moderna y responsive  
- 📦 Gestión completa de productos (Crear, Leer, Actualizar, Eliminar)  
- 🔍 Búsqueda y filtrado de productos  
- 🗄️ Conexión con base de datos PostgreSQL  
- 🎨 Estilos personalizados y tema oscuro/claro  

---

## Requisitos del sistema ⚙️  

### Software necesario
- Python 3.8+  
- PostgreSQL 12+  
- Bibliotecas Python:  
```bash
pip install -r requirements.txt
```

### Hardware recomendado
- 2GB RAM mínimo  
- 100MB espacio en disco  

---

## Instalación 🛠️  

### 1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/gestion-inventario.git
cd gestion-inventario
```

### 2. Configurar base de datos:
- Crear base de datos PostgreSQL llamada `inventario_db`  
- Configurar usuario y contraseña en el archivo `app.py`  

### 3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación:
```bash
python app.py
```

---

## Estructura del proyecto 📂  
```
gestion-inventario/
├── assets/               # Recursos gráficos
│   └── inventario.ico    # Icono de la aplicación
├── controllers/          # Lógica de control
│   └── producto_controller.py
├── models/               # Modelos de datos
│   └── producto_model.py
├── views/                # Interfaces de usuario
│   ├── main_view.py
│   └── producto_view.py
├── styles.py             # Estilos de la interfaz
├── app.py                # Punto de entrada
├── requirements.txt      # Dependencias
└── README.md             # Este archivo
```

---

## Configuración ⚙️  

Editar las siguientes variables en `app.py`:
```python
DB_CONFIG = {
    'db_name': 'inventario_db',
    'db_user': 'tu_usuario',
    'db_password': 'tu_contraseña',
    'db_host': 'localhost',
    'db_port': '5432'
}
```

---

## Uso básico 🖱️  

- **Menú principal**: Accede a todas las funciones desde la pantalla inicial  
- **Registrar producto**: Completa el formulario con los datos del producto  
- **Consultar productos**: Visualiza y filtra todos los productos registrados  
- **Actualizar producto**: Modifica la información de productos existentes  
- **Eliminar producto**: Remueve productos del inventario  

---
