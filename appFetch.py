from flask import Flask,render_template,request,jsonify

app= Flask(__name__)

listaPersonas=[]

@app.route("/")
def inicio():
    return render_template("index2.html",persona=listaPersonas)


#//////////////////// usando api fetch ///////////////////////

@app.route('/agregar', methods=['POST'])
def agregarPersona():
    estado=False
    mensaje=None
    try:
        datos=request.json
        identificacion=datos.get('pullId')
        correo=datos.get('pullCorreo')
        
        # validar si ya existe
        for p in listaPersonas:
            if(p['identificacion']==identificacion or p['correo']==correo):
                mensaje="Persona ya existe con identificacion o correo"
                break
        else:
            listaPersonas.append(datos)
            mensaje='persona agregada correctamente'
            estado=True
    except Exception as error:
        mensaje= error
        
    return jsonify({"estado":estado , "mensaje":mensaje, "personas":listaPersonas})
#////////////////////////////////////////////////////////////////////

@app.route("/consultarPersona/<identificacion>", methods=['GET'])
def consultarPersona(identificacion):
    estado=False
    persona=None
    mensaje=None
    try:
        for p in listaPersonas:
            if p['identificacion']==identificacion:
                persona=p
                estado=True
                break
        else:
            mensaje='Persona con esa identificacion no existe'
    except Exception as error:
        mensaje=error
        
    return jsonify({'estado':estado,'persona':persona,'mensaje':mensaje})


#////////////////////////////////////////////////////////////////////
        
@app.route('/actualizar', methods=['PUT'])
def actualizarPersona():
    estado=False
    mensaje=None

    try:
        datos=request.json
        persona=datos.get('persona')
        id=datos.get('id')
        #validar si ya existe
        pos=0
        for p in listaPersonas:
            
            if ((p['identificacion']==persona['identificacion'] or p['correo']==persona['correo'])
                and (p["identificacion"]!=id)):
                listaPersonas[pos]=persona
                mensaje="Persona ya existe. verifique la identificación"
                break
        else: 
            pos=0
            for p in listaPersonas:
                listaPersonas[pos]=persona
                estado=True
                mensaje='Persona actualizada correctamente'
            pos +=1
    except Exception as error:
        mensaje= error
        
    return jsonify({"estado":estado , "mensaje":mensaje, "personas":listaPersonas})

#////////////////////////////////////////////////////////////////////

@app.route("/eliminar/<identificacion>", methods=["DELETE"])
def eliminarPersona(identificacion):
    estado=False
    mensaje=None
    try:
        for p in listaPersonas:
            if p['identificacion']==identificacion:
                listaPersonas.remove(p)
                estado=True
                mensaje='Persona eliminada correctamente'
                break
        else:
            mensaje=f'No existe persona con esa identificacion\ {identificacion} para eliminar'
    except Exception as error:
        mensaje=error
        
    return jsonify({'estado':estado,'persona':listaPersonas,'mensaje':mensaje})

if __name__=='__main__':
    app.run(port=3000, debug=True)