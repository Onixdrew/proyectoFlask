from flask import Flask,render_template,request

app= Flask(__name__)

listaPersonas=[]

@app.route("/")
def inicio():
    return render_template("index.html")



@app.route("/operaciones", methods=['POST'])
def operaciones():
    option=request.form['btnOption']
    mensaje=''
    producto=None
    
    match (option):
        case 'agregar':
        # persona=[
        #         request.form['pullNombre'],
        #          request.form['pullApellidos'],
        #          request.form['pullCorreo']
        #         ]
            persona={
                "identificacion":request.form['pullId'],
                "Nombre":request.form['pullNombre'],
                "apellido":request.form['pullApellidos'],
                "correo":request.form['pullCorreo']
                
            }
            listaPersonas.append(persona)
            mensaje='agregada satisfactoriamente'

        case 'consultar':
            pass
        
        case 'actualizar':
            pass
        
        case 'eliminar':
            pass
    
    return render_template ('index.html',personas=listaPersonas, mensaje=mensaje, producto=producto)

# esta condicion siempre va al final
if __name__=='__main__':
    app.run(port=3000, debug=True)
    

# @app.route("/saludo/<nombre>")
# def saludo(nombre):
#     return f'hola {nombre}'