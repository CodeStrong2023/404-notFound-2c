
import java.util.Scanner;

public class holaMundo {

    public static void main(String[] args) {
        /*System.out.println("Hola mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
         */
        //Var - Inferencia de tipos en Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tab

        //Ej1
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        //Ej2
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));

        //Ejercicio caracteres especiales con Java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre);// \n da un salto de linea
        System.out.println("Tabulador: \t" + nombre);// \t espacio ancho o tabulador
        System.out.println("\t\t.:MENÚ:.");
        System.out.println("Retroceso: \b \b" + nombre);//Caracter de retroceso
        System.out.println("Comillas simples: \'" + nombre + "\'");//Comillas simples
        System.out.println("Comillas dobles: \"" + nombre+"\"");//Comillas dobles*/

        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine ();
        System.out.println("Resultado: " + titulo2 +" " + usuario2);*/
 /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor mínimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor máximo del Byte: "+ Byte.MAX_VALUE);
        
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor mínimo del Short: "+ Short.MIN_VALUE);
        System.out.println("Valor máximo del Short: "+ Short.MAX_VALUE);


        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor mínimo del Int: "+ Integer.MIN_VALUE);
        System.out.println("Valor máximo del Int: "+ Integer.MAX_VALUE);
        
        
        long numEnteroLong = 10;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor mínimo del Long: "+ Long.MIN_VALUE);
        System.out.println("Valor máximo del Long: "+ Long.MAX_VALUE);
        
        
        float numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor mínimo del Float: "+ Float.MIN_VALUE);
        System.out.println("Valor máximo del Float: "+ Float.MAX_VALUE);
        
        
        double numDouble = 10;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor mínimo del Double: "+ Double.MIN_VALUE);
        System.out.println("Valor máximo del Double: "+ Double.MAX_VALUE);*/
        //Inferencia de tipos var y tipos primitivos
        /*var numEntero = 20; //Las literales sin punto automáticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; // Automáticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat); 
        var numDouble= 10.0;
        System.out.println("numDouble = " + numDouble);*/
        //Tipos Primitivos Char
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; // Indicamos  Java la asignación con el código Unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; // Valor decimal del jeugo de caracteres Unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; // Un caracter especial, podemos copiar y pegar desde Unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; // Indicamos  Java la asignación con el código Unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; // Valor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; // Un caracter especial, podemos copiar y pegar desde Unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar); */
        //Tipos primitivos tipos booleanos
        /*var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es verde");
                    }
        else{
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo: ¿Es mayor de edad?
        var edad = 18; //Literal tener presente la inferencia de tipos
        //var adulto = edad >= 18; //Expresión booleana
        if (edad >=18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        } */
        //Conversión de tipos primitivos
//      var edad = Integer.parseInt("20");
//      System.out.println("edad = " + (edad + 1));
//      var valorPI = Double.parseDouble("3.1416");
//      System.out.println("valorPI = " + valorPI);
        //Pedir un valor
//      ?  var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad: ");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);
        //Conversión de tipos primitivos en Java parte 2
        /*var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.print("Digite un carácter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
 /*int num1 = 5, num2 = 4;
      var solucion = num1 + num2;
      System.out.println("solución de la suma = " + solucion);
      
      solucion = num1 - num2;
        System.out.println("solución de la resta = " + solucion);
        
      solucion = num1 * num2;
        System.out.println("solución de la multiplicación = " + solucion);
        
      solucion = num1 / num2;
        System.out.println("solución de la división = " + solucion);
        
      var solucion2 = 3.4D / num2;
        System.out.println("solucion2 resultado de la división = " + solucion2);
        
      solucion = num1 % num2; // Guarda el residuo enterp de la división
        System.out.println("solucion = " + solucion);
        
      if (num2 % 2 == 0)
            System.out.println("Es par");
      else 
            System.out.println("Es impar"); */
        // Práctica de operadores de asignación
        /* int varNum1 = 1, varNum2 = 4;
    var varNum3 = varNum1 + 6 - varNum2; // Una operación
    System.out.println("varNum3 = " + varNum3);
    
    varNum1 += 1; // varNum1 = varNum1 + 1;
    System.out.println("varNum1 = " + varNum1);
    
    // -=   *=  /=  %=
    
    varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
    varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
    varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
    varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);*/
 /*
    //Operadores Unarios: Cambio de Signo
    var varA = 7;
    var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); // El resultado será negativo
        
        // Operador de Negación (Para variables de tipo boolean)
        var varC = true; // Esta literal por default en Java es de tipo boolean
        var varD = !varC; // Aquí está invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = "+ varD);
        
        //Operadores Unarios de Incremento
        var varE = 9; //Se va a modificar su valor
        var varF = ++varE; // Simbolo antes de la variables
        //Primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE); // Se incrementa en la unidad
        System.out.println("varF = " + varF); // Va a sumar uno
        
        //Postincremento(el simbolo va después de la variable)
        var varG = 3;
        var varH = varG++;
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores Unarios de decremento: predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("VarI = " + varI); // La variable ya está con decremento
        System.out.println("VarJ = " + varJ);
        
        //Postdecremento
        var varK = 8;
        var varL = varK--; // Primero el valor de la variable, luego queda el decremento
        System.out.println("varK = " + varK); // Aquí va a decrementar en 1
        System.out.println("varL = " + varL); */
 
 /*
        //Operadores de igualdad y relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);

        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);

        var gVar = aNum != bNum; // Se pueden utilizar > >= < <= == !=
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("El número es Par.");
        } else {
            System.out.println("El número es Impar.");
        }
        
        var edad = 30;
        var adulto = 18;
        if(edad >= adulto){
            System.out.println("Es mayor de edad.");
        }
        else{
            System.out.println("Es menor de edad.");
        }
        
        */
 
        /*
        //Operadores condicionales AND
        var valorA = 7;
        var valorMinimo = 0; //rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;
        if(respuesta){
            System.out.println("Está dentro del rango establecido.");
        }
        else{
            System.out.println("Está fuera del rango establecido.");
        }
        
        //Operadores condicionales OR
        var vacaciones = true;
        var diaLibre = false;
        if(vacaciones || diaLibre){
            System.out.println("Papá puede asistir al juego de su hijo.");
        }
        else{
            System.out.println("Papá no puede asistir al juego de su hijo.");
        } */
 
        /*
        //Operadores Ternarios
        var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es Par" : "Es Impar";
        System.out.println("ResultadoT = " + resultadoT);
        */
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x); //6
        System.out.println("y = " + y); //9
        System.out.println("z = " + z); //16
        
        var solucionAritmetica = 4 + 5 * 6 / 3; // 4 + ((5*6) / 3) = 30 / 3 = 10 + 4 = 14
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3; // (4 + 5) = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        
    }
}
