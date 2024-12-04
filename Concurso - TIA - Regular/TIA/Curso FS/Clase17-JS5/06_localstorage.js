//---------------------------------------------------------
// LocalStorage
//---------------------------------------------------------

//---------------------------------------------------------
// Funcion que guarda valores en el dispositivo del usuario:
//---------------------------------------------------------
function guardar(ape,nom ){
    // ¿El navegador soporta esta función?
    if (typeof(Storage) !== "undefined") {
        // setItem guarda datos en el dispositivo
        localStorage.setItem("apellido", ape)
        localStorage.setItem("nombre", nom)
        imprimir("<hr>", false)
        imprimir("Datos guardados:")
        imprimir("Color texto: "+ ape)
        imprimir("Color fondo: "+ nom)
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
        ape = localStorage.getItem("apellido")
        nom = localStorage.getItem("nombre")
        imprimir("<hr>", false)
        imprimir("Datos recuperados:")
        imprimir("Color texto: "+ ape)
        imprimir("Color fondo: "+ nom)
     } else {
        imprimir("Web Storage no soportado.")
     }     
}

//---------------------------------------------------------
// Cuerpo principal del programa:
//---------------------------------------------------------
//guardar("Tesla", "Nicolas" ) 
recuperar()
imprimir("<hr>", false)
//---------------------------------------------------------
// Despues de ejecutar el script, puedes comentar la linea
// que invoca a la función guardar(), cerrar el navegador
// y volver a cargar el ejemplo. Los valores guardados en
// la sesión anterior seguirán estando disponibles.
//
// ¿Que pasa si intento recuperar datos que no he guardado?
//---------------------------------------------------------