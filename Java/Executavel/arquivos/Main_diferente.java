import java.util.Scanner;

public class Main_diferente {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        Scanner sc = new Scanner(System.in);
        mostrar_nome(sc);
    }

    public static void mostrar_nome(Scanner a){
        String texto = a.nextLine();
        System.out.println("seu nome e: " + texto);
        a.nextLine();
    }
}