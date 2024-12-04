//---------------------------------------
// Para deﬁnir un tipo (clase) de objeto, 
// creamos una función que especiﬁque su 
// nombre, propiedades y métodos. Supongamos
// que deseas una clase llamada “Auto” para
// crear objetos “auto”, y deseas que tenga
// las siguientes propiedades: marca, tipo y
// modelo. Podrías escribir la siguiente función:

// Función constructora
function Auto(marca, tipo, modelo) {
    // Atributos
    this.marca = marca
    this.tipo = tipo
    this.modelo = modelo

    // Métodos
	this.mostrar = function() {
		return "Soy un "+this.marca+" modelo "+this.tipo+" del año "+this.modelo}
    }
// Fin de la declaracion de la función constructora

//Instanciamos el objeto miAuto
var miAuto = new Auto('Ford','Focus', 2019)

// Instanciamos el objeto miFurgon
var miFurgon = new Auto('Renault','Traffic', 2010)

// Mostramos algunas propiedades de los objetos:
console.log("Tengo un",miAuto.marca,"modelo",miAuto.tipo,"del año",miAuto.modelo)
console.log("Tengo un",miFurgon.marca,"modelo",miFurgon.tipo,"del año",miFurgon.modelo)

// Mostramos la salida del método "mostrar":
console.log(miAuto.mostrar())
console.log(miFurgon.mostrar())