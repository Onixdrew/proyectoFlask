# from flask import Flask,render_template,request

# app= Flask(__name__)

# listaPersonas=[]

# @app.route("/")
# def inicio():
#     return render_template("index.html")

# def existeId(id)->bool:
#     for p in listaPersonas:
#         if p['identificacion']==id:
#             return True
#     return False

# def existeCorreo(correo)->bool:
#     for p in listaPersonas:
#         if p['correo']==correo:
#             return True
#     return False


# @app.route("/operaciones", methods=['POST'])
# def operaciones():
#     option=request.form['btnOption']
#     mensaje=''
#     bandera=None
#     persona=None
    
#     match (option):
#         case 'agregar':
#         # persona=[
#         #         request.form['pullNombre'],
#         #          request.form['pullApellidos'],
#         #          request.form['pullCorreo']
#         #         ]
        
#             identificacion=request.form['pullId']
#             correo=request.form['pullCorreo']
#             persona={
#                 "identificacion":identificacion,
#                 "Nombre":request.form['pullNombre'],
#                 "apellido":request.form['pullApellidos'],
#                 "correo":correo  
#             }
            
#             existe=existeId(identificacion)
#             if not existe:
#                 listaPersonas.append(persona)
#                 mensaje='agregada satisfactoriamente'
                
#             else:
#                 mensaje='¡Esta persona ya existe!'
#                 persona=persona    

#         case 'consultar':
            
#             identificacion=request.form['pullId']
#             correo=request.form['pullCorreo']
#             # persona={
#             #     "identificacion":identificacion,
#             #     "Nombre":request.form['pullNombre'],
#             #     "apellido":request.form['pullApellidos'],
#             #     "correo":correo
#             # }
                
#             existe=existeId(identificacion)
            
#             if existe:
#                 for resultado in listaPersonas:
#                     if resultado['identificacion']==identificacion:
#                         persona=resultado
                
#                 mensaje='Persona encontrada'
#             else:
#                 mensaje='No encontrada con ese ID'
        
#         case 'actualizar':  
#             idAnterior= request.form['idAnterior']
#             identificacion=request.form['pullId']
#             correo=request.form['pullCorreo']
#             persona={
#                 "identificacion":identificacion,
#                 "Nombre":request.form['pullNombre'],
#                 "apellido":request.form['pullApellidos'],
#                 "correo":correo  
#             }
#             pos=0
#             for p in listaPersonas:
#                 if p['identificacion']==idAnterior:
#                     listaPersonas[pos]=persona
#                     mensaje="persona actualizada"
#                     break
#                 pos +=1
        
#         # case 'eliminar':
#         #     identificacion=request.form['pullId']
#         #     existe=existeId(identificacion)
#         #     if existe:
#         #         for resultado in listaPersonas:
#         #             if resultado['identificacion']==identificacion:
#         #                 persona=resultado
#         #                 bandera='eliminar'
                        
#         #         mensaje='Persona eliminada'
#         #     else:
#         #         mensaje='No encontrada'
    

#     return render_template ( "index.html",persona=persona, bandera=bandera, personas=listaPersonas, mensaje=mensaje)





# # esta condicion siempre va al final
# if __name__=='__main__':
#     app.run(port=3000, debug=True)
    

# # @app.route("/saludo/<nombre>")
# # def saludo(nombre):
# #     return f'hola {nombre}'