// Limpiamos la consola
console.clear();

// Mostramos el valor de algunas constantes:
console.log("Número PI:", Math.PI);     // Razón entre circunferencia y diámetro
console.log(" Número e:", Math.E);      // Número de Euler, base de los logaritmos naturales
console.log("      LN2:", Math.LN2);    // Logaritmo natural de 2
console.log("     LN10:", Math.LN10);   // Logaritmo natural de 10
console.log("    LOG2E:", Math.LOG2E);  // Logaritmo en base 2 de e
console.log("   LOG10E:", Math.LOG10E); // Logaritmo en base 10 de e
console.log("    SQRT2:", Math.SQRT2);  // Raiz cuadrada de 2
console.log("  SQRT1_2:", Math.SQRT1_2);// Raiz cuadrada de 0.5

// Uso de algunos métodos de Math.
// var cateto1 = 10;
// var cateto2 = 15;
// var hipotenusa = Math.sqrt(Math.pow(cateto1,2) + Math.pow(cateto2,2))
// console.log("Teorema de Pitágoras"); 
// console.log("Cat1:", cateto1, "Cat2:",cateto2, "Hipotenusa:", hipotenusa)


// Metodo Random()
// Obtenemos un número al azar entre [0, 1) con 16 decimales
let x = Math.random();
console.log(x);
// Multiplicamos x por el valor máximo que buscamos (5)
x = x * 5;
console.log(x);
// Redondeamos hacia abajo, obtenemos un entero
x = Math.floor(x);
console.log(x);
