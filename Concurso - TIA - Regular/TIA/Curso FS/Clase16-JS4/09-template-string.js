//Función usando Template Strings
function saludar(nombre, edad){
    //console.log("Mi nombre es " + nombre + " y mi edad es " + edad);
    console.log(`Mi nombre es ${nombre} y tengo ${edad} años.`);
}

saludar("Carlos", 32);

// Podemos pedir los datos al usuario, y
// luego llamar a la función con esos
// argumentos:
var n = prompt("Introduce tu nombre");
var e = prompt("Introduce tu edad");
saludar(n, e);