// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica.
*/

// Tipo String
var nombre = "Maximiliano"; 
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

// Tipo Numérico
var numero = 3000; 
console.log(numero);

var objeto = {
    nombre : "Maximiliano", 
    apellido : "Robilotta",
    teléfono : "2625262526"
}

console.log(typeof objeto);

// Tipos de Datos Booleanos
var bandera = true;
console.log(bandera);

// Tipo de Dato Función (Permite reutilizar líneas de código)
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de Dato Symbol
var simbolo = Symbol("Mi símbolo");
console.log(typeof simbolo);

// Tipo de Dato Clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

// Tipo de Dato Undefined
var x; 
console.log(typeof x);

x = undefined; // Variable no definida
console.log(typeof x);


// Null: Significa ausencia de valor
var y = null; // Null no es un tipo de dato pero su origen es de tipo object
console.log(typeof y);


// Tipo de Dato array (de tipo object) y Empty String
var autos = ["Citroen", "Audi", "BMW", "Ford"];
console.log(autos);
console.log(typeof autos); // Preguntamos que tipo de dato es:

var z = "";
console.log(z); // Esto se refiere a que es una cadena vacía
console.log(typeof z);