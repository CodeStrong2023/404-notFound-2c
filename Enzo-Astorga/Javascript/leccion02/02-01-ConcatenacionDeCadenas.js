var nombre = "José";
var apellido = " Montes";
var nombreCompleto = nombre+" "+apellido; // Primera Concatenación
console.log(nombreCompleto);
var nombreCompleto2 = "Enzo"+" "+"Astorga"; // Seguna Concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izq a der siguiendo la cadena lee el número como String
console.log(juntos);
juntos = nombre + 78 + 17; // Aquí se puede diferenciar a través de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre; // Primero suma, luego concatena.
console.log(juntos);

nombre += apellido; // Tercera Concatenación usando el operador simplificado
console.log(nombre);