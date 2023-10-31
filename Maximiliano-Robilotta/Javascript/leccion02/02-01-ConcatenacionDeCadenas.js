var nombre = "José";
var apellido = " Montes";
var nombreCompleto = nombre+" "+apellido; // Primera Concatenación
console.log(nombreCompleto);
var nombreCompleto2 = "Maximiliano"+" "+"Robilotta"; // Segunda Concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izq a der siguiendo la cadena lee el número como String
console.log(juntos);
juntos = nombre + 78 + 17; // Aquí se puede diferenciar a través de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre; // Primero suma, luego concatena.
console.log(juntos);

nombre += apellido; // Tercera Concatenación usando el operador simplificado
console.log(nombre);

// Hoy ya no se utiliza var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lopes";
// apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido2); // Console = Objeto, que llama al método o función .log y entre paréntesis se colocan los argumentos.

let x, y; // Se pueden crear varias variables dentro de una misma línea
x = 17, y = 21; // Se puede hacer asignación de varias variables dentro de una misma línea
let z = x + y; // Se asigna el valor de la operación
console.log(z);

let _1num = 31; // No utilizar números para iniciar el nombre de una variable
let rompiendo = "rompe"; // No utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);