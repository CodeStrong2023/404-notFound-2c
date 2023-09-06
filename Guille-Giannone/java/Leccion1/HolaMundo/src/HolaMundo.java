
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        /*System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable );
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);*/

        //Var - inferencia de tipo java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //para escribir esta funcion tecleamos soutv+tab
        //Para ejecutar el programa usar shift + f6
        //Reglas para definir una variable en Java
        
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo +" "+ usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(usuario +" "+ (a+b));
        //Ejercicios: caracteres especiales en Java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n"+nombre);//Diagonal inversa(alt+92) + n (salto de linea)
        System.out.println("Tabulador: \t"+nombre);//Diagonal inversa + t (sangria o tabulador)
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroseso: \b\b"+nombre);//nos borra un espacio antes
        System.out.println("Comillas simples: \'"+nombre+"\'");//en este teclado la comilla simple es alt+39
        System.out.println("Comillas Dobles: \""+nombre+"\"");*/
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su Nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/
 /*byte numEnteroByte = (byte)127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:"+Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+Byte.MAX_VALUE);
        
        short numEnteroShort = 10;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("El valor minimo del Short: "+Short.MIN_VALUE);
        System.out.println("EL valor maximo del Short: "+Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("El valor minimo de Int: "+Integer.MIN_VALUE);
        System.out.println("El valor maximo de Int: "+Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("El valor minimo de long: "+Long.MIN_VALUE);
        System.out.println("El valor maximo de long: "+Long.MAX_VALUE);*/
 /*float numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de float es: "+Float.MIN_VALUE);
        System.out.println("El valor maximo de float es: "+Float.MAX_VALUE);
        
        double numDouble = 10;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de double es: "+Double.MIN_VALUE);
        System.out.println("El valor maximo de double es: "+Double.MAX_VALUE);*/
        //Inferencia de tipos var y tipos primitivos
        /*var numEntero = 20;
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //Automaticamente con el punto decimal se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("NumDouble = " + numDouble);*/
        //Tipos primitivos char
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024';//Indicamos a Java la asignacion con el codigo Unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Utilizamos el valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';//Un caracter especial podemos copiar y pegar desde unicode.
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024';//Indicamos a Java la asignacion con el codigo Unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; //Aqui sin poner (char) el valor lo va a tomar como int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$';//Un caracter especial podemos copiar y pegar desde unicode.
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'g';
        System.out.println("caracterChar = " + caracterChar);*/
        //Tipos Primitivos tipo booleanos
        /*var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if (varBool) {
            System.out.println("La bandera es verde");
        }
        else {
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo - Es mayor de edad?
        
        var edad =20; // Literal, tener presente la inferencia de tipos
        //var adulto = edad >= 18; //Esta es una expresion booleana
        if(edad >=18) {
            System.out.println("Eres mayor de edad");    
        }
        else  {
            System.out.println("Eres menor de edad");
        }*/
        // COnversion de tipos primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad+1));
//        
//        var valorPI = Double.parseDouble("3.1416");
//        System.out.println("valorPI = " + valorPI);
//    
//        Pedir un valor
        var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);

        //Conversion de tipos primitivos en Java parte 2
        /*var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        var fraseChar = "Programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
 /*int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion );
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion= " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la division= " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 de la division = " + solucion2);
        
        solucion = num1 % num2;//Guarda el residuo de la division
        System.out.println("solucion = " + solucion); 
        
        if (num2 % 2 == 0)
            System.out.println("Es un numero Par");
        else
            System.out.println("Es un numero Impar");*/
 /*int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; // Una Operacion
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; //Es la forma simplificada de poner var num1 = varNum1 + 1
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 -= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 *= 2;
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 /= 2;
        System.out.println("varNum2 = " + varNum2);
        
        varNum2 %= 2;
        System.out.println("varNum2 = " + varNum2);*/
        //Operadores Unarios: Cambio de signo
        /*var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); // El resultado sera un numero negativo
        
        //Operador de negacion
        var varC = true;//Esta literal en Java por defecto es de tipo boolean
        var varD = !varC;//Aqui esta invertido el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores Unarios de Incremento: Preincremento
        var varE = 9;// se va a modificar su valor
        var varF = ++varE;//simbolo antes de la variable
        //Primero se incrementa la variable despues se usa su valor
        System.out.println("varE = " + varE);//Se incrementa en la unidad
        System.out.println("varF = " + varF);//Va a sumar uno
        
        //Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++;//Primero el valor de la variable, despues el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores Unarios de Decremento: predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);//La variable ya tiene asignado el decremento
        System.out.println("varJ = " + varJ);
        //Postdecremento
        var varK = 8;
        var varL = varK--;//Primero el valor de la variable,
        System.out.println("varK = " + varK);//Aqui va a decrementar en 1
        System.out.println("varL = " + varL);*/
 /* var aNum = 5;
        var bNum = 5;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        var cadenaA = "Hello";
        var cadenaB = "Bye Bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);

        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);

        var gVar = aNum >= bNum;
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("El numero es Par");
        } else {
            System.out.println("El numero es Impar");
        }
        var edad = 30;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }*/
        //Operadores condicionales And
        /*var valorA = 5;
        var valorMinimo = 0;//creamos un rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;
        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        //condicional or
        var vacaciones = true;
        var diaLibre = false;
        if (vacaciones || diaLibre)
            System.out.println("Papá puede asistir al juego de su hijo");
        else
            System.out.println("Papá no puede asistir al juego de su hijo");*/
        
        // Operador Ternario
        var resultadoT = (5 > 4) ? "verdadero" : "falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 6;
        resultadoT =  (numeroT % 2 == 0)? "Es Par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);
        
        //Prioridad de los operadores
        /*var x = 5;
        var y = 10;
        var z = ++ x + y --;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16
        
        var solucionAritmetica = 4 + 5 * 6 / 3;// 4 + ((5*6)/3)= 30/3=10+4
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        solucionAritmetica = (4+5)*6/3; // 9*6=54/3=18
        System.out.println("solucionAritmetica = " + solucionAritmetica);*/
        
        //Ejercicio sacar Area y perimetro de un rectangulo
        
        var altoRectangulo = 5;
        var anchoRectangulo = 10;
        var perimetro = (altoRectangulo + anchoRectangulo)*2;
        var area = altoRectangulo * anchoRectangulo;
        System.out.println("perimetro = " + perimetro);
        System.out.println("area = " + area);
        
        //Ejercicio mostrar el numero mas grande
        
        Scanner scanner = new Scanner(System.in);
        int num1,num2,salida;
        System.out.println("Ingrese el primer numero");
        num1=scanner.nextInt();
        System.out.println("Ingrese el segundo numero ");
        num2=scanner.nextInt();
        salida = (num1>num2)?num1:num2;
        System.out.println("El numero mayor es: "+salida);
        
        
    }

}
