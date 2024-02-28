listaPersonas=[]
let mensajeValidarDatos=''

function validarDatos(){
    // a las variables se le asigna el id de los inputs
    let identificacion=pullId
    let nombre=pullNombre
    let apellido=pullApellidos
    let correo=pullCorreo
    
    if (identificacion.value==''){
        mensajeValidarDatos='Debe ingresar la identificacion'
        return false
    }else if(nombre.value==''){
        mensajeValidarDatos='Debe ingresar el nombre o los nombres'
        return false
    }else if(apellido.value==''){
        mensajeValidarDatos='Debe ingresar el apellido'
        return false
    }else if(correo.value==''){
        mensajeValidarDatos='Debe ingresar el correo electronico'
        return false
    }else{
        return true
    }
    
}


function mostrarDatosTabla(){
    let datos=''
    listaPersonas.forEach(persona => {
        datos += "<tr>"
        datos += "<td>" + persona['identificacion'] + "</td>" 
        datos += "<td>" + persona['nombre'] + "</td>" 
        datos += "<td>" + persona['apellido'] + "</td>" 
        datos += "<td>" + persona['correo'] + "<7td>" 
        datos += "</tr>"



        
    });

    document.getElementById('datosPersonas').innerHTML=datos
}



// peticion al servidor tipo post

function agregar(){
    if(validarDatos()){
        const persona={
            // a las variables se le asigna el id de los inputs


            "identificacion":pullId.value,
            "nombre":pullNombre.value,
            "apellido":pullApellidos.value,
            "correo":pullCorreo.value
        }
        fetch("/agregar",{
            method:"POST",
            body:JSON.stringify(persona),
            headers:{
                "content-Type":"applications/json"
            }
        }
        )
        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            console.log(resultado);
            if(resultado.estado){
                limpiar()
                Swal.fire("registro persona",resultado.mensaje,"success")
                listaPersonas=resultado.personas
                mostrarDatosTabla()
            }else{
                Swal.fire("registro persona",resultado.mensaje,"warning")
            }
        })
        .catch(error=>console.log(error))
    
    }else{
        Swal.fire("registro persona",mensajeValidarDatos,"warning")
    }
}