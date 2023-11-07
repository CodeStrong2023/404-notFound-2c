
// Evitar repetir tu código
// Dry don't repeat yourself

days = 4;
switch(days) {
    case 1:
        console.log("Hoy es Lunes");
        break;
    case 2:
        console.log("Hoy es Martes");
        break;
    case 3:
        console.log("Hoy es Miercoles");
        break;
    case 4:
        console.log("Hoy es Jueves");
        break;
    case 5:
        console.log("Hoy es Viernes");
        break;
    case 6:
        console.log("Hoy es Sabado");
        break;
    case 7:
        console.log("Hoy es Domingo");
        break;
    default:
        console.log("Error en el ingreso del dia de la semana");
        break;

}

// Opción Mejorada.
let days2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];

function getDay(n) {
    if (n < 1 || n > 7) {
        throw new Error("out of range"); // Si esta fuera de rango damos una alarte sobre el error.
    }
    return days2[n-1];
}

console.log(getDay(9))