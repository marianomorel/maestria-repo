//---------------------------------------
// Veamos cómo definir un nuevo objeto 
// Perro, con los métodos quienSoy() y 
// ladrar():
//---------------------------------------


var perro = {
    nombre: "Milo",    // Propiedad "nombre"
    edad: 12,          // Propiedad "edad"
    color: "negro",    // Propiedad "color"

    // Este es un método:
    quienSoy() {return "Soy " + this.nombre},

    // Y este es otro:
    ladrar() {return this.nombre + " dice guau!"}
}
// Fin de la declaracion del objeto

// Mostramos algunas propiedades del objeto:
console.log(perro.nombre,"tiene",perro.edad,"años")

// Y usamos uno de sus métodos:
console.log(perro.quienSoy())

// Podemos utilizar un método solo si una propiedad
// tiene determinado valor:
if (perro.color == "negro") {
    console.log(perro.ladrar())
}