var nombre = "Gonzalo";
nombre = "Nicolas";
console.log(nombre);

function saludar() {
    var nombre2 = "Natalia";
    console.log(nombre2);
}
//console.log(nombre2) // Aqui no lee el dato de la función.

if (true) {
    var edad = 20;
    console.log(edad);
}
console.log(edad); // Esto es una falla, no deria de leer el dato fuera del if, por eso se dejó de usar var. 

/*
let: Esta pueder ser reasignada en cualquier momento, la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves o dentro de una función.
*/

function saludar2() {
    let nombre2 = "Gonzalo";
    console.log(nombre2);
}
//console.log(nombre2)

if (true) {
    let edad2 = 20;
    console.log(edad);
}
//console.log(edad2);

// const: Se utiliza para valores constantes osea que no pueden ser reasignados.
const fechaNacimiento = 2002;
console.log(fechaNacimiento);
fechaNacimiento = 2006; // No se puede reasignar una constante.