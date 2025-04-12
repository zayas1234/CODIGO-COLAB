
#para una tienda que tiene una gran cantidad de productos 
# que tiene una problemática necesita : gestionar eficientemente 
# productos con diferentes cantidades y precios . 

#ordenar_por_novedad(): Usa Quick Sort para priorizar productos más nuevos (con fecha de vencimiento más lejana).

#etiquetar_por_precio_calidad(): Devuelve diccionario con productos ordenados por precio, calidad y mejor valor (calidad/precio) usando Insertion Sort.

#ordenar_por_mas_vendidos(): Ordena productos por unidades vendidas usando Bubble Sort.

#mostrar_inventario(): Muestra la cantidad disponible de cada producto.




import datetime
from typing import List, Dict, Tuple

class Producto:
    def __init__(self, id_unico: int, nombre: str, precio: float, puntuacion: float, 
                 fecha_vencimiento: str, cantidad: int, vendidos: int = 0):
        self.id = id_unico
        self.nombre = nombre
        self.precio = precio
        self.puntuacion = puntuacion
        self.fecha_vencimiento = datetime.datetime.strptime(fecha_vencimiento, "%Y-%m-%d").date()
        self.cantidad = cantidad
        self.vendidos = vendidos
    
    def __repr__(self):
        return (f"Producto(ID={self.id}, Nombre='{self.nombre}', Precio={self.precio}, "
                f"Puntuación={self.puntuacion}, Vence={self.fecha_vencimiento}, "
                f"Existencia={self.cantidad}, Vendidos={self.vendidos})")

class SistemaGestionProductos:
    def __init__(self):
        self.productos: List[Producto] = []
    
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
    
    def ordenar_por_novedad(self) -> List[Producto]:
        """Prioriza productos más nuevos (por fecha de vencimiento más lejana)"""
        # Usamos Quick Sort para ordenar por novedad
        return self._quick_sort(self.productos.copy(), key=lambda x: x.fecha_vencimiento, reverse=True)
    
    def etiquetar_por_precio_calidad(self) -> Dict[str, List[Producto]]:
        """Etiqueta productos por precio y calidad (puntuación)"""
        # Usamos Insertion Sort para ordenar por precio y calidad
        por_precio = self._insertion_sort(self.productos.copy(), key=lambda x: x.precio)
        por_calidad = self._insertion_sort(self.productos.copy(), key=lambda x: x.puntuacion, reverse=True)
        
        return {
            "por_precio": por_precio,
            "por_calidad": por_calidad,
            "mejor_valor": self._insertion_sort(
                self.productos.copy(), 
                key=lambda x: x.puntuacion / x.precio if x.precio > 0 else 0, 
                reverse=True
            )
        }
    
    def ordenar_por_mas_vendidos(self) -> List[Producto]:
        """Ordena productos de más vendidos a menos vendidos"""
        # Usamos Bubble Sort para ordenar por vendidos
        return self._bubble_sort(self.productos.copy(), key=lambda x: x.vendidos, reverse=True)
    
    def mostrar_inventario(self) -> List[Tuple[str, int]]:
        """Muestra la cantidad en existencia de cada producto"""
        return [(p.nombre, p.cantidad) for p in self.productos]
    
    # Algoritmos de ordenamiento
    def _quick_sort(self, arr: List[Producto], key=None, reverse=False) -> List[Producto]:
        """Implementación de Quick Sort"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if (key(x) < key(pivot) if not reverse else key(x) > key(pivot))]
        middle = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if (key(x) > key(pivot) if not reverse else key(x) < key(pivot))]
        
        return self._quick_sort(left, key, reverse) + middle + self._quick_sort(right, key, reverse)
    
    def _insertion_sort(self, arr: List[Producto], key=None, reverse=False) -> List[Producto]:
        """Implementación de Insertion Sort"""
        for i in range(1, len(arr)):
            current = arr[i]
            j = i - 1
            
            if not reverse:
                while j >= 0 and key(arr[j]) > key(current):
                    arr[j + 1] = arr[j]
                    j -= 1
            else:
                while j >= 0 and key(arr[j]) < key(current):
                    arr[j + 1] = arr[j]
                    j -= 1
            
            arr[j + 1] = current
        return arr
    
    def _bubble_sort(self, arr: List[Producto], key=None, reverse=False) -> List[Producto]:
        """Implementación de Bubble Sort"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                condition = (key(arr[j]) < key(arr[j+1])) if reverse else (key(arr[j]) > key(arr[j+1]))
                if condition:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

if __name__ == "__main__":
    sistema = SistemaGestionProductos()
    

    sistema.agregar_producto(Producto(1, "Leche", 2.50, 4.5, "2023-12-31", 100, 150))
    sistema.agregar_producto(Producto(2, "Pan", 1.20, 4.2, "2023-11-15", 50, 200))
    sistema.agregar_producto(Producto(3, "Queso", 5.75, 4.8, "2024-01-20", 30, 75))
    sistema.agregar_producto(Producto(4, "Jamon", 7.40, 4.3, "2023-12-15", 40, 120))
    sistema.agregar_producto(Producto(5, "Huevos", 3.20, 4.7, "2023-11-30", 60, 180))
    
    print("\n--- Productos ordenados por novedad (fecha vencimiento más lejana primero) ---")
    for p in sistema.ordenar_por_novedad():
        print(p)
    
    print("\n--- Productos etiquetados por precio y calidad ---")
    etiquetas = sistema.etiquetar_por_precio_calidad()
    print("\nMás baratos:")
    for p in etiquetas["por_precio"][:3]:
        print(f"{p.nombre} - ${p.precio}")
    
    print("\nMejor calidad:")
    for p in etiquetas["por_calidad"][:3]:
        print(f"{p.nombre} - ⭐{p.puntuacion}")
    
    print("\nMejor valor (calidad/precio):")
    for p in etiquetas["mejor_valor"][:3]:
        print(f"{p.nombre} - ⭐{p.puntuacion} - ${p.precio}")
    
    print("\n--- Productos ordenados por más vendidos ---")
    for p in sistema.ordenar_por_mas_vendidos():
        print(f"{p.nombre} - Vendidos: {p.vendidos}")
    
    print("\n--- Cantidad en existencia ---")
    for nombre, cantidad in sistema.mostrar_inventario():
        print(f"{nombre}: {cantidad} unidades")