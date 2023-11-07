//Hacer un ejercicio similar a1 que esta hecho, pero ahora con los
//meses del año, debes hacerlo con la estructura switch y luego con
// la función en la opción mejorada
let monthNumber = 5;
let monthName;

switch (monthNumber) {
  case 1:
    monthName = "Enero";
    break;
  case 2:
    monthName = "Febrero";
    break;
  case 3:
    monthName = "Marzo";
    break;
  case 4:
    monthName = "Abril";
    break;
  case 5:
    monthName = "Mayo";
    break;
  case 6:
    monthName = "Junio";
    break;
  case 7:
    monthName = "Julio";
    break;
  case 8:
    monthName = "Agosto";
    break;
  case 9:
    monthName = "Septiembre";
    break;
  case 10:
    monthName = "Octubre";
    break;
  case 11:
    monthName = "Noviembre";
    break;
  case 12:
    monthName = "Diciembre";
    break;
  default:
    monthName = "Error en el ingreso del número de mes.";
}

console.log(monthName);

//version mejorada
let monthNumber2 = 5;

function getMonthName(n) {
  let months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
  if (n < 1 || n > 12) {
    throw new Error("Número de mes fuera de rango.");
  }
  return months[n - 1];
}

console.log(getMonthName(monthNumber2));
