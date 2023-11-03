// Tipos de datos en Javascript
/*
La sintáxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es idéntica
*/
var nombre = "Matias"; //Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000; //Tipo numérico
console.log(numero);

var objeto = {
    nombre : "Matias",
    apellido : "Landi",
    telefono : "2604408188"

}

console.log(typeof objeto);

//Tipo de dato booleano
var bandera = true;
console.log(typeof bandera);

//Tipo de dato función
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi símbolo");
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);