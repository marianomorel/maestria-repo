// En este script vamos a analizar las
// principales propiedades de los objetos
// array.
// Excelente información sobre arrays en general aqui:
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array
//
// Mas info sobre como recorrer un array
// con un bucle aqui:
// https://www.delftstack.com/es/howto/javascript/javascript-loop-through-array
//----------------------------------------

// Creacion:
var colores  = ["Rojo", "Verde", "Azul"]
var beatles  = new Array ("John", "Paul", "George", "Ringo")
var vacio    = []
var mixto    = ["Lunes", 2, true]

//----------------------------------------
// Podemos mostrar directamente el contenido
// del array completo o elementos individuales:

// document.write("Array Colores: ",colores , "<br>")
// document.write("Array beatles: ",beatles , "<br>")
// document.write("Array vacio: "  ,vacio   , "<br>")
// document.write("Array mixto: "  ,mixto   , "<br>")
// document.write("<br>")
// document.write(colores[1] , "<br>")
// document.write(beatles[2] , "<br>")
// document.write(vacio[1]   , "<br>")
// document.write(mixto[0]   , "<br>")

//----------------------------------------
// La propiedad .length nos devuelve el
// número de elementos del array:

// document.write("Array Colores: ", colores.length , "<br>")
// document.write("Array beatles: ", beatles.length , "<br>")
// document.write("Array vacio: "  , vacio.length   , "<br>")
// document.write("Array mixto: "  , mixto.length   , "<br>")
// document.write("<br>")


//----------------------------------------
// La propiedad .length nos ayuda a recorrer
// un aray completo, elemento por elemento, con
// la ayuda de un bucle:

// document.write("<h3>Elementos del vector Colores:</h3> ")
// for(let i = 0; i < colores.length+1; i++ ){
//     document.write("Elemento ",i, " del vector Colores: ", colores[i], "<br>")
// }


//----------------------------------------
// Con push(elemento) añadimos uno o varios
// elementos al final del array.
// Devuelve tamaño del array:

// colores.push("Amarillo","Rosa", "Rojo")

// document.write(colores, "<br>")
// document.write("La longitud del nuevo arreglo es: ", largo, "<br>")


//----------------------------------------
// Con pop() se elimina y devuelve el
// último elemento del array:

// var color = colores.pop()
// document.write(colores, "<br>")
// document.write("El elemento que se eliminó es: ", color, "<br>")


//----------------------------------------
// Con .unshift(obj1) se añade uno o varios
// elementos al inicio del array.
//Devuelve tamaño del array:

// var largo = colores.unshift("Amarillo", "Blanco")
// document.write(colores, "<br>")
// document.write("La longitud del nuevo arreglo es: ", largo, "<br>")


//----------------------------------------
// Con shift() se elimina y devuelve el
// primer elemento del array:

// var color = colores.shift()
// document.write(colores, "<br>")
// document.write("El elemento que se eliminó es: ", color, "<br>")


//----------------------------------------
// Con concat() se concatenan los elementos
// (o elementos de los arrays) pasados por
// parámetro. Este método no cambia los arrays
// existentes, sino que devuelve uno nuevo:

// var nuevoArray = colores.concat(beatles)

// document.write("Colores.: ", colores, "<br>")
// document.write("Beatles.: ", beatles, "<br>")
// document.write("Union...: ", nuevoArray, "<br>")
// document.write("Sumo más: ", nuevoArray.concat("Mick", "Keith"), "<br>")

//----------------------------------------
// .indexOf(obj, from) devuelve la posición
// de la primera aparición de obj desde from,
// ó  -1 si el elemento no se encuentra:

//               0 1 2 3 4 5 6 7 8 9
// const numeros = [8,6,5,4,5,6,7,8,6,4]
// document.write( numeros.indexOf(4)  , "<br>")
// document.write( numeros.indexOf(4,5), "<br>")


//----------------------------------------
// .lastIndexOf(obj, from) devuelve la posición
// de la última aparición de obj desde from, ó
// -1 si el elemento no se encuentra.
// El arreglo es recorrido en sentido contrario,
// empezando por el índice from.
//               0 1 2 3 4 5 6 7 8 9
// const numeros = [8,6,5,4,5,6,7,8,6,4]
// document.write( numeros.lastIndexOf(4)  , "<br>")
// document.write( numeros.lastIndexOf(4,5), "<br>")
// document.write( numeros.lastIndexOf(1,5), "<br>")


//----------------------------------------
// .splice  agrega / elimina elementos a / de
// una matriz y DEVUELVE LA LISTA DE ELEMENTOS
// ELIMINADOS.
// (posición,  elementos a eliminar, elem1, elem2, ...)

// document.write("Colores: ", colores, "<br>")
// document.write(colores.splice(1, 1), "<br>")
// document.write("Colores: ", colores, "<br>")


//----------------------------------------
// El método slice (start, end) devuelve los elementos
// seleccionados como un nuevo objeto

// document.write("Beatles : ", beatles, "<br>")
// document.write(beatles.slice(1, 3), "<br>")


//----------------------------------------
// El método reverse() Invierte el orden
// de elementos del array (NO ORDENA):

// document.write("Beatles : ", beatles, "<br>")
// document.write("Beatles : ", beatles.reverse(), "<br>")
// document.write("Beatles : ", beatles, "<br>")

//----------------------------------------
// El método sort() ordena alfabeticamente un array:

// var valores = [1, 60, 6, 64, 3, 2, 5, 7]

// document.write("Colores : ", valores, "<br>")
// document.write("Colores : ", valores.sort(), "<br>")
// document.write("Colores : ", valores, "<br>")

//----------------------------------------
// El método sort(func) ordena un array
// segun el CRITERIO definido por func.
//( La función debe devolver un valor negativo,
// cero o positivo):

// var numeros = [40, 100, 1, 5, 25, 10];
// document.write(numeros, "<br>")
// document.write(numeros.sort(function(a, b){return a-b}))


//----------------------------------------
// .forEach(cb, arg)  Realiza la operación
// definida en cb PARA CADA elemento del array:

// function sumarUno(elemento, indice) {
//     document.write(elemento = elemento+1, " ")
// }

// var numeros = [40, 100, 1, 5, 25, 10];
// document.write(numeros, "<br>")
// numeros.forEach(sumarUno)



//----------------------------------------
// .every(cb, arg)  comprueba si TODOS los
// elementos cumplen alguna condición:

function comprobarEdad(elemento, indice) {
    return elemento >= 18
}

// var edades = [40, 100, 18, 53, 25, 45];
// document.write("¿Son todos mayores? ", edades.every(comprobarEdad), "<br>")

// document.write("¿Son todos menores? ", !edades.every(comprobarEdad), "<br>")


//----------------------------------------
// .some(cb, arg)  comprueba si ALGUNO los
// elementos cumplen alguna condición:

// function comprobarEdad(elemento, indice) {
//     return elemento >= 18
// }

// var edades = [40, 100, 18, 53, 25, 14];
// document.write("¿Alguno es mayor? ", edades.some(comprobarEdad), "<br>")


//----------------------------------------
// .map(cb, arg)  comprueba si ALGUNO los
// elementos cumplen alguna condición:

// var duplicar = (elemento, indice) => elemento * 2
// var alCuadrado = (elemento, indice) => elemento * elemento

// var valores = [2, 3, 1, 4, 5, 10];
// document.write("Original.......", valores, "<br>")
// document.write("Duplicados.....", valores.map(duplicar, 3), "<br>")
// document.write("Cuadrados......", valores.map(alCuadrado), "<br>")

// document.write("Original.......", valores, "<br>")

//----------------------------------------
// .filter(cb, ) Filtra elementos que cunplen
// con alguna condicion:

// var comienzaConA = (elemento) => elemento[0] == "A"

// var valores = ["Ariel", "anana", "Pablo", "Mariana", "Ana"];
// document.write("Original.......: ", valores, "<br>")
// document.write("Comienzan con A: ", valores.filter(comienzaConA), "<br>")


//----------------------------------------
// .find(cb,arg ) Devuelve el primer elemento
//  que cumple la condición de cb:

// function comprobarEdad(edad) {
//     if (edad >= 18) {
//         return edad
//     }
// }

// var edades = [15, 40, 100, 18, 53, 25, 14];
// document.write("¿Alguno es mayor? ", edades.find(comprobarEdad), "<br>")

// // Otro métodos "de la familia" de .find
// document.write("¿Alguno es mayor? ", edades.findIndex(comprobarEdad), "<br>")




//----------------------------------------
// .reduce(cb,arg )Ejecuta cb con cada
// elemento (de izq a der), acumulando el resultado.:

// var restarValores = (total, elemento) => total - elemento

// var valores = [100, 10, 15, 5, 20];
// document.write("Valores disponibles:", valores, "<br>")
// document.write("Reduce.............:", valores.reduce(restarValores), "<br>")

// Otro métodos "de la familia" de .reduce
// document.write("ReduceRight.............:", valores.reduceRight(restarValores), "<br>")


//----------------------------------------
// En w3schools tenemos todos los métodos y
// ejemplos de los mismos:
//
// https://www.w3schools.com/jsref/jsref_obj_array.asp
//
//----------------------------------------

