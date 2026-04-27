// linha de importação do scanner
import java.util.Scanner;

// criação da classe principal
public class ex3Main {
    public static void main(String[] args) {

        // linha de criação do objeto scanner
        Scanner sc = new Scanner(System.in);

        // linha de criação do objeto carro
        ex3Carro c1 = new ex3Carro();

        // bloco de inserção da marca do carro
        System.out.println("Digite a marca do seu carro:");
        c1.marca = sc.nextLine();

        // bloco de inserção da quantitade de vezes para acelerar
        System.out.println("Quantas vezes deseja acelerar? (maximo 8)");
        int vezes = Integer.parseInt(sc.nextLine());

        // bloco para verificar se o numero de vezes é maior ou igual a 9, se for pergunta de novo até ser 8 ou menos.
        while (vezes >= 9) {
            System.out.println("Quantas vezes deseja acelerar? (maximo 8)");
            vezes = Integer.parseInt(sc.nextLine());
        }

        // Linha para executar o while da outra classe
        c1.vezesacelerar(vezes);

        // bloco de encerramento
        System.out.print("Aperte Enter para encerrar...");
        sc.nextLine();
    }
}
