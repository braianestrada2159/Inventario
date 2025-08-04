# Controlador para manejar la lógica de productos
class ProductoController:
    # Inicializa el controlador con el modelo y la ventana raíz
    def __init__(self, model, root):
        self.model = model
        self.root = root
        self.current_view = None
        self.producto_view = None
        
    # Inicializar la vista de producto
    def mostrar_menu_principal(self):
        """Muestra la vista principal cerrando ventanas secundarias"""
        if self.producto_view:
            self.producto_view.cerrar_ventana()
        if self.current_view:
            self.current_view.cerrar_ventana()
        
        # Limpiar la ventana actual
        from views.main_view import MainView
        self.current_view = MainView(self.root, self)
    
    # Método para mostrar el formulario de registro de producto
    def mostrar_registro_producto(self):
        """Muestra el formulario de registro de producto"""
        from views.producto_view import ProductoView
        self.producto_view = ProductoView(self.root, self, "registrar producto")
        self.producto_view.mostrar_formulario_registro()
    
    # Método para mostrar la lista de productos
    def mostrar_consulta_productos(self):
        """Muestra la lista de productos"""
        # Verifica si ya hay una vista de producto abierta
        try:
            productos = self.model.obtener_productos()
            from views.producto_view import ProductoView
            self.producto_view = ProductoView(self.root, self, "consultar productos")
            self.producto_view.mostrar_lista_productos(productos)
        # Manejo de excepciones para errores al obtener productos
        except Exception as e:
            if self.producto_view:
                self.producto_view.mostrar_error(str(e))
    
    # Método para mostrar formulario de actualización de producto
    def mostrar_actualizacion_producto(self):
        """Muestra el formulario para actualizar producto"""
        from views.producto_view import ProductoView
        self.producto_view = ProductoView(self.root, self, "actualizar producto")
        self.producto_view.mostrar_formulario_actualizacion()
    
    # Método para mostrar formulario de eliminación de producto
    def mostrar_eliminacion_producto(self):
        """Muestra el formulario para eliminar producto"""
        from views.producto_view import ProductoView
        self.producto_view = ProductoView(self.root, self, "eliminar producto")
        self.producto_view.mostrar_formulario_eliminacion()
    
    # Métodos para manejar acciones de productos
    def guardar_producto(self):
        """Guarda un nuevo producto con validación mejorada"""
        try:
            datos = self.producto_view.obtener_datos_producto()
            
            # Validación mejorada
            if not datos['nombre']:
                raise ValueError("El nombre es obligatorio")
            
            # Validación de precio y cantidad
            try:
                precio = float(datos['precio'])
                cantidad = int(datos['cantidad'])
            except ValueError:
                raise ValueError("Precio debe ser un número y cantidad un entero")
            
            # Verificar que precio y cantidad sean positivos
            if precio <= 0 or cantidad < 0:
                raise ValueError("Precio y cantidad deben ser valores positivos")
            
            # Crear producto
            self.model.crear_producto(
                datos['nombre'],
                datos['descripcion'],
                precio,
                cantidad,
                datos['categoria']
            )
            
            # Actualizar lista de productos
            self.producto_view.mostrar_info("Producto registrado correctamente")
            self.producto_view.cerrar_ventana()

        # Excepciones específicas para manejo de errores 
        except Exception as e:
            self.producto_view.mostrar_error(str(e))
    
    # Método para buscar un producto por ID para actualizar
    def buscar_producto_para_actualizar(self):
        """Busca un producto para actualizar"""
        id_producto = self.producto_view.obtener_id_producto()
        
        # Validación del ID ingresado
        if not id_producto:
            self.producto_view.mostrar_error("Debe ingresar un ID de producto")
            return
        
        # Manejo de excepciones al buscar el producto
        try:
            productos = self.model.obtener_productos()
            producto = next((p for p in productos if str(p[0]) == id_producto), None)
            
            # Si se encuentra el producto, mostrar formulario de edición
            if producto:
                self.producto_view.current_product_id = producto[0]  # Guardar el ID
                self.producto_view.mostrar_formulario_edicion(producto)
            # Si no se encuentra el producto, mostrar mensaje
            else:
                self.producto_view.mostrar_info("No se encontró un producto con ese ID")
        # Manejo de excepciones para errores al buscar el producto
        except ValueError:
            self.producto_view.mostrar_error("El ID debe ser un número válido")
        except Exception as e:
            self.producto_view.mostrar_error(str(e))
    
    # Método para guardar los cambios de un producto actualizado
    def guardar_actualizacion(self):
        """Guarda los cambios de un producto actualizado"""
        # Manejo de excepciones al guardar la actualización
        try:
            if not hasattr(self.producto_view, 'current_product_id'):
                raise ValueError("No se ha seleccionado ningún producto para actualizar")
                
            datos = self.producto_view.obtener_datos_producto()
            id_producto = self.producto_view.current_product_id
            
            # Validación mejorada
            if not datos['nombre']:
                raise ValueError("El nombre es obligatorio")

            # Validación de precio y cantidad    
            try:
                precio = float(datos['precio'])
                cantidad = int(datos['cantidad'])
            except ValueError:
                raise ValueError("Precio debe ser un número y cantidad un entero")
            
            # Verificar que precio y cantidad sean positivos
            if precio <= 0 or cantidad < 0:
                raise ValueError("Precio y cantidad deben ser valores positivos")
            
            # Actualizar producto
            actualizado = self.model.actualizar_producto(
                id_producto,
                datos['nombre'],
                datos['descripcion'],
                precio,
                cantidad,
                datos['categoria']
            )
            
            # Si se actualiza correctamente, mostrar mensaje y cerrar ventana
            if actualizado:
                self.producto_view.mostrar_info("Producto actualizado correctamente")
                self.producto_view.cerrar_ventana()
            else:
                raise Exception("No se pudo actualizar el producto")

        # Manejo de excepciones para errores al guardar la actualización        
        except Exception as e:
            self.producto_view.mostrar_error(str(e))
    
    # Método para actualizar la lista de productos en la vista
    def actualizar_lista_productos(self):
        """Actualiza la lista de productos en la vista"""
        # Manejo de excepciones al actualizar la lista de productos
        try:
            productos = self.model.obtener_productos()
            self.producto_view.tree.delete(*self.producto_view.tree.get_children())
            
            # Insertar cada producto en el Treeview
            for producto in productos:
                self.producto_view.tree.insert("", "end", values=producto)
                
            self.producto_view.mostrar_info("Lista de productos actualizada")
        except Exception as e:
            self.producto_view.mostrar_error(f"Error al actualizar: {str(e)}")
    
    # Método para confirmar la eliminación de un producto
    def confirmar_eliminacion(self):
        """Confirma y ejecuta la eliminación de un producto"""
        id_producto = self.producto_view.obtener_id_producto()
        
        # Validación del ID ingresado
        if not id_producto:
            self.producto_view.mostrar_error("Debe ingresar un ID de producto")
            return
        
        # Manejo de excepciones al eliminar el producto
        if self.producto_view.confirmar_eliminacion():
            try:
                eliminado = self.model.eliminar_producto(id_producto)
                
                # Si se elimina correctamente, mostrar mensaje y cerrar ventana
                if eliminado:
                    self.producto_view.mostrar_info("Producto eliminado correctamente")
                    self.producto_view.cerrar_ventana()
                else:
                    self.producto_view.mostrar_info("No se encontró un producto con ese ID")
            except ValueError:
                self.producto_view.mostrar_error("El ID debe ser un número válido")
            except Exception as e:
                self.producto_view.mostrar_error(str(e))