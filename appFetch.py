from flask import Flask,render_template,request,jsonify

app= Flask(__name__)

listaPersonas=[]

@app.route("/")
def inicio():
    return render_template("index.html")


#//////////////// usando api fetch ///////////////////////

@app.route('/agregar', methods=['POST'])
def agregar():
    estado=False
    mensaje=None
    try:
        datos=request.json
        identificacion=datos.get('pullId')
        correo=datos.get('pullCorreo')
        
        for p in listaPersonas:
            if(p['identificacion']==identificacion or p['correo']==correo):
                mensaje="Persona ya existe con identificacion o correo"
                break
        else:
            persona={
                "identificacion":identificacion,
                "Nombre":datos.get['pullNombre'],
                "apellido":datos.get['pullApellidos'],
                "correo":correo  
            }
            listaPersonas.append(persona)
            mensaje='persona agregada correctamente'
            estado=True
    except Exception as error:
        mensaje= error
        
    return jsonify({"estado":estado , "mensaje":mensaje, "personas":listaPersonas})

        
        
        
        
        
        

if __name__=='__main__':
    app.run(port=3000, debug=True)