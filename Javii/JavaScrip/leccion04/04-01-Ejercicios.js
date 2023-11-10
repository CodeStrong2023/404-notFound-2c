//Ejercicio 1: Calcular estacion del año
let mes = 9;
let estacion; // Unidefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if (mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if (mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estacion de: "+estacion);
// Ejercicio 2: Hora del dia 

// de 6 a 11 nos saluda Good: Mornig 
// de 12 a 16 nos saluda Good: Afternoom
// de 17 a 19 nos saluda Good: evening
// de 20 a 23 nos saludara: Good night
// Trabajamos con 24hs

let horaDia = 7; 
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good Morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good Afternoom";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good Evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good Night";
}
else{
    mensaje = "Valor Incorrecto";
}
console.log(mensaje);

// Etructura swich(la sintaxis es igual a la de Java)
switch(mes){ // No solo se pueden utilizar numero, tambien cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor Incorrecto";
}
console.log("Bienvenido a la estacion de: "+estacion);

// Ampliando el uso de var let y const

//Con var podes reasignar en cualquier momento
// esta forma parte del ambito global
// Un error es que se sobreescriba


var nombre = "Ariel";
nombre = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia";
    console.log(nombre3);
}
//console.log(nombre3);// Aqui no lee el dato en la funcion


if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad);


//let: Esta puede ser reasignada en cualquier momento
// la difencia es que su ambito es de bloque,
// solo disponible dentro de un bloque de llaves
// o dentro de una funcion


function saludar2(){
    let nombre2 = "Ariel";
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad);
}
console.log(edad);


//const se utiliza para valores constantes que no pueden ser reasignadas



const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento);

//Evitar repetir tu codigo
// Dry don't repeat yourself

let days = 5;
switch (days){
    case 1:
        console.log("Hoy es Lunes");
        break;
    case 2:
        console.log("Hoy es Martes");
        break;
    case 3:
        console.log("Hoy es Miercoles");
        break;
    case 4:
        console.log("Hoy es Jueves");
        break;
    case 5:
        console.log("Hoy es Viernes");
        break;
    case 6:
        console.log("Hoy es Sabado");
        break;
    case 7:
        console.log("Hoy es Domingo");
        break;
    default:
        console.log("Error en el ingreso del dia de la semana");
        break;
}

// Esta es la opcion mejorada

let day2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];
function getDay(n){
    if (n < 1 || n > 7){
        throw new Error("out of range");
    }
    return day2[n-1];
}
console.log(getDay(3));