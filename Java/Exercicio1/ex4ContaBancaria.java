// linha de importação do scanner
import java.util.Scanner;

// linha de criação da classe ContaBancaria
public class ex4ContaBancaria {

    // bloco de declaração dos atributos
    Scanner sc = new Scanner(System.in);
    double saldo;
    int escolha;
    int valsac;

    // bloco do metodo depositar, que soma o valor digitado na variavel saldo e chama o metodo operação, para uma nova operação.
    public void depositar(double valor){
        saldo += valor;
        System.out.println("Valor: " + saldo);
        operacao();
    }

    // bloco do metodo sacar, que retira o valor digitado na variavel saldo e chama o metodo operação, para uma nova operação.
    // no switch existe um while, que verifica se o valor que o usuario digitou é maior que o saldo, para que o usuario não retire mais que possui
    // assim evitando do valor ficar negativado. valsac declarada exatamente para esse proposito. apenas para verificar essa condicional.
    public void sacar(double valor){
        saldo -= valor;
        System.out.println("Valor: " + saldo);
        operacao();
    }

    // bloco do metodo de ver o saldo, apenas mostra o saldo atual e chama novamente o metodo operação, para uma nova operação.
    public void verSaldo(){
        System.out.println("o valor em saldo é de: " + saldo);
        operacao();
    }

    // bloco do metodo operação, onde a magica acontece, nele solicita um numero, cada numero com sua respectiva função.
    public void operacao(){
        // solicita o numero
        System.out.println("Qual operação você deseja fazer?\n[1] Depositar\n[2] Sacar\n[3] Ver saldo\n[0] Sair");
        // atribui esse valor numero a variavel escolha
        escolha = Integer.parseInt(sc.nextLine());

        // e passa por esse switch
        switch (escolha){
            // se for 1, ele pergunta o valor a ser depositado
            case 1:
                System.out.println("Qual valor você quer depositar?");
                // e deposita usando o metodo de depositar, com o argumento transformando o que o usuario digitou em um valor inteiro.
                depositar(Integer.parseInt(sc.nextLine()));
                break;
            // se for 2, ele pergunta o valor a ser sacado.
            case 2:
                System.out.println("Qual valor você quer sacar?");
                // atribui a essa variavel valsac, para que possa ser verificado uma condicional
                valsac = Integer.parseInt(sc.nextLine());

                // enquanto essa variavel for maior que o saldo, ele vai continuar perguntando até que seja menor
                while (valsac > saldo) {
                    System.out.println("Valor invalido! Qual valor você quer sacar?");
                    valsac = Integer.parseInt(sc.nextLine());
                }

                // e quando for menor, ele vai sacar, dando o argumento valsac, que já é um inteiro.
                sacar(valsac);
                break;
            // se for 3, ele vai apenas mostrar o saldo.
            case 3:
                verSaldo();
                break;
        }
    }
}
