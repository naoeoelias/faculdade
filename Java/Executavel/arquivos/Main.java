import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        Scanner sc = new Scanner(System.in);
        String nome = sc.nextLine();
        System.out.println("Seu nome é: " + nome);
        sc.nextLine();
    }
}
