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

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor 
var y  = null; // null no es un tipo de dato, pero su origen es tipo objet
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ["Citroen","Audi","BMW","Ford"];
console.log(autos);
console.log(typeof autos); //preguntamos que tipo de dato es:

var z= " ";
console.log(z);//Esto se refiere a una cadena vacia:
console.log(typeof z);
