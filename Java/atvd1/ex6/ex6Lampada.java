// linha de importação do pacote
package atvd1.ex6;

// linha de importação do scanner
import java.util.Scanner;

// linha de criação da classe Lampada
public class ex6Lampada {

    // bloco de declaração dos atributos
    Scanner sc = new Scanner(System.in);
    boolean lampada;
    int escolha;


    // bloco do metodo ligar, onde marca a lampada para true e chama uma nova operação.
    public void ligar(){
        lampada = true;
        System.out.println("(ALTERAÇÃO DE ESTADO) Lampada ligada");
        operacao();
    }

    // bloco do metodo desligar, onde marca a lampada para false e chama uma nova operação.
    public void desligar(){
        lampada = false;
        System.out.println("(ALTERAÇÃO DE ESTADO) Lampada desligada");
        operacao();
    }

    // bloco do metodo mostrar estado, onde verifica se lampada está true, caso estiver,
    // printa lampada ligada, caso não, lampada desligada. e no fim chama a operação novamente.
    public void mostrarEstado(){
        if (lampada){
            System.out.println("Lampada ligada");
        } else {
            System.out.println("Lampada desligada");
        }
        operacao();
    }

    // bloco do metodo principal, o operação, nele solicita um numero, cada um com a sua respectiva função.
    public void operacao(){
        // primeiro ele solicita um numero
        System.out.println("Qual operação você deseja fazer?\n[1] Ligar lampada\n[2] Desligar Lampada\n[3] Ver estado da lampada\n[0] Sair");
        escolha = Integer.parseInt(sc.nextLine());

        // e verifica esse numero
        switch (escolha){
            case 1:
                // caso for 1, ele chama o metodo ligar
                ligar();
                break;
            case 2:
                // caso 2, chama o metodo desligar
                desligar();
                break;
            case 3:
                // caso 3, ele chama o mostrar estado
                mostrarEstado();
                break;
        }
    }
}
