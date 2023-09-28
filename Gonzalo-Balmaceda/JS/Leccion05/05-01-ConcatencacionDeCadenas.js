var nombre = "Jose";
var apellido = "Montes";
var nombreCompleto = nombre + " " + apellido; // Primero  Concatenación.
console.log(nombreCompleto);

var nombreCompleto2 = "Gonzalo " + "Balmaceda"; // Segunda Concatenación.
console.log(nombreCompleto2);

var juntos = nombre + 219; // Concatena el número con un Str.
console.log(juntos);

juntos = nombre + 78 + 17; 
console.log(juntos);

juntos = 78 + 17 + nombre; // Al tener los número primero los suma y despues concatena con el Str.
console.log(juntos);

nombre += apellido; // Tercera Concatenación con el operador simplificado.
console.log(nombre);