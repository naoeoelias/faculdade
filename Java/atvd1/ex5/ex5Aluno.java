// linha de importação do pacote
package atvd1.ex5;

// linha de criação da classe Aluno
public class ex5Aluno {

    // bloco e declaração dos atributos
    String nome;
    double nota1;
    double nota2;

    // bloco do metodo principal
    public void calcularMedia(){

        // linha do calculo da media
        double media = (nota1 + nota2) / 2;

        // bloco de validação se a media é maior ou igual a 7, caso for e aprovado, se não for é reprovado.
        if (media >= 7){
            System.out.println(nome + " está aprovado com a media: " + media);
        } else {
            System.out.println(nome + " está REPROVADO com a media: " + media);
        }
    }
}
