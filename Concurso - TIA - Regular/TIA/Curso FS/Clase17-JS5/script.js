// Imprime una cadena. Si tiene otro parámetro en
// false, NO hace un salto de linea. Por defecto salta
// a la linea siguiente.
function imprimir(cadena ="", salto=true){
    document.write(cadena)
    if (salto) document.write("<br>")
}