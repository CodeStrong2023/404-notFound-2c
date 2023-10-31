var nombre="jose";
var apellido="Montes";
var nombreCompleto=nombre+" "+apellido;//primera concatenacion
console.log(nombreCompleto); 
var nombreCompleto2="ariel"+" "+"betancud";//segunda concatenacion
console.log(nombreCompleto2);
var juntos=nombre+219;//lee de izq a der siiguiendo la cadena lee el numero como str
console.log(juntos);
juntos=nombre+78+17;//aqui se puede diferenciar a traves de los parentesis
console.log(juntos);
juntos=78+17+nombre;
console.log(juntos);

nombre+=apellido; //tercera concatenacion usando el operador simplificado
console.log(nombre);

//hoy ya no se usa var, se utiliza let y const
let nombre2="Pedro";
console.log(nombre2);

const apellido2="Lepes";
//apellido2="perez"; una constante no puede ser modificada
console.log(apellido2);
let x,y; //se pueden crear varias variables dentro de una misma linea
x=17,y=21;//se puede hacer asignaciones de varias variables dentro de la misma linea
let z=z=y;//se asigna el valor de la operacion
console.log(z);

let _1num=31;//no utilizar numeros para iniciar el nombre de una variable
let rompienndo="rompe";//no utilizar palabras reservadas para variables

console.log(_1num)
console.log(rompienndo)
