// Ampliando el uso de var, let y const
/*
Var: Con var puedes reasignar en cualquier momento
esta forma parte del ámbito global 
Un error es que se sobreescriba
*/

var nombre = "Enzo";
nombre = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia";
    console.log(nombre3);
}
//console.log(nombre3); // Aquí no lee el dato en la función

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); // En la función funcionó correctamente, en la estructura if falló

/*
Let: Ésta puede ser reasignada en cualquier momento
la diferencia es que su ámbito es de bloque,
solo disponible dentro de un bloque de llaves o dentro de una función
*/

function saludar2(){
    let nombre2 = "Enzo";
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
Const: Se utiliza para valores constantes que no pueden ser reasignadas
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); // Solo se ejecuta el console anterior