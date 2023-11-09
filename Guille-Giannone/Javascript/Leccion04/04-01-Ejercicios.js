//Ampliamos el uso de var let y const
/*
Con var puedes reasiganr en cualquier momento
este forma parte del ambito global
Un error es que se sobreescriba
*/
var nombre = "Ariel";
nombre = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia";
    console.log(nombre3);
}
//console.log(nombre3);//Aqui no lee el dato en la funcion

if (true){
    var edad = 34;
    console.log(edad);
}
console.log(edad);//En la funcion funciono correctamente en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre2 = "Ariel";
    console.log(nombre2);
}
//console.log(nombre2);
if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);
/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/
const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento);// Solo se ejecuta el console anterior


//Ejercicio 1: Calcular la estacion del año
let mes = 12;
let estacion;
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
} 
else if (mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño"
}
else if (mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno"
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera"
}
else{
    estacion = "Valor Incorrecto"
}
console.log("El valor corresponde a la estacion: "+estacion);

//Ejercicio 2: Hora del dia
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good Afternoom
de 17 a 19 nos saluda: Good evening
de 20 a 23 nos saluda: Good night
Trabajaremos con 24 hs
*/
let horaDia = 7;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good Morning"
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good Afternoom"
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good Evening"
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good Night"
}
else{
    mensaje = "Valor incorrecto"
}
console.log(mensaje)

//Estructura Swith (la sintaxis es igual a java)
switch(mes){ // no solo se puede usar numero sino tambien cadena
    case 1: case 2: case 12:
        estacion = "Verano"
        break;
    case 3: case 4: case 5:
        estacion = "Otoño"
        break;
    case 6: case 7: case 8:
        estacion = "Invierno"
        break;
    case 9: case 10: case 11:
        estacion = "Primavera"
        break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estacion de: "+estacion);


//Evitar Repetir tu codigo
//Dry don´t repeat youtself
let days = "8";
switch (days) {
    case "1":
        console.log("hoy es: Lunes");
        break;
    case "2":
        console.log("hoy es: Martes");
        break;
    case "3":
        console.log("hoy es: Miércoles");
        break;
    case "4":
        console.log("hoy es: Jueves");
        break;
    case "5":
        console.log("hoy es: Viernes");
        break;
    case "6":
        console.log("hoy es: Sábado");
        break;
    case "7":
        console.log("hoy es: Domingo");
        break;

    default:
        console.log("Error en el ingreso del día de la semana")

        break;
}
//Esta es la opcion mejorada

let days2 = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"];

function getDay(n){
    if(n < 1 || n > 7){
        throw new Error("out of range");
    }
    return days2[n-1];
}
console.log(getDay(1));

//Hacer un ejercicio similar al que esta hecho pero ahora con los meses del año
//debes hacerlo con la estructuta switch y luego con la funcion de opcion mejorada

let meses = 10;
switch (meses) {
    case 1:
        console.log("El mes es Enero");
        break;
    case 2:
        console.log("El mes es Febrero");
        break;
    case 3:
        console.log("El mes es Marzo");
        break;
    case 4:
        console.log("El mes es Abril");
        break;
    case 5:
        console.log("El mes es Mayo");
        break;
    case 6:
        console.log("El mes es Junio");
        break;
    case 7:
        console.log("El mes es Julio");
        break;
    case 8:
        console.log("El mes es Agosto");
        break;
    case 9:
        console.log("El mes es Setiembre");
        break;
    case 10:
        console.log("El mes es Octubre");
         break;
    case 11:
        console.log("El mes es Noviembre");
        break;
    case 12:
        console.log("El mes es Diciembre");
        break;
    default:
        console.log("Erro de ingreso número de mes")
        break;
}
//Opcion de funcion mejorada
let meses2 = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agoso","Setiembre","Octubre","Noviembre0","Diciembre"];

function getMeses(n){
    if(n < 1 || n > 12){
        throw new Error("out of range");
    }
    return meses2[n-1];
}
console.log(getMeses(9));