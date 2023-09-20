//Tipos de datos en JavaScript
/*
La sintaxis en lo que es comentarios es muy similiar a Java
realmente diriamos que es identica
*/
var nombre = "Guillermo"; //Tipo str
console.log(typeof nombre);
 
var numero = "3000"; //Tipo numerico
console.log(numero);

var objeto = {
    nombre : "Guillermo",
    apellido : "Giannone",
    telefono : "2604567891"
}
console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion)

//Tipo de dato symbol
var simbolo = Symbol("Mi Simbolo");


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
var y = null; //null no es un tipo de dato, pero su origen es de tipo objet
console.log(typeof y);

//Tipo de datos array y Empty String
var autos = ["Citroen","Audi","BMW","Ford"];
console.log(autos);

var z = "";
console.log(z); // Esto se refiere a que es una cadena vacia
console.log(typeof z);