var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido;//primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "Ariel"+' '+"Betancud";//segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219;// Lee de izq a der siguiendo la cadena de numeros
console.log(juntos);
juntos = nombre+ 78 + 17;//aqui se puede diferenciar atraves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre; //
console.log(juntos);

nombre += apellido; //Tercera concatenacion usando el operador simplificado
console.log(nombre)

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido2)

let x, y; //se pueden crear varias variables dentro de la misma linea
x = 17, y = 21; // se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y; //se asigna el valor de la operacion
console.log(z)

let _1num = 31; //no utilizar numeros para iniciar el nombre de una variable
let rompiendo = "rompe";//No utilizar palbras reservadas para variables

console.log(_1num)
console.log(rompiendo)