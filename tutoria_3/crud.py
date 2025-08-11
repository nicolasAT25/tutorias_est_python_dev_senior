from clases import Categoria, Producto
import os

inventario = []
id_producto = 1

def agregar_producto():
    """
    Solicita los datos del producto al usuario y lo agrega al inventario.
    Garantiza que la cantidad y el precio sean números válidos.
    """
    
    global id_producto
    
    while True:
        try:
            categoria_nombre = input("Ingrese el nombre de la categoría del producto: ").strip().title()
            
            if not categoria_nombre.isalpha():
                raise ValueError("El nombre de la categoría debe contener solo letras.")
            if not categoria_nombre:
                raise ValueError("El nombre de la categoría no puede estar vacío.")
            
        except ValueError as e:
            print(f"Valor inválido: {e}")
            
        except Exception as e:
            print(f"ERROR. {e}")
            
        else:
            break
        
    while True:
        try:
            subcategoria_nombre = input("Ingrese el nombre de la subcategoría del producto: ").strip().title()
            if not subcategoria_nombre.isalpha():
                raise ValueError("El nombre de la categoría debe contener solo letras.")
            if not subcategoria_nombre:
                raise ValueError("El nombre de la categoría no puede estar vacío.")
            
        except ValueError as e:
            print(f"❌ Valor inválido: {e}")
            
        except Exception as e:
            print(f"ERROR. {e}")
        
        else:
            break
        
    # Validar que el nombre del producto no contenga números
    while True:
        try:
            producto = input("Ingrese el nombre del producto: ").strip().title()
            if not producto.isalpha():
                raise ValueError(f"❌El nombre del producto no debe contener números. Nombre de producto ingresado '{producto}'")
        
        except Exception as e:
            print(f"ERROR. {e}")
        
        else:
            break
        
    # Validación de la cantidad (solo acepta números enteros positivos)
    while True:
        try:
            cantidad = input("Ingrese la cantidad inicial en inventario: ")
            
            if not cantidad.isdigit():
                raise ValueError(f"La cantidad de inventario inicial debe ser un número entero positivo. Cantidad ingresada '{cantidad}'")           
        except Exception as e:
            print(f"ERROR. {e}")
        else:
            cantidad = int(cantidad)
            break
        
    # Validación del precio unitario (solo acepta números decimales positivos)
    while True:
        try:
            precio_unitario = input("Ingrese el precio unitario del producto: ")
            
            if not (precio_unitario.replace(".", "").isdigit() or precio_unitario.replace(",", "").isdigit()):
                raise ValueError(f"❌ Entrada inválida! El precio debe ser un número positivo (ej: 10.50). {precio_unitario}")
        
        except ValueError as e:
            print(f"❌ Valor inválido: {e}")
        
        except Exception as e:
            print(f"ERROR. {e}")
        else:
            if precio_unitario.__contains__(","):
                precio_unitario = float(precio_unitario.replace(",", "."))
            else:
                precio_unitario = float(precio_unitario)
            break
        
    nuevo_producto = Producto(
        nombre=producto,
        cantidad=cantidad,
        precio_unitario=precio_unitario,
        categoria=Categoria(nombre=categoria_nombre, subcategoria=subcategoria_nombre),
        id=id_producto
    )
    
    # Agregando el producto al inventario
    inventario.append(nuevo_producto)
    id_producto += 1
    
    print(f"\n✅ ¡Producto '{producto}' agregado al inventario!")
    
def mostrar_inventario():
    """
    Muestra todos los productos registrados en el inventario.
    """
    if not inventario:
        print("\n⚠️ ¡El inventario está vacío!")
        return

    print("\n📦 Inventario Actualizado")
    print("-" * 40)
    for producto in inventario:
        print(f"{producto}")
        print("-" * 40)
    
