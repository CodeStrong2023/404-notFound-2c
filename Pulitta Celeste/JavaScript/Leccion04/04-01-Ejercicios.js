//Ejercicio 1: calcular estacion del año
let mes = 9;
let estacion; //Undefined
if(mes == 1 || mes ==2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes== 8){
    estacion = "invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estacion de: "+estacion);
 
//Ejercicio 2: Hora del dia
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good afternoon
de 17 a 19 nos saluda: good eveningh
de 20 a 23 nos saluda : good nigth
Trabajaremos con 24 horas
*/
let horaDia = 7;
let mensaje;
if(horaDia >= 6 && horaDia <=11){
    mensaje = "Good Morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good afternoom"
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good nigth";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje);

//Estructura switch(la sintaxis es igual a Java)
switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Primavera";
        break;
    case 9: case 10: case 11:
        estacion = "Verano"
        break;
    default:
        estacion = "valor incorrecto"
}
console.log("Bienvenido a la estacion de: "+estacion);

//Ampliando el uso de var let y const
/* 
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescribe
*/

var nombre = "Ariel";
nombre = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia";
    console,log(nombre3);
}
//console.log(nombre3); //aqui no le el dato en la funcion

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); // en la funcion funciono correctamente en la estructura if fallo

/* 
let; esta puede ser reasignada en cualquier momento
la diferencia es que su ambito de bloque
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre2= "Ariel";
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*c
const se utiliza para valores constantes que no pueden ser reasignados
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anteior
//let days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];

//evitar repetir tu codigo
// dry dont repeat yourself

let days= 1;

switch (days) {
    case 1:
        console.log('hoy es Lunes');
        break;
    case 2:
        console.log('hoy es Martes');
        break;
    case 3:
        console.log('hoy es Miercoles');
        break;
    case 4:
        console.log('hoy es Jueves');
        break;
    case 5:
        console.log('hoy es Viernes');
        break;
    case 6:
        console.log('hoy es Sabado');
        break;
    case 7:
        console.log('hoy es Domingo');
        break;
    default:
        console.log('Error en el ingreso del dia de la semnaa');
        break;
}

//Esta opcion es mejorada

let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
function getDays(n){
    if(n < 1 || n> 7){
        throw new Error('out of range')
    }
    return days2[n-1];
}
console.log(getDays(3));