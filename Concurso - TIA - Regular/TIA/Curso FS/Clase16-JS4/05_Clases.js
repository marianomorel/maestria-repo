//---------------------------------------
// Las clases son una suerte de “molde” que
// podemos usar para crear varios objetos
// del mismo tipo. Usamos un constructor y
// this para asignar valores a las propiedades
// de los objetos instanciados:
//---------------------------------------

// Clase Perro, con su constructor:
class Perro {
    constructor( nombre, edad, vivo){
         this.nombre = nombre
         this.edad   = edad
         this.vivo   = vivo
         }
     }
// Fin de la declaracion de la clase

// Instanciamos dos objetos clase Perro:
var perro1 = new Perro ("Lola", 4, true)
var perro2 = new Perro ("Lassie", 10, false)

// Mostramos algunas propiedades de los objetos:
console.log(perro1.nombre,"tiene",perro1.edad,"años")
console.log(perro2.nombre,"tiene",perro2.edad,"años")


// El tema de las Clases es mucho mas amplio y rico.
// Lo vamos a retomar en Python, donde veremos temas
// como herencia, polimorfismo, etc.