def actualizar_producto():
    """
    Actualiza la cantidad y el precio unitario de un producto existente en el inventario.

    Parámetros:
    - None

    Retorno:
    - None
    """
    mostrar_inventario()
    
    while True:
        try:
            id_producto_actualizar = input("Ingrese el ID del producto a actualizar: ").strip()
            if not id_producto_actualizar.isdigit():
                raise ValueError("❌ El ID debe ser un número entero.")
        
            if int(id_producto_actualizar) < 1 or int(id_producto_actualizar) >= id_producto:
                raise ValueError(f"❌ ID inválido. El ID debe estar entre 1 y {id_producto}.")
            
            if id_producto_actualizar == None or id_producto_actualizar == "":
                raise ValueError("❌ El ID no puede estar vacío.")
        
        except ValueError as e:
            print(f"❌ Valor inválido: {e}")
        
        except Exception as e:
            print(f"ERROR. {e}")
            
        else:
            id_producto_actualizar = int(id_producto_actualizar)
            break
        
        
    for producto in inventario:
        if producto.id == id_producto_actualizar:
            producto_actualizar = producto
    
    os.system("cls" if os.name == "nt" else "clear") 
    
    try:
        if not inventario:
            raise ValueError("⚠️ ¡El inventario está vacío!")
        
    except ValueError as e:
        print(f"❌ Valor inválido: {e}")
        
    except Exception as e:
        print(f"ERROR. {e}")
        
    else:
        # Agregar una categoría al producto
        while True:
            try:
                nueva_categoria = input("Ingrese el nombre de la categoría del producto: ").strip().title() or producto_actualizar.categoria.nombre
                # if not nueva_categoria.isalpha():
                #     raise ValueError("El nombre de la categoría debe contener solo letras.")
                if not nueva_categoria:
                    raise ValueError("El nombre de la categoría no puede estar vacío.")
                
            except ValueError as e:
                print(f"❌ Valor inválido: {e}")
                
            except Exception as e:
                print(f"ERROR. {e}")
            
            else:
                break
        
        # Agregar una subcategoría al producto
        while True:
            try:
                nueva_subcategoria = input("Ingrese el nombre de la nueva subcategoría del producto: ").strip().title() or producto_actualizar.categoria.subcategoria
                # if not nueva_categoria.isalpha():
                #     raise ValueError("El nombre de la categoría debe contener solo letras.")
                if not nueva_subcategoria:
                    raise ValueError("El nombre de la categoría no puede estar vacío.")
                
            except ValueError as e:
                print(f"❌ Valor inválido: {e}")
                
            except Exception as e:
                print(f"ERROR. {e}")
            
            else:
                break
        
        
        # Validar que el nombre del producto no contenga números
        while True:
            try:
                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip().title() or producto_actualizar.nombre
                if not nuevo_nombre.isalpha():
                    raise ValueError(f"❌El nombre del producto no debe contener números. Nombre de producto ingresado '{producto}'")
            
            except Exception as e:
                print(f"ERROR. {e}")
            
            else:
                break
        
        # Validación de la cantidad (solo acepta números enteros positivos)  
        while True:
            try:
                nueva_cantidad = input("Ingrese la nueva cantidad inicial en inventario: ") or producto_actualizar.cantidad
                if not str(nueva_cantidad).isdigit():
                    raise ValueError(f"La cantidad de inventario inicial debe ser un número entero positivo. Cantidad ingresada '{nueva_cantidad}'")           
            except Exception as e:
                print(f"ERROR. {e}")
            else:
                nueva_cantidad = int(nueva_cantidad)
                break

        # Validación del precio unitario (solo acepta números decimales positivos)
        while True:
            try:
                nuevo_precio_unitario = input("Ingrese el nuevo precio unitario del producto: ") or producto_actualizar.precio_unitario
                if not (str(nuevo_precio_unitario).replace(".", "").isdigit() or str(nuevo_precio_unitario).replace(",", "").isdigit()):
                    raise ValueError(f"❌ Entrada inválida! El precio debe ser un número positivo (ej: 10.50). {nuevo_precio_unitario}")
            except Exception as e:
                print(f"ERROR. {e}")
            else:
                if str(nuevo_precio_unitario).__contains__(","):
                    nuevo_precio_unitario = float(nuevo_precio_unitario.replace(",", "."))
                    # nuevo_precio_unitario = float(nuevo_precio_unitario.replace(",", "."))
                else:
                    nuevo_precio_unitario = float(nuevo_precio_unitario)
                    # nuevo_precio_unitario = float(nuevo_precio_unitario)
                break
            
                
        # Actualizando los datos del producto
        producto_actualizar.nombre = nuevo_nombre
        producto_actualizar.cantidad = nueva_cantidad
        producto_actualizar.precio_unitario = nuevo_precio_unitario
        producto_actualizar.valor_total = producto_actualizar.cantidad * producto_actualizar.precio_unitario
        producto_actualizar.categoria = Categoria(nombre=nueva_categoria, subcategoria=nueva_subcategoria)
        
        print(f"\n✅ ¡Producto '{producto_actualizar.nombre}' actualizado exitosamente!")
        
def eliminar_producto(producto_eliminar):
    """
    Elimina un producto del inventario según el nombre proporcionado.

    Parámetros:
    - producto_eliminar (str): Nombre del producto a eliminar.

    Retorno:
    - None
    """
    try:
        if not inventario:
            raise ValueError("⚠️ ¡El inventario está vacío!")
        for producto in inventario:
            if producto.nombre != producto_eliminar:
                raise ValueError(f"⚠️ Producto '{producto_eliminar}' no encontrado en el inventario.")
    
    except Exception as e:
        print(f"ERROR. {e}")
    
    else:
        for producto in inventario:
            if producto.nombre == producto_eliminar:
                inventario.remove(producto)
                print(f"\n✅ ¡Producto '{producto_eliminar}' eliminado del inventario!")
            else:
                print(f"\n❌ Producto '{producto_eliminar}' no encontrado en el inventario.")