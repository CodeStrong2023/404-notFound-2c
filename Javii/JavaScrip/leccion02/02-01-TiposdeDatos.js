//Tipos de datos en javascript
//
//La sintaxis en lo que es comentarios
//es muy similar a la de Java
//realmente diriamos que es identica

var nombre = "Ariel";//Tipo str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000;// Tipo numerico
console.log(numero);

var objeto = {
    nombre: "Ariel",
    apellido : "Betancud",
    telefono : "28483934"
}

console.log(objeto);

// Tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipos de datos symbol
var simbolo = Symbol("Mi simbolo")
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);
