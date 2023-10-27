// Si el padre puede asistir la juego de su hijo.

const vaciones = false, diaFranco = true;

if (vaciones || diaFranco === true) {
    console.log("Si podra asistir al partido de su hijo");
} else {
    console.log("No podra asistir al partido, tiene que trabajar");
}

// Operador Ternario.
let resultado = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado);

let numero = 9;
resultado = numero % 2 === 0 ? "Número Par" : "Número Impar";
console.log(resultado);

// Converit String a Number.
let miNumero = "20"; // Número de tipo String.
console.log(typeof miNumero); 

let edad = Number(miNumero); // Lo convertimos a tipo Number.
console.log(edad);

// Ejercicio: Es mayor de edad.

// Ejercicio con el condicional if
if (isNaN(edad)) {  // Función isNaN = no es un número
    console.log("Esta variable no es un número")
} else {
    if (edad >= 18) {
            console.log("Puede votar");
        } else {
            console.log("Muy joven para votar");
        }
}


// Ejercicio con el operador ternario
let resultado2 = edad >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado2)