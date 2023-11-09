//Ejercicio para encontrar números pares e impares

let parImpar = 10;
if(parImpar % 2 == 0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}

//Ejercicio: es mayor de edad

let edad = 15, adulto = 18;
if( edad >= adulto ){
    console.log('Es una persona adulta');
}
else{
    console.log('Es una persona menor de edad')
}

//Ejercicio: Dentro de un rango

let dentroRango = 5; //Aquí vamos a ir cambiando el valor
let valMin = 0; valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log('Está dentro del rango establecido');
}
else{
    console.log('Está fuera del rango establecido');
}
