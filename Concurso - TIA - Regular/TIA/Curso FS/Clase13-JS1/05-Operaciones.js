// Declaramos algunas variables
var num1 = 10;
var num2 = 20;
var cadena1 = "Hola ";
var cadena2 = ", cómo estás?";
var nombre = "Ana";

// Operamos con ellas:
var resultado = num1 + num2;
console.log("La suma de",num1,"y",num2,"es",resultado);

// El + en JS sirve para "pegar" (concatenar) cadenas:
var frase;
frase = cadena1 + nombre + cadena2;
console.log(frase);

// Cuidado con estos casos:
var resultado = num1 + "3";
console.log(resultado);

// Más operaciones:
resta = num1 - num2;      // Resta
producto = num1 * 8;      // Multiplicación
cociente = num2 / num1;   // División
modulo = 13 % 5;          // 3 (el resto de dividir 13 entre 5)
potencia = num1 ** 2;     // Elevamos num1 al cuadrado
num1++;                   // Incremento (suma 1 al valor de num1)
num1--;                   // Decremento (resta 1 al valor de num1)

// Una curiosidad. ¿Puedes explicar que ocurre?

//console.log(0.1 + 0.2)