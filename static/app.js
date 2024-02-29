let listaPersonas=[]
let mensajeValidarDatos=''
let idAnterior=null
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
        datos += "<tr clas>"
        datos += "<td>" + persona['identificacion'] + "</td>" 
        datos += "<td>" + persona['nombre'] + "</td>" 
        datos += "<td>" + persona['apellido'] + "</td>" 
        datos += "<td>" + persona['correo'] + "</td>" 
        datos += "</tr>"



        
    });

    datosPersonas.innerHTML=datos
}

////////////////////////////////////////////////////////////////

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
                "content-Type":"application/json",
            }
        }
        )
        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            console.log(resultado);
            if(resultado.estado){
                Formulario.reset()
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

////////////////////////////////////////////////////////////////

function consultar(){
    if (pullId.value!=''){

        fetch("/consultarPersona/"+ pullId.value,  
        {method:'GET', headers:{"content-Type":"applications/json"}})

        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            console.log(resultado);
            if(resultado.estado){
                pullNombre.value=resultado.persona.nombre
                pullApellidos.value=resultado.persona.apellido
                pullCorreo.value=resultado.persona.correo
                idAnterior.value=pullId.value
            }else{
                Swal.fire("Consultar persona",resultado.mensaje,"warning")
            }
        })
        .catch(error=>console.log(error))
    }

}


function actualizar(){
    if (validarDatos()){
        const persona={
            // a las variables se le asigna el id de los inputs

            "identificacion":pullId.value,
            "nombre":pullNombre.value,
            "apellido":pullApellidos.value,
            "correo":pullCorreo.value
        }
        const datos={
            'persona':persona,
            'id':idAnterior
        }
        
        fetch("/actualizar",{
            method:"PUT",
            body:JSON.stringify(persona),
            headers:{
                "content-Type":"application/json",
            }
        })

        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            console.log(resultado);
            if(resultado.estado){
                personas=resultado.personas
                mostrarDatosTabla()
                Swal.fire("Actualizar persona",resultado.mensaje,"success")
            }else{
                Swal.fire("Actualizar persona",resultado.mensaje,"warning")
            }
        })
        .catch(error=>console.log(error))


    }else{
        Swal.fire("Consultar persona",resultado.mensaje,"warning")
    }
}

////////////////////////////////////////////////////////////////

function eliminar(){
    if (pullId.value!='')

    Swal.fire({
        title: "Estas seguro de eliminar",
        showDenyButton: true,
        confirmButtonText: "Si",
        denyButtonText: `No`
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire("Eliminado correctamente!", "", "success");
          formulario.reset()
        } else if (result.isDenied) {
          Swal.fire("No se pudo eliminar", "", "info");
        }
    });


    fetch("/eliminar/"+pullId.value,
    {
        method:"DELETE",
        body:JSON.stringify(persona),
        headers:{
            "content-Type":"application/json",
        }
    })

    .then(respuesta=>respuesta.json())
    .then(resultado=>{
        console.log(resultado);
        if(resultado.estado){
            personas=resultado.personas
            mostrarDatosTabla()
            formulario.reset()
            Swal.fire("Eliminar persona",resultado.mensaje,"success")
        }else{
            Swal.fire("Eliminar persona",resultado.mensaje,"warning")
        }
    })
    .catch(error=>console.log(error))
}
