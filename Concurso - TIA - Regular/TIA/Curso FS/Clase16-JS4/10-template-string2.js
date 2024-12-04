//Función usando Template Strings
function suma(num1,num2){
    return num1+num2;
   }

// Declaro las variables y le asigno valores
let a = 6
let b = 7
console.log("La suma de " + a + " y " + b + " es " + suma(a,b));
console.log(`La suma de ${a} y ${b} es ${suma(a,b)}`);

// Por supuesto, la función suma(a,b) no es necesaria,
// solo lo inclumos como parte del ejemplo. Se puede
// realizar la operación directamente en el template:
console.log(`La suma de ${a} y ${b} es ${(a+b)}`);