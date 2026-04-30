// linha de importação do pacote
package atvd1.ex2;

// linha de importação do scanner
import java.util.Scanner;

// criação da classe principal
public class ex2Main {
    public static void main(String[] args) {

        // linha de criação do objeto scanner
        Scanner sc = new Scanner(System.in);

        // bloco de criação dos produtos
        ex2Produto p1 = new ex2Produto();
        ex2Produto p2 = new ex2Produto();
        ex2Produto p3 = new ex2Produto();

        // bloco de inserção de dados do primeiro produto
        System.out.println("Digite o nome do primeiro produto:");
        p1.nome = sc.nextLine();
        System.out.println("Digite o preco do primeiro produto:");
        p1.preco = Double.parseDouble(sc.nextLine());

        // bloco de inserção de dados do segundo produto
        System.out.println("Digite o nome do segundo produto:");
        p2.nome = sc.nextLine();
        System.out.println("Digite o preco do segundo produto:");
        p2.preco = Double.parseDouble(sc.nextLine());

        // bloco de inserção de dados do terceiro produto
        System.out.println("Digite o nome do terceiro produto:");
        p3.nome = sc.nextLine();
        System.out.println("Digite o preco do terceiro produto:");
        p3.preco = Double.parseDouble(sc.nextLine());

        // bloco de mostrar as informações
        p1.mostrarPreco(1);
        p2.mostrarPreco(2);
        p3.mostrarPreco(3);

        // bloco de encerramento
        System.out.print("Aperte Enter para encerrar...");
        sc.nextLine();
    }
}
