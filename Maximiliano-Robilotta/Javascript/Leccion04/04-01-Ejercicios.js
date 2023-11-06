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
console.log("La estacion seleccionada es "+estacion);

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
    mensaje = "Incorrecto";
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
console.log("La estacion seleccionada es "+estacion)