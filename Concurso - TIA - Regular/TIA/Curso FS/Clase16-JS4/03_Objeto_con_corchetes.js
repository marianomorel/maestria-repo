// Se puede acceder o establecer las propiedades 
// de los objetos mediante la notación de corchetes.
// En los objetos cada propiedad está asociada con
// un valor tipo String que se puede utilizar para
// acceder a ella. Por lo tanto puedes acceder a las
// propiedades del objeto miPerro de la siguiente
// manera:

// Creamos un objeto
var myperro = { nombre: "Toby", edad: 3, color: "blanco" }

// Mostramos alguna propiedad con esta notacion:
console.log (myperro['nombre'])

// Cambiamos valor de la propiedad y mostramos:
myperro['nombre'] = 'Tati'
console.log (myperro['nombre'])

// Por supuesto, podemos seguir usando la 
// notación "tradicional"
myperro.nombre = "Juancito"
console.log (myperro.nombre)

