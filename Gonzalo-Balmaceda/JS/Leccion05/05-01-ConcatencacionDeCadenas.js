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

// Hoy ya no se usar 'var', se usa let y const.
const nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lopez";
// apellido2 = "Perez"; Una constante no puede ser modificada.
console.log(apellido2);

let x, y; // Se pueden crear varias variables dentro de una misma linea.
x = 17, y = 21; // Se pueden hacer asignaciones de varias variables dentro de una misma linea.
let z = x + y; // Se asigna el valor de la operación.