// linha de importação do pacote
package atvd1.ex1;

// linha de criação da classe pessoa
public class ex1Pessoa{

    // bloco de declaração dos atributos
    String nome;
    int idade;

    // bloco de declaração do metodo principal
    public void apresentar(int i){
        System.out.println("O " + i + "º nome digitado foi: " + nome + "\n \\-- e a " + i +"º idade digitada foi: " + idade);
    }
}