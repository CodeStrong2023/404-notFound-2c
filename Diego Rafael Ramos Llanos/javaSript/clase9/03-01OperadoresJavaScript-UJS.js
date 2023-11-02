//Ejercicio para encontrar numero pares
var parImpar = 10;
if (parImpar % 2 === 0) {
    console.log(parImpar + " es un número par.");
} else {
  console.log(parImpar + " es un número impar.");
}
//ejercicio:ejercicio es mayor de edad
var edad = 18
if (edad >= 18){
    console.log("Es mayor de edad,edad de : "+edad);
}else{
    console.log("Es menor de edad,edad de : "+edad);
}
//Ejercicio:Dentro de un rango
let dentroRango = 1;
let valMin = 0, valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}
//Ejercicio:Si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = false;
if (vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre no puede asistir al juego de su hijo")
}
//Operador Ternario
let resultado2 = 3 > 2 ? "verdadero" : "falso";
console.log(resultado2);
let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un numero PAR" : "Es un numero IMPAR";
console.log(resultado2); 

//Convertir String a Number
let miNumero = "12"; //Es cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); //Es una funcion
console.log(typeof edad2);

//Funcion isNaN
if(isNaN(edad2)){ //No es un numero : is Not a Number
    console.log("Esta variable no contiene solo numeros")
}
else{
    if (edad2 >= 18){
        console.log("Puede Votar")
}
    else{
        console.log("Muy joven para Votar -----")
    }
}

//Operador Ternario
let resultado3 = edad2 >= 18 ? "Puede Votar" : "Muy joven para Votar";
console.log(resultado3);

