package atvd1;
import atvd1.ex1.ex1Main;
import atvd1.ex2.ex2Main;
import atvd1.ex3.ex3Main;
import atvd1.ex4.ex4Main;
import atvd1.ex5.ex5Main;
import atvd1.ex6.ex6Main;

public class Launcher {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Argumento invalido, tente executar o .JAR da seguinte maneira\njava -jar launcher.jar ex1/ex2/ex3/ex4/ex5/ex6");
            return;
        }

        String comando = args[0];

        switch (comando.toLowerCase()){
            case "ex1":
                ex1Main.main(null);
                break;
            case "ex2":
                ex2Main.main(null);
                break;
            case "ex3":
                ex3Main.main(null);
                break;
            case "ex4":
                ex4Main.main(null);
                break;
            case "ex5":
                ex5Main.main(null);
                break;
            case "ex6":
                ex6Main.main(null);
                break;
            default:
                System.out.println("Argumento invalido, tente executar o .JAR da seguinte maneira\njava -jar launcher.jar ex1/ex2/ex3/ex4/ex5/ex6");
        }
    }
}
