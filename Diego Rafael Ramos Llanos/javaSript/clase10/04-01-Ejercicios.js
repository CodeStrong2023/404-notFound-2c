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