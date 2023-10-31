//tipos de datos en javascript

/*
la sintaxis en lo que es comentarios
es muy similar a la de java
realmente 
*/
//tipo String 
var nombre="Ariel"; //tipo str
console.log(typeof nombre);
nombre=7; 
console.log(typeof nombre);
 nombre=3.6;
console.log(typeof nombre);
//tipo numerico
var numero=3000; //tipo numerico
console.log(numero);
//tipo objeto
var objeto={
    nombre:"ariel",
    apellido: "betancud",
    telefono:1122334455
}
console.log(objeto);
console.log(typeof objeto);

//tipo de dato boolean
var bandera=true;
console.log(bandera);

//tipo de dato funcion
function miFuncion(){
    console.log(typeof miFuncion);
}

//tipo de dato symbol
var simbolo=symbol("mi simbolo");
console.log(typeof simbolo);
console.log(simbolo);

//tipo de dato clase
class Persona{
    constructor(nombre,apellido){
    this.nombre=nombre;
    this.apellido=apellido;
    }
}

console.log(Persona);
console.log(typeof Persona);

//tipo de dato undefined
 var x;
 console.log(typeof x);
 console.log(x);
 //null: significa ausencia de valor
 x=undefined;
 console.log(x);

 var y=null; //null no es un tipo de dato, pero 
 //su origen es object

 console.log(typeof y);
//tipo de dato array y empty string
var autos=["citroen","audi","bmw","ford"];
console.log(autos); 
console.log(typeof autos); //preguntamos que tipo de dato es:
var z="";
console.log(z); //esto se refiere a que es una cadena vacia
console.log(typeof z);


