// linha de importação do pacote
package atvd1.ex2;

// linha de criação da classe produto
public class ex2Produto {

    // bloco de declaração dos atributos
    String nome;
    double preco;

    // bloco de declaração do metodo principal
    public void mostrarPreco(int i){
        System.out.println("O nome do " + i + "º produto é " + nome + "\n \\-- e o seu preço é: " + preco);
    }
}
