// linha de importação do pacote
package atvd1.ex1;

// linha de importação do scanner
import java.util.Scanner;

// criação da classe principal
public class ex1Main {
    public static void main(String[] args) {

        // linha de criação do objeto scanner
        Scanner sc = new Scanner(System.in);

        // bloco de criação dos objetos de pessoa 1 e 2
        ex1Pessoa p1 = new ex1Pessoa();
        ex1Pessoa p2 = new ex1Pessoa();

        // bloco de inserção de dados da primeira pessoa
        System.out.println("Digite o nome da pessoa 1:");
        p1.nome = sc.nextLine();
        System.out.println("Digite a idade da pessoa 1:");
        p1.idade = Integer.parseInt(sc.nextLine());

        // bloco de inserção de dados da segunda pessoa
        System.out.println("Digite o nome da pessoa 2:");
        p2.nome = sc.nextLine();
        System.out.println("Digite a idade da pessoa 2:");
        p2.idade = Integer.parseInt(sc.nextLine());

        // bloco de apresentações
        p1.apresentar(1);
        p2.apresentar(2);

        // bloco de encerramento
        System.out.print("Aperte Enter para encerrar...");
        sc.nextLine();
    }
}