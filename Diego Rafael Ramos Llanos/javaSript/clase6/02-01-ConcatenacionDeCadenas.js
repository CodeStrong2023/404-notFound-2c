var nombre = "Jose ";
var apellido = "Montes ";
var nombreCompleto = nombre + " " + apellido; 
console.log(nombreCompleto);

var nombreCompleto2 = "Diego " + "Rafael";
console.log(nombreCompleto2);

var juntos = nombre + 219; // Concatena el número con un Str.
console.log(juntos);
juntos = nombre + 78 + 17; 
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //Concatenación con el operador simplificado.
console.log(nombre);