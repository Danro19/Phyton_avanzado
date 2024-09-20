
from modelo.modelo import insertar, consultar
from interfaz.menu import menu
from persistencia.persistencia import cargar


# PROGRAMA PRINCIPAL
libreria = {}
archivo ="revisiondeerror/libreria/utils/libreria1.json"
libreria=cargar(archivo) 

print(libreria)

while True:            
    op = menu()
    match op:
        case 1:
            libreria = insertar(libreria, archivo)
            
        case 2:
            consultar(libreria)
        case 3:
            print("\nGracias por usar el sofware.\n")
            break    

