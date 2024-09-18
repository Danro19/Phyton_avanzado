#citas variables las horas (Se escriben como str la lista)
#añadir con append, 16:30

#existe una lista de citas 
lstcitas=["9:00", "10:30", "14:00", "15:00", "15:30"]
#se agrega con el metodo append un nuevo dato
lstcitas.append("16:30")#se agrega una nueva cita
#imprimimos para poder rectificar que todo salio bien
print(lstcitas)


#agregaremos usando el operador "+"
agregar= "16:30"#opcional
#creo la variable "agregar" para poder hacer la suma 
nlstcitas= lstcitas + [agregar]#creo una nueva lista para comparar y sumar la variable 
#imprimo para rectificar que todo salio bien
print(lstcitas)
print(nlstcitas)

#LA INCOGNITA SE BASA EN PODER SABER CON CUAL SE AGREGA UN DATO A LA LISTA Y CON CUAL METODO SE CREA UNA LISTA
#Con + se crea una lista, con .append se modifica