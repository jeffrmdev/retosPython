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


usuarios_creados = [['0', 'Jeff', 'Rios', '1234567890', 'jeff@email.com']]
salir = False

#LISTA DE ACCIONES
def new_user(id):           
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
                
    usuarios_creados.append(usuario.values())
    id += 1 
          
    print("Se ha creado el siguiente usuario: \n")
    for val in usuario.keys():
        print(str(val).upper(), end="     \t")
    print("")  
    for value in usuarios_creados[-1]:
        print(value, end="     \t")
    print("")
    return id
        
def list_user():
    for val in usuario.keys():
        print(str(val).upper(), end="     \t")
    print("")
    
    for i in range(0,len(usuarios_creados)):   
        for value in usuarios_creados[i]:
            print(value, end="     \t")
        print("")
    print("\n")
            
def edit_user(editar_id):
    usuario = {'id': '','name': '','lastname': '','phone': '','email': '' }
    if editar_id >= len(usuarios_creados):
        print("El usuario no se ha encontrado")
        return
    
    for val in usuario.keys():
        print(str(val).upper(), end="     \t")
    print("")
    for value in usuarios_creados[editar_id]:
        print(value, end="     \t")
    print("\n")
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
    usuarios_creados[editar_id] = usuario.values()
    print("El usuario se ha editado con exito\n")
    for val in usuario.keys():
        print(str(val).upper(), end="     \t")
    print("")
    for value in usuarios_creados[editar_id]:
        print(value, end="     \t")
    print("\n")


while not salir:

    print("\n--------- REGISTRO DE USUARIOS ---------\n")
    
    for i, op in list(opciones.items()):
        print("\t" + str(i) + ". " + op)
    print()
    
    #Verificar la opcion ingresada del usuario
    while True:
        try:
            opcion = int(input("Ingrese la opción deseada: "))
            while (opcion > 5 or opcion <= 0):
                print("Ingrese una opción valida")
                opcion = int(input("Ingrese la opción deseada: "))  
            break   
        except ValueError:
            print("¡Solo se permite ingresar números!")
        
    match opcion:
        case 1:
            print("\n------- Ingreso de usuarios -------\n")
            
            while True:
                try:
                    n = int(input("Ingresa cuantos usuarios quieres registrar: "))
                    break 
                except ValueError:
                    print("Ingresa solo números")
            
            if n <= 0:
                continue
                
            for i in range(0, n): 
                print(f"Ingrese el {i+1}° usuario de {n}: ")
                new_user(id)
                print()
                id += 1
            
                         
        case 2:
            print("\n------- Ver Usuarios Registrados -------\n")
            list_user()
            input("Presione cualquier tecla para continuar...")
                
        case 3:
            print("\n------- Editar un usuario -------\n")
            while True:
                try: 
                    editar_id = int(input("Ingrese el ID del usuario que va a editar: "))
                    break
                except ValueError:
                    print("El valor ID debe ser numerico")
                    editar_id = int(input("Ingrese el ID del usuario que va a editar: "))       
            edit_user(editar_id)        
            input("Pulse cualquier tecla para continuar...")
             
        case 4:
            print("------- Busqueda de Usuario -------")
            while True:
                try:
                    editar_id = int(input("Ingrese el ID del usuario que busca: "))
                    break
                except ValueError:
                    print("El valor del ID debe ser numérico: ")
                    editar_id = int(input("Ingrese el ID del usuario que busca: "))
                
            if editar_id >= len(usuarios_creados):
                print("\nNo se ha encontrado el usuario con ese ID")
                break
            
            print("")
            for val in usuario.keys():
                print(str(val).upper(), end="     \t")
            print("")
            for value in usuarios_creados[editar_id]:
                    print(value, end="     \t")
            print("\n")
            input("Presione cualquier tecla para continuar...")
            
        case 5:
            if(opcion == 5):
                salir = True
            