// Ejercicio 1 = estación del año.

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

console.log(`El mes ingresado corresponde a la estación de ${estacion}`);

// Ejercicio 2 = hora del dia.
/* 
de 6 a 11 = Good Morning
de 12 a 16 = Good Afternoon
de 17 a 19 = God Evening
de 20 a 23 = Good Night
*/

let hora = 17;
let saludo;

if (hora >= 6 && hora <= 11) {
    saludo = "Good Morning!";
} else if (hora >= 12 && hora <= 16) {
    saludo = "Good Afternoon!";
} else if (hora >= 17 && hora <= 19) {
    saludo = "Good Evening!";
} else if (hora >= 20 && hora <= 23) {
    saludo = "Good Night!";
} else {
    console.log("Error, Valor Incorrecto");
}

console.log(`La hora ingresada es ${hora}, ${saludo}`);

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
        console.log("Error, Valor Incorrecto");
}

console.log(estacion)

// Ejercicio 2 = hora del dia pero ahora con switch.
/* 
de 6 a 11 = Good Morning
de 12 a 16 = Good Afternoon
de 17 a 19 = God Evening
de 20 a 23 = Good Night
*/

switch(hora) {
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