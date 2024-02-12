id = 1
usuario = {'id': '','name': '','lastname': '','phone': '','email': '' }
opciones = {
    1: "Ingresar usuarios",
    2: "Ver usuarios registrados",
    3: "Editar usuario",
    4: "Buscar Usuario",
    5: "Eliminar Usuario",
    6: "Salir del programa",
}

usuarios_creados = {0:{'id':'0', 'name':'Jeff', 'lastname':'Rios', 'phone':'1234567890', 'email':'jeff@email.com'}}
salir = False

#LISTA DE ACCIONES
def new_user(id, usuarios_creados_dic):           
    usuario = {'id': '','name': '','lastname': '','phone': '','email': '' }
    usuario['id'] = id
    #Ingreso nombre
    #no saldrá del bucle hasta que ingrese los caracteres solicitados
    first_name = input("Ingrese su nombre: ")
    if len(first_name) >= 5 and len(first_name) < 50 : 
        usuario['name']=first_name
    else:   
        while len(first_name) < 5 or len(first_name) > 50:
            first_name = input("Ingrese un nombre valido (min 5 - max 50 caracteres): ")
            if len(first_name) > 5 and len(first_name) < 50: 
                usuario['name']=first_name
    #Ingreso de apellidos    
    last_name = input("Ingrese su apellido: ")
    if len(last_name) >= 5 and len(last_name) < 50:
        usuario['lastname']=last_name     
    else:   
        while len(last_name) < 5 or len(last_name) > 50:
            last_name = input("Ingrese un apellido valido (min 5 - max 50 caracteres): ") 
            if len(last_name) >= 5 and len(last_name) < 50:
                usuario['lastname']=last_name
    #Ingreso de telefonos    
    telefono = input("Ingrese su número de telefono: ")
    if len(telefono) == 10:  
        usuario['phone']=telefono
    else:    
        while len(telefono) != 10:
            telefono = input("Ingrese un telefono valido (10 dígitos): ")
            if len(telefono) == 10:  
                usuario['phone']=telefono
    # Ingreso de correos   
    email = input("Ingrese su correo electrónico: ")
    if len(email) >= 5 or len(email) < 50:
        usuario['email']=email
    else:   
        while len(email) < 5 or len(email) > 50:
            email = input("Ingrese un correo valido (min 5 - max 50 caracteres): ")
            if len(email) >= 5 or len(email) < 50:
                usuario['email']=email
                
    usuarios_creados_dic[id] = usuario
    print("Se ha creado el siguiente usuario: \n")
    list_user(id)
    id += 1   
    
    
    return id
 
#Muestra a todos los usuarios        
def list_all_users():
    for val in usuario.keys():
        print(str(val).upper(), end="     \t")
    print("")
    
    if len(usuarios_creados) == 0:
        print("No existen usuarios registrados\n")
        return
    
    for i, *_ in tuple(usuarios_creados.items()):
        for value in list(usuarios_creados[i].values()):
            print(value, end="     \t")
        print()
    
    print("\n")
 
#Muestra un usuario si existe su ID
def list_user(id):
    if  id not in usuarios_creados:
        print("\nNo se ha encontrado el usuario\n")
        return False
    
    for val in usuario.keys():
        print(str(val).upper(), end="     \t")
    print("")  
    for value in list(usuarios_creados[id].values()):
        print(value, end="     \t")
    print("")           

#Editar un usuario
def edit_user(editar_id, usuarios_creados):
    usuario = {'id': '','name': '','lastname': '','phone': '','email': '' }
    if editar_id >= len(usuarios_creados):
        print("\nEl usuario no se ha encontrado\n")
        return
    
    list_user(editar_id)
    usuario['id'] = editar_id
    
    first_name = input("Ingrese el nombre: ")
    if len(first_name) >= 5 and len(first_name) < 50 : 
        usuario['name']=first_name
    else:   
        while len(first_name) < 5 or len(first_name) > 50:
            first_name = input("Ingrese un nombre valido (min 5 - max 50 caracteres): ")
            if len(first_name) > 5 and len(first_name) < 50: 
                usuario['name']=first_name
    #Ingreso de apellidos    
    last_name = input("Ingrese el apellido: ")
    if len(last_name) >= 5 and len(last_name) < 50:
        usuario['lastname']=last_name     
    else:   
        while len(last_name) < 5 or len(last_name) > 50:
            last_name = input("Ingrese un apellido valido (min 5 - max 50 caracteres): ") 
            if len(last_name) >= 5 and len(last_name) < 50:
                usuario['lastname']=last_name
    #Ingreso de telefonos    
    telefono = input("Ingrese el número de telefono: ")
    if len(telefono) == 10:  
        usuario['phone']=telefono
    else:    
        while len(telefono) != 10:
            telefono = input("Ingrese un telefono valido (10 dígitos): ")
            if len(telefono) == 10:  
                usuario['phone']=telefono
    # Ingreso de correos   
    email = input("Ingrese el correo electrónico: ")
    if len(email) >= 5 or len(email) < 50:
        usuario['email']=email
    else:   
        while len(email) < 5 or len(email) > 50:
            email = input("Ingrese un correo valido (min 5 - max 50 caracteres): ")
            if len(email) >= 5 or len(email) < 50:
                usuario['email']=email
                
    usuarios_creados[editar_id] = usuario
    print("El usuario se ha editado con exito\n")
    list_user(editar_id)
 
#Elimina el usuario si existe un ID   
def delete_user(id):
    if id not in usuarios_creados: #Verifica si el usuario
        print("\nEl usuario no se ha encontrado\n")
        return #retorna a las funciones principales
    confirm = input("\n¿Desea eliminar el usuario? Si (yes/y)     No (Enter): ")   
    
    #Si el usuario elige 'y' se elimina el usuario
    if 'y' in confirm:
        usuarios_creados.pop(id)
        print("\nSe ha borrado el usuario\n")

#Valida las entradas del usuario
def validar_input(mensaje):
    while True:
        try:
            entrada_usuario = int(input(mensaje + ": "))
            break 
        except ValueError:
            print("Ingresa solo números")
    return entrada_usuario
def validar_input_error(mensaje, error):
    while True:
        try:
            entrada_usuario = int(input(mensaje + ": "))
            break 
        except ValueError:
            print(error)
    return entrada_usuario

while not salir:
    print("\n--------- REGISTRO DE USUARIOS ---------\n")
    
    #Imprimir opciones en pantalla
    for i, op in list(opciones.items()):
        print("\t" + str(i) + ". " + op)
    print()
    
    #Verificar la opcion ingresada del usuario
    opcion = validar_input("Ingrese la opción deseada")
    while (opcion > 6 or opcion <= 0): #Se repite hasta que escoja una opción válida
        opcion = validar_input("Ingrese la opción deseada")
        if opcion > 6 or opcion <= 0:
            print("¡Ingresa una opción válida!")
        
    match opcion:
        case 1:
            print("\n------- Ingreso de usuarios -------\n")
            n = validar_input("Ingrese el número de usuarios a registrar")
            
            if n <= 0:
                continue
                
            for i in range(0, n): 
                print(f"Ingrese el {i+1}° usuario de {n}: ")
                new_user(id, usuarios_creados)
                print()
                id += 1
                        
        case 2:
            print("\n------- Ver Usuarios Registrados -------\n")
            list_all_users()
            input("Presione cualquier tecla para continuar...")
                
        case 3:
            print("\n------- Editar un usuario -------\n")
            editar_id = validar_input_error("Ingrese el ID del usuario que va a editar","El valor del ID debe ser numérico")           
            edit_user(editar_id, usuarios_creados)        
            input("Pulse cualquier tecla para continuar...")
             
        case 4:
            print("------- Busqueda de Usuario -------")
            edit_id = validar_input_error("Ingrese el ID del usuario que busca", "El valor del ID debe ser numérico")  
            if edit_id not in usuarios_creados:
                print("\nNo se ha encontrado el usuario con ese ID")
                continue
            
            list_user(edit_id)
            input("Presione cualquier tecla para continuar...")
            
        case 5:
            print("------- Eliminar usuario -------")
            delete_id = validar_input_error("Ingrese el ID del usuario que desea eliminar", "El valor del ID debe ser numérico")       
            list_user(delete_id)
            delete_user(delete_id)
                
            input("Pulse cualquier tecla para continuar...")
            
        case 6:
            input("Presione cualquier tecla para continuar...")
            salir = True
            