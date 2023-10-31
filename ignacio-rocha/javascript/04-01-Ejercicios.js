//ampliando el uso de var let y const
/*con var puedes reasignar en cualquier momento
esta forma parte del ambito global un es que se sobreescriba
*/
var nombre="ariel";
nombre="osvaldo";
console.log(nombre);//aqui no lee el dato en la funcion
if (true){
    var edad=34;
    console.log(edad);

}
console.log(edad);//en la funcion funciono correctamente, en la estructura if fallo
/*let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque*/
function saludar2(){
    let nombre2="ariel";
    console.log(nombre2);
}
console.log(nombre2);
if(true){
    let edad=33;
    console.log(edad);
}
console.log(edad2);

//const se utiliza para valores constantes que no
//pueden ser reasignadas
const fechaNacimiento=2006;
console.log(fechaNacimiento);
fechaNacimiento=2003;
console.log(fechaNacimiento);//solo se ejecuta el console anterior

//Ejercicio 1: Calcular estacion del año
let mes=4;
let estacion;//undefined
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