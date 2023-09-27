/*Ejercicio 9: Pedir el día, mes y año de una fecha e
indicar si la fecha es correcta. Suponiendo que
todos los meses son de 30 días*/
package clase5;

import java.util.Scanner;

public class ejercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dia,mes,anio;
        System.out.println("digite el dia: ");
        dia=Integer.parseInt(sc.nextLine());
        System.out.println("digite el mes: ");
        mes=Integer.parseInt(sc.nextLine());
        System.out.println("digite el año: ");
        anio=Integer.parseInt(sc.nextLine());
                if((dia!=0)&&(dia<=30)){
            if((mes!=0)&& (mes<=12)){
                if((anio!=0)&&(anio<=2022)){
                    System.out.println("LA fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                    System.out.println("fecha incorrecta, año incorrecto");
                }
            }
            else{
                System.out.println("fecha incorrecta, mes incorrecto");
            }
        }
        else{
            System.out.println("fecha incorrecta, dia incorrecto");
        }
    }
}
