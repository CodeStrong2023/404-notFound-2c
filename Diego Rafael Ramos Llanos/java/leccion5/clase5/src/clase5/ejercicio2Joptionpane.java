/*Ejercicio 9: Pedir el día, mes y año de una fecha e
indicar si la fecha es correcta. Suponiendo que
todos los meses son de 30 días*/
package clase5;
import javax.swing.JOptionPane;

public class ejercicio2Joptionpane {
    public static void main(String[] args) {
        int dia,mes,anio;
        dia=Integer.parseInt(JOptionPane.showInputDialog("digite el dia: "));
        mes=Integer.parseInt(JOptionPane.showInputDialog("digite el mes: "));
        anio=Integer.parseInt(JOptionPane.showInputDialog("digite el año: "));
                if((dia!=0)&&(dia<=30)){
            if((mes!=0)&& (mes<=12)){
                if((anio!=0)&&(anio<=2022)){
                    JOptionPane.showMessageDialog(null,"LA fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                     JOptionPane.showMessageDialog(null,"fecha incorrecta, año incorrecto");
                }
            }
            else{
                JOptionPane.showMessageDialog(null,"fecha incorrecta, mes incorrecto");
            }
        }
        else{
            JOptionPane.showMessageDialog(null,"fecha incorrecta, dia incorrecto");
        }

    }
}
