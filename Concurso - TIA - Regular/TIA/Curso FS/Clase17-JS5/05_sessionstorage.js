//---------------------------------------------------------
// SessionStorage
//---------------------------------------------------------

//---------------------------------------------------------
// Funcion que guarda valores en el dispositivo del usuario:
//---------------------------------------------------------
function guardar(color,fondo ){
    // ¿El navegador soporta esta función?
    if (typeof(Storage) !== "undefined") {
        // setItem guarda datos en el dispositivo
        sessionStorage.setItem("color", color)
        sessionStorage.setItem("fondo", fondo)
        imprimir("<hr>", false)
        imprimir("Datos guardados:")
        imprimir("Color texto: "+ color)
        imprimir("Color fondo: "+ fondo)
    } else {
        imprimir("Web Storage no soportado.")
    }
}

//---------------------------------------------------------
// Funcion que recupera valores del dispositivo del usuario:
//---------------------------------------------------------
function recuperar(){
    if (typeof(Storage) !== "undefined") {
        // getItem recupera datos del dispositivo
        color = sessionStorage.getItem("color")
        fondo = sessionStorage.getItem("fondo")
        imprimir("<hr>", false)
        imprimir("Datos recuperados:")
        imprimir("Color texto: "+ color)
        imprimir("Color fondo: "+ fondo)
     } else {
        imprimir("Web Storage no soportado.")
     }     
}

//---------------------------------------------------------
// Cuerpo principal del programa:
//---------------------------------------------------------

//guardar("Negro", "Blanco" ) 
recuperar()
imprimir("<hr>", false)
//---------------------------------------------------------
// Despues de ejecutar el script, puedes comentar la linea
// que invoca a la función guardar(), cerrar el navegador
// y volver a cargar el ejemplo. Los valores guardados en
// la sesión anterior NO estan disponibles luego de cerrar
// la sesion.
//
// ¿Que pasa si intento recuperar datos que no he guardado?
//---------------------------------------------------------