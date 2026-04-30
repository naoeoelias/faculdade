// linha de importação do pacote
package atvd1.ex4;

// linha de importação do scanner
import java.util.Scanner;

// criação da classe principal
public class ex4Main {
    public static void main(String[] args){

        // linha de criação do objeto ContaBancaria
        ex4ContaBancaria c = new ex4ContaBancaria();

        // linha de criação do Scanner
        Scanner sc = new Scanner(System.in);

        // linha que chama o metodo principal
        c.operacao();

        // bloco de encerramento
        System.out.print("Aperte Enter para encerrar...");
        sc.nextLine();
    }
}
