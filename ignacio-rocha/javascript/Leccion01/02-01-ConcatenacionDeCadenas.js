var nombre="jose";
var apellido="Montes";
var nombreCompleto=nombre+" "+apellido;//primera concatenacion
console.log(nombreCompleto); 
var nombreCompleto2="ariel"+" "+"betancud";//segunda concatenacion
console.log(nombreCompleto2);
var juntos=nombre+219;//lee de izq a der siiguiendo la cadena lee el numero como str
console.log(juntos);
juntos=nombre+78+17;//aqui se puede diferenciar a traves de los parentesis
console.log(juntos);
juntos=78+17+nombre;
console.log(juntos);

nombre+=apellido; //tercera concatenacion usando el operador simplificado
console.log(nombre);