from heap import HeapMax

# Crear la cola de prioridad para impresión
cola_impresion = HeapMax()


print("SISTEMA DE COLA DE IMPRESIÓN CON PRIORIDADES")
print("\n")



print("\n")
print("a) Cargue 3 documentos de empleados:")
cola_impresion.arrive("reporte_ventas", 1)
cola_impresion.arrive("facturas", 1)
cola_impresion.arrive("solicitudes", 1)
print("reporte_ventas (prioridad 1)")
print("facturas (prioridad 1)")
print("solicitudes (prioridad 1)")



print("\n")
print("b) Imprimir el primer documento de la cola:")
documento = cola_impresion.attention()
print(f"{documento[1]} (prioridad {documento[0]})")


print("\n")
print("c) Cargue 2 documentos del staff de TI:")
cola_impresion.arrive("reporte_servidores", 2)
cola_impresion.arrive("backup", 2)
print("reporte_servidores (prioridad 2)")
print("backup (prioridad 2)")


print("\n")
print("d) Cargue 1 documento del gerente:")
cola_impresion.arrive("estrategia", 3)
print("estrategia (prioridad 3)")


print("\n")
print("e) Imprimir los 2 primeros documentos de la cola:")
documento1 = cola_impresion.attention()
print(f"{documento1[1]} (prioridad {documento1[0]})")
documento2 = cola_impresion.attention()
print(f"{documento2[1]} (prioridad {documento2[0]})")


print("\n")
print("f) Cargue 2 documentos de empleados y 1 de gerente:")
cola_impresion.arrive("nominas", 1)
cola_impresion.arrive("contratos", 1)
cola_impresion.arrive("presupuesto", 3)
print("nominas (prioridad 1)")
print("contratos (prioridad 1)")
print("presupuesto (prioridad 3)")


print("\n")
print("g) Imprimir todos los documentos restantes de la cola:")
while cola_impresion.size() > 0:
    documento = cola_impresion.attention()
    print(f"{documento[1]} (prioridad {documento[0]})")
    

