// linha de criação da classe carro
public class ex3Carro {

    // bloco de declaração dos atributos
    String marca;
    int velocidade = 0;

    // bloco de declaração do metodo secundario
    public void acelerar(){
        velocidade += 10;
        System.out.println("A marca do carro é " + marca + ", e a velocidade atual é " + velocidade);
    }

    // bloco de declaração do metodo principal
    public void vezesacelerar(int vezes) {
        int i = 0;
        while (i < vezes) {
            acelerar();
            i++;
        }
    }
}
