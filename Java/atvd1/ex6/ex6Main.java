// linha de importação do pacote
package atvd1.ex6;

// linha de importação do scanner
import java.util.Scanner;

// criação da classe principal
public class ex6Main {
    public static void main(String[] args){

        // linha de criação do objeto Lampada
        ex6Lampada a = new ex6Lampada();

        // linha de criação do Scanner
        Scanner sc = new Scanner(System.in);

        // linha que chama o metodo principal
        a.operacao();

        // bloco de encerramento
        System.out.print("Aperte Enter para encerrar...");
        sc.nextLine();
    }
}
