// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica.
*/
var nombre = "Diego"; //Tipo str
console.log(nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
var numero = "3000"; 
console.log(numero);

var objeto = {
    nombre : "Diego",
    apellido : "Rafael",
    telefono : "12353524"
}
console.log(objeto);
var bandera = true;
console.log(bandera);

// Tipo de Dato Funcion(Permite reutilizar líneas de código)
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de Dato Symbol
var simbolo = Symbol("Mi símbolo");
console.log(typeof simbolo);
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
// Tipo undefined
var x;
console.log(typeof x);
x = undefined;
console.log(typeof x);

// null = a ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es de tipo object.
console.log(typeof y);

var autos = ["Citroen", "Audi", "BMW", "Ford"];
console.log(autos);
console.log(typeof autos);

var z = "";
console.log(z); // empty (cadena vacia)
console.log(typeof z);