import javax.swing.*;
import java.util.Scanner;

public class EjerciciosCiclos09JOptionPane {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int dia, mes, anio;

        dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el dia: "));

        mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));

        anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año: "));

        if ((dia != 0) && (dia <= 30) ) {
            if ((mes != 0) && (mes <= 30)){
                if ((anio != 0) && (anio <= 2023)) {
                    JOptionPane.showMessageDialog(null,"La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null,"Error, año no valido");
                }
            } else {
                JOptionPane.showMessageDialog(null,"Error, mes no valido");
            }
        } else {
            JOptionPane.showMessageDialog(null,"Error, dia no valido");
        }
    }
}
