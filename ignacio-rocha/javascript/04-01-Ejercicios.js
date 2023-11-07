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

//evitar repetir tu codigo
//dry dont repeat yourself
//let days=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"];
let days=5;
switch (days) {
    case 1:
        console.log('hoy es: lunes');
        break;
    case 2:
        console.log('hoy es: martes');
        break;    
    case 3:
        console.log('hoy es: miercoles');
        break;
    case 4:
        console.log('hoy es:jueves');
        break;
    case 5:
        console.log('hoy es: viernes');
        break;
    case 6:
        console.log('hoy es:sabado');
        break;
    case 7:
        console.log('hoy es: domingo');
        break;
    default:
        break;
}
let days2=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"];

function getDay(n){
    if (n<1 || n>7){
        throw new Error ('out of range');
    }
    return days2(n-1);
}
console.log(getDay(3));
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

/*
hacer un ejercicio similar al que esta hecho, pero ahora con los meses del año,
debes hacerlo con la estructura switch y luego con la funcion en la opcion mejorada
*/
let month=11;
switch (month) {
    case 1:
        console.log("es enero");
        break;
    case 2:
        console.log("es febrero");
        break;
    case 3:
        console.log("es marzo");
        break;
    case 4:
        console.log("es abril");
        break;
    case 5:
        console.log("es mayo");
        break;
    case 6:
        console.log("es junio");
        break;
    case 7:
        console.log("es julio");
        break;
    case 8:
        console.log("es agosto");
        break;
    case 9:
        console.log("es septiembre");
        break;
    case 10:
        console.log("es octubre");
        break;
    case 11:
        console.log("es noviembre");
        break;
    case 12:
        console.log("es diciembre");
        break;
    default:
        console.log("error en el ingreso del mes del año");
        break;
}

//opcion mejorada
let month2=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"];
function getMonth(n){
    if(n<1 || n>12){
        throw new Error('out of range');

    }
    return month2(n-1);
}
console.log(getMonth(1));
