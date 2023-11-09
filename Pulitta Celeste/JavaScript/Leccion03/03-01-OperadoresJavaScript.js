//Ejercicio para encontrar numeros pares
let parImpar = 10;
if(parImpar % 2 == 0){
    console.log("Es un numero PAR");
}
else{
    console.log("Es un numero IMPAR");
}

//Ejercicio: es mayor de edad
let edad = 14, adulto = 18;
if(edad >= adulto){
    console.log("Usted es una persona adulta")
}
else{
    console.log("Usted es una persona menor de edad")
}

//Ejercicio dentro de un rango
let dentroRango = 10; //aqui vamos cambiando el valor
let valMin = 0, valMax= 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido");
}
else{
    console.log("Esta fuera del rango establecido");

}

//Ejercicio si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("el padre no puede asistir al juego de su hijo")
}

//Operador ternario 
let resultado2 = 3 > 2 ?"verdadero" : "falso";
console.log(resultado2)
let numero = 12;
resultado2 = numero % 2 == 0 ? "Es un numero PAR" : "ES un numero IMPAR";
console.log(resultado2)

//Convertir String a Number
let miNumero= "21"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); // ewsta es una funcion
console.log(typeof edad2);
//Funcion isNan
if(isNaN(edad2)){
    console,log("Esta variable no contiene solo numeros")
}
else{
    if(edad2 >= 18){
    console.log("Puede votar")
    }
    else{
        console.log("Muy joven para votar");
    }
}
//Operador ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3)





//Ampliando el uso de var let y const
/*
Con var puedes reasignar en cualquier momento
esta forma parte del ambito global
un error es que se sobreescriba
*/
/*
var nombre = "Ariel";
nombre = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre  = "Natalia";
    console.log(nombre);
}
console.log(nombre); //El problema es que aqui no lee el dato de la function

if(true){
    var edad= 34;
    console.log(edad);
}
console.log(edad); //en la funion funciono correctamente, en la estructura fallo
*/