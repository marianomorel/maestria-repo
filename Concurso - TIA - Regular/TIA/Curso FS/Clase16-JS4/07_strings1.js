// En este script vamos a analizar las
// principales propiedades de los objetos
// string.
// Excelente información aqui:
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String
//----------------------------------------


// Creacion:
//                       1111111
//             01234567890123456
var cadena1 = "Método mas simple"
var cadena2 = new String ("Usando un constructor")

document.write("cadena1: "+cadena1+"<br>")
document.write("cadena2: "+cadena2+"<br><br>")

// Las cadenas son variables que se pueden
// redefinir:
var cadena1 = "Full Stack Python"
var cadena2 = "Codo a Codo 2022"

document.write("cadena1: "+cadena1+"<br>")
document.write("cadena2: "+cadena2+"<br><br>")

//----------------------------------------
// La propiedad .lenght nos proporciona
// el número de caracteres que contiene
// el string:
document.write("Longitud cadena1: "+cadena1.length , "<br>")
document.write("Longitud cadena2: "+cadena2.length , "<br><br>")

//----------------------------------------
// La propiedad .charAt nos devuelve el
// caracter ubicado en una posición:
document.write("cadena1, pos.5: "+cadena1.charAt(5)+"<br>")
document.write("cadena1, pos.6: "+cadena1.charAt(6)+"<br>")
document.write("cadena1, pos.7: "+cadena1.charAt(7)+"<br>")
document.write("cadena1, pos.8: "+cadena1.charAt(8)+"<br>")
document.write("cadena1, pos.9: "+cadena1.charAt(9)+"<br><br>")

//----------------------------------------
// La propiedad .concat une un string al
// final del actual:
document.write(cadena1.concat(" - "+cadena2) , "<br>")
document.write("Hola ".concat("clase!") , "<br>")
document.write("Hola "+ "clase!" , "<br><br>")

//----------------------------------------
// La propiedad .indexOf(str, from) nos
// devuelve la primera posicion en que srt
// aparece en la cadena:
document.write("Posición primera letra 'F' en cadena1: ")
document.write(cadena1.indexOf("F") , "<br>")

document.write("Posición primera letra 'S' en cadena1: ")
document.write(cadena1.indexOf("S") , "<br>")

document.write("Posición primera letra 'P' en cadena1: ")
document.write(cadena1.indexOf("P") , "<br>")

// Si agregamos el valor del "from", devuelve
// la primer ocurrencia a partir de esa posición:
document.write("Posición del 2do. 'Codo' en cadena2 : ")
document.write(cadena2.indexOf("Codo", 4) , "<br><br>")

//----------------------------------------
// La propiedad .lastIndexOf(str, from) es
// similar pero contando desde el final.
document.write("Posición última letra 'C' en cadena2: ")
document.write(cadena2.lastIndexOf("C") , "<br>")

document.write("Posición última letra 'o' en cadena2: ")
document.write(cadena2.lastIndexOf("o") , "<br>")

document.write("Posición letra o (from=7) en cadena2: ")
document.write(cadena2.lastIndexOf("o",7) , "<br>")

document.write("Posición última letra 'm' en cadena2: ")
document.write(cadena1.lastIndexOf("m") , "<br><br>")

//----------------------------------------
// La propiedad .repeat(n) devuelve la
// cadena repetida "n" veces:
document.write("Hola! ".repeat(3) , "<br>")
document.write("-".repeat(30) , "<br><br>")

//----------------------------------------
// .toLowerCase() y .toUpperCase()
// convierten una cadena a minúsculas
// y mayúsculas respectivamente:

document.write(cadena1               , "<br>")
document.write(cadena1.toLowerCase() , "<br>")
document.write(cadena1.toUpperCase() , "<br><br>")

//----------------------------------------
// .trim() elimina espacios a derecha e
// izquierda:

var cadena = "    texto    "  //Ojo: HTML solo "cuenta" uno de todos los espacios que ponemos!
document.write("[" + cadena + "]<br>")
document.write("[" + cadena.trim() + "]<br><br>")

//----------------------------------------
// .replace(str, newstr) reemplaza la
// primera aparición del texto str por
// newstr:
document.write(cadena2, "<br>")
document.write(cadena2.replace("Codo", "Mano")  , "<br><br>")

//----------------------------------------
// .substr(ini, len) devuelve el subtexto
// desde la posición ini hasta ini+len.
//            0123456789012345678901234
var cadena = "Esta es una bonita cadena"
document.write(cadena, "<br>")
document.write(cadena.substr(12, 6)  , "<br><br>")

//----------------------------------------
// .substring(ini, end) devuelve el subtexto
// desde la posición ini hasta end.
//            0123456789012345678901234
var cadena = "Esta es una bonita cadena"
document.write(cadena, "<br>")
document.write(cadena.substring(0,4)  , "<br>")


