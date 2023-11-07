// Ejercicio 1: Calcular estación del año
let mes = 7;
let estacion; 
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Inexistente";
}
console.log("La estación es "+estacion);

// Ejercicio 2: Ejercicio hora del día
/*
de 6 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good Afternoon
de 17 a 19 nos saluda: Good evening
de 20 a 23 nos saluda: Good night
Trabajaremos con 24 horas
*/
let horaDia = 20;
let mensaje;
if(horaDia >= 6 && horaDia <=11){
    mensaje = "Good morning";
}
else if(horaDia >= 12 && horaDia <=16){
    mensaje = "Good Afternoon";
}
else if(horaDia >= 17 && horaDia <=19){
    mensaje = "Good evening";
}
else if(horaDia >= 20 && horaDia <=23){
    mensaje = "Good night";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje);

// Estructura switch(la sintaxis es igual a java)
switch(mes){ // No solo se pueden utilizar números, también cadenas
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
        estacion = "Inexistente"
}
console.log("La estación es "+estacion)

// Evitar repetir tu código
// Dry don't repeat yourself


let days = 1;
switch (days){
    case 1:
        console.log("Hoy es Lunes")
        break;
    case 2:
        console.log("Hoy es Martes")
        break;
    case 3:
        console.log("Hoy es Miércoles")
        break;
    case 4:
        console.log("Hoy es Jueves")
        break;
    case 5:
        console.log("Hoy es Viernes")
        break;
    case 6:
        console.log("Hoy es Sábado")
        break;
    case 7:
        console.log("Hoy es Domingo")
        break;
    default:
        console.log("Error en el ingreso del día de la semana.");
        break;
}

// Esta es la opción mejorada

let days2 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
function getDay(n){
    if(n < 1 || n > 7){
    throw new Error("Out of range");
    }
    return days2[n-1];
}
console.log(getDay(5));

// Hacer un ejercicio similar al que está hecho, pero ahora con los
// meses del año, debes hacerlo con la estructura switch y luego con
// la función en la opción mejorada

let month = 11;
switch (month) {
    case 1:
        console.log("Es enero.");
        break;
    case 2:
        console.log("Es febrero.");
        break;
    case 3:
        console.log("Es marzo.");
        break;
    case 4:
        console.log("Es abril.");
        break;
    case 5:
        console.log("Es mayo.");
        break;
    case 6:
        console.log("Es junio.");
        break;
    case 7:
        console.log("Es julio.");
        break;
    case 8:
        console.log("Es agosto.");
        break;
    case 9:
        console.log("Es septiembre.");
        break;
    case 10:
        console.log("Es octubre.");
        break;
    case 11:
        console.log("Es noviembre.");
        break;
    case 12:
        console.log("Es diciembre.");
        break;
    default:
        console.log("Error en el ingreso del mes del año.");
        break;
}

// Esta es la opción mejorada
let month2 = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error("Out of range");
    }
    return month2[n-1];
}
console.log(getMonth(11));