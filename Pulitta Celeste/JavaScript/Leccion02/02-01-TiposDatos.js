//Tipos de datos en Javascript
/*
La sintaxis en lo que es comentarios
es muy similar a la de java
realmente diriamos que es identica
*/

var nombre = "Ariel";//Tipo str
console.log(nombre);
nombre = 7;
console.log(nombre);
nombre = 12.3;
console.log(nombre);
//Tipo numerico
var numero = 3000;//Tipo Numerico
console.log(numero);
//Tipo Object
var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2619868987"

}

console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo)

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
    this.nombre = nombre;
    this.apellido = apellido;
    }
}

console.log(typeof Persona)

//Tipo de dato undefined
var x;
console.log(typeof x);
x = undefined;
console.log(typeof x)

//null: significa ausencia de un valor
var y = null;//null no es un tipo de dato, pero es de tipo object
console.log(typeof y)

//Tipo de dato array y Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford']
console.log(autos);
console.log(typeof autos);

var z= '';
console.log(z); //Esto se refiere a que es una cadena vacia
console.log(typeof z);
