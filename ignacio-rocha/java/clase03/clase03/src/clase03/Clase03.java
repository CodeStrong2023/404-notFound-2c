package clase03;

import java.util.Scanner;

public class Clase03 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner (System.in);
        int numero;
        System.out.println("ingrese un numero: ");
        numero=Integer.parseInt(scanner.nextLine());
        while(numero!=0){
            if(numero%2==0){
                System.out.println("el numero ingresado "+numero+" es PAR");
                
            }
            else{
                System.out.println("el numero ingresado "+numero+" es IMPAR");
            }
            System.out.println("digite otro numero: ");
            numero=Integer.parseInt(scanner.nextLine());
            
        }
        
    }
    
}
