//Ejercicio 1: Calcular estacion del año
let mes=4;
let estacion;
if (mes==1|| mes==2||mes==12){
    estacion="verano";
}
else if(mes==3 || mes==4 || mes==5){
    estacion="otoño";
}
else if(mes==6||mes==7||mes==8){
    estacion="invierno";
}
else{
    estacion="valor incorrecto";
}
console.log("el valor corresponde a la estacion de: "+estacion);

//ejercicio 2: hora del dia
let horaDia=9;
let mensaje;
if (horaDia>=6 && horaDia<=11){
    mensaje="good morning";
}
else if(horaDia>=12 && horaDia<=16){
    mensaje="good afternoon";
}
else if(horaDia>=17 && horaDia<=19){
    mensaje="good evening";
}
else if(horaDia>=20 && horaDia<=23){
    mensaje="good night";
}
else{
    mensaje="valor incorrecto";
}
console.log(mensaje);
//estructura switch: (la sintaxis es igual a java)
switch(mes){//no solo se pueden utilizar numero, tambien cadenas
    case 1:case 2:case 12:
        estacion="verano";
        break;
    case 3: case 4: case 5:
        estacion="otoño";
        break;
    case 6: case 7: case 8:
        estacion="invierno";
        break;
    case 9: case 10: case 11:
        estacion ="primavera";
        break;
    default:
        estacion="valor incorrecto";

}
console.log("bienvenido a la estacion de: "+estacion);

//evita repetir tu codigo
let days = 1
switch (days){
    case 1:
        console.log("hoy es lunes");
        break;
    case 2:
        console.log("hoy es martes");
        break;
    case 3:
        console.log("hoy es miercoles");
        break;
    case 4:
        console.log("hoy es jueves");
        break;
    case 5:
        console.log("hoy es viernes");
        break;
    case 6:
        console.log("hoy es sabado");
        break;
    case 7:
        console.log("hoy es domingo");
        break;
    default:
        console.log("Error en el ingreso del día de la semana.");
        break
}
let days2 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
function getDay(n){
    if(n < 1 || n > 7){
    throw new Error("Out of range");
    }
    return days2[n-1];
}
console.log(getDay(7));

