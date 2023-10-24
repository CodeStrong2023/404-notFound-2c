//ejercicio para encontrar numeros pares e impares
let parImpar=10;
if(parImpar%2==0){
	console.log("es un numero PAR");
}
else{
	console.log("es un numero IMPAR");

}
//ejercicio: es mayor de edad
let edad=18,adulto=18;
if(edad>=adulto){
	console.log("Usted es una persona adulta");
}
else{
	console.log("Usted es una persona menor de edad");
}
//ejercicio: dentro de un rango
let dentroRango=5; //aqui vamos a ir cambiando el valor
let valMin=0,valMax=10;
if(dentroRango>=valMin && dentroRango<=valMax){
	console.log("esta dentro del rango establecido")
}
else{
	console.log("esta fuera del rango establecido")
}

//ejercicio: si el padre puede asistir al juego de su hijo
let vacaciones= false,diaDescanso=false;
if(vacaciones||diaDescanso){
	console.log("el padre puede asistir al juego de su hijo")
}
else{
	console.log("el padre no puede asistir al juego de su hijo")
}

//operador ternario
let resultado2=3>2?"verdadero":"falso";
console.log(resultado2);
let numero=9;
resultado2=numero%2==0?"es un numero PAR":"es un numero IMPAR";
console.log(resultado2)

//convertir string a number
let miNumero="10";//es una cadena
console.log(typeof miNumero)
let edad=number(miNumero) //esta es una funcion
console.log(typeof miNumero)
//funcion isNaN
if (isNaN(edad2)){//no es un numero=is not a number (devuelve un resultado booleano)
	console.log("esta variable no contiene solo numeros")
}
if (edad>=18){
	console.log("puede votar");
}
else{
	console.log("es muy joven para votar");
}

let resultado3=edad2>=18?"puede votar":"muy joven para votar";
console.log(resultado3);

