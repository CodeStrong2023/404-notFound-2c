// Ejercicio 1 = Calcular stación del año

let mes = 6;
let estacion;

if (mes == 1 || mes == 2 || mes == 12) {
    estacion =  "Verano";
} else if (mes == 3 || mes == 4 || mes == 5) {
    estacion = "Otoño";
} else if (mes === 6 || mes === 7 || mes === 8) {
    estacion = "Invierno";
} else if (mes === 9 || mes === 10 || mes === 11) {
    estacion = "Primavera";
} else {
    console.log("Valor Incorrecto");
}

console.log("El mes ingresado corresponde a la estación de: "+estacion);

// Ejercicio 2 = Hora del dia
/* 
de 6 a 11 nos saluda = Good Morning
de 12 a 16 nos saluda = Good Afternoon
de 17 a 19 nos saluda = God Evening
de 20 a 23 nos saluda = Good Night
Trabajaremos con 24 horas
*/

let horaDia = 9;
let mensaje;

if (horaDia >= 6 && horaDia <= 11) {
    mensaje = "Good morning!";
} else if (horaDia >= 12 && horaDia <= 16) {
    mensaje = "Good afternoon!";
} else if (horaDia >= 17 && horaDia <= 19) {
    mensaje = "Good evening!";
} else if (horaDia >= 20 && horaDia <= 23) {
    mensaje = "Good night!";
} else {
    console.log("Error, Valor incorrecto");
}

console.log(`La hora ingresada es ${horaDia}, ${mensaje}`);

// Estructura switch con el break.
// Ejercicio 1 = estación del año pero ahora con el switch.
switch(mes) {
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case  5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        console.log("Valor Incorrecto");
}

console.log("Estacion: "+estacion)

// Ejercicio 2 = Hora del dia pero ahora con switch.
/* 
de 6 a 11 = Good morning
de 12 a 16 = Good afternoon
de 17 a 19 = God evening
de 20 a 23 = Good night
*/

switch(horaDia) {
    case 6: case 7: case 8: case 9: case 10: case 11:
        saludo = "Good Morning desde switch";
        break;
    case 12: case 13: case 14: case 15: case 16:
        saludo = "Good Afternoon desde switch";
        break;
    case 17: case 18: case 19:
        saludo = "Good Evening desde switch";
        break;
    case 20: case 21: case 22: case 23:
        saludo = "Good Night desde switch";
        break;
    default:
        console.log("Error, Valor Incorrecto");
}

console.log(saludo);

/*
const se utiliza para vlaores constantes que no pueden ser reasignadas
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2023;
//console.log(fechaNacimiento); //Solo se ejecuta el console anterior

//Evitar repetir tu código

let days= 5;

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
        console.log('Error en el ingreso del dia de la semana');
        break;
}

//Opción mejorada

let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
function getDays(n){
    if(n < 1 || n> 7){
        throw new Error('out of range')
    }
    return days2[n-1];
}
console.log(getDays(3));

