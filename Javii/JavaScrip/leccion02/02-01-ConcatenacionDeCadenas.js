var nombre = "Jose ";
var apellido = "Montes";
var nombreCompleto = nombre+" "+apellido;//Primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "Ariel"+" "+"Betancud";// Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izquierda a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17;// Aqui se puede diferenciar a travez de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos)

nombre += apellido;
console.log(nombre)

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido)

let x, y; //Se puden crear varias variables en una misma linea
x = 17, y = 21; // se puede hacer asignacion de varias variables dentro de una misma linea
let z = x + y; // Se asigna el valor de la operacion
console.log(z);

let _1num = 31; //No utilizar numeros para iniciar el nombre de una variable
let rompiendo = "rompe"; // No utilizar palabras reservadas para variables

console.log(_1num)
console.log(rompiendo)