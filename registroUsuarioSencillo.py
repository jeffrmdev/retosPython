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

print("Hola")

usuarios_creados = [['0', 'Jeff', 'Rios', '1234567890', 'jeff@email.com']]
salir = False

while not salir:

    print("\n--------- REGISTRO DE USUARIOS ---------\n")
    
    print("Opciones disponibles \n\n\
    1. Ingresar usuarios        \n\
    2. Ver usuarios registrados \n\
    3. Editar un usuario        \n\
    4. Buscar usuario           \n\
    5. Salir                    \n")
    
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
            
            while True:
                try: 
                    n = int((input("Ingrese cuantos usuarios quiere registrar: ")))
                    break
                except ValueError:
                    print("Ingresa solo numeros")
                
                
            for i in range(1, n+1):  
                
                usuario = {'id': '','name': '','lastname': '','phone': '','email': '' }
                usuario['id'] = id
    
                #Imprimir el numero de usuario en pantall, solo si es mayor a uno
                print(f"\nIngrese los datos de el {i}° usuario\n")
    
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
                  
        case 2:
            print("\n------- Ver Usuarios Registrados -------\n")
            for val in usuario.keys():
                print(str(val).upper(), end="     \t")
            print("")
            
            for i in range(0,len(usuarios_creados)):   
                for value in usuarios_creados[i]:
                    print(value, end="     \t")
                print("")
                    
            print("\n")
            input("Presione cualquier tecla para continuar...")
                
        case 3:
            print("\n------- Editar un usuario -------\n")
            usuario = {'id': '','name': '','lastname': '','phone': '','email': '' }
            while True:
                try: 
                    editar_id = int(input("Ingrese el ID del usuario que va a editar: "))
                    break

                except ValueError:
                    print("El valor ID debe ser numerico")
                    editar_id = int(input("Ingrese el ID del usuario que va a editar: "))
            if editar_id > len(usuarios_creados):
                print("El usuario no se ha encontrado")
                input("Pulse cualquier tecla para continuar...")
                continue
            
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
            