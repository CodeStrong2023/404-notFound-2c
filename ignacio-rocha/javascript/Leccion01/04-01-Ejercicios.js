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

