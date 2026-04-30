// linha de importação do pacote
package atvd1.ex5;

// linha de importação do scanner
import java.util.Scanner;

// criação da classe principal
public class ex5Main {
    public static void main(String[] args){

        // linha de criação do objeto scanner
        Scanner sc = new Scanner(System.in);

        // linha de criação do objeto Aluno
        ex5Aluno a = new ex5Aluno();

        // bloco de inserção de dados do aluno
        System.out.println("Digite o seu nome:");
        a.nome = sc.nextLine();

        // bloco de inserção de dados das notas do aluno
        System.out.println("Digite a primeira nota:");
        a.nota1 = Double.parseDouble(sc.nextLine());
        System.out.println("Digite a segunda nota:");
        a.nota2 = Double.parseDouble(sc.nextLine());

        // calculo da media + o resultado.
        a.calcularMedia();

        // bloco de encerramento
        System.out.print("Aperte Enter para encerrar...");
        sc.nextLine();
    }
}
