# TUTORIAL DO EXECUTAVEL

1. Primeiro peguei o codigo fonte Main.java e fiz a compilação usando o `javac Main.java`, gerando o arquivo: Main.class

2. apos isso fiz o manifest.txt > apontando que a classe principal do projeto é a Main `Main-Class: Main` (+ quebra de linha), para gerar o .jar da aplicação usando o seguinte comando `jar cfm teste.jar manifest.txt Main.class` (sendo: Main.class + manifest.txt)

3. com o .jar gerado, já é possivel executar via terminal usando o `java -jar teste.jar`

4. depois é legal verificar as dependencias desse .jar usando o `jdeps --print-module-deps teste.jar` para fazer um runner customizado do JRE para o que você precisa

5. que é o proximo topico, com o seguinte comando `jlink --add-modules java.base --output JREcustom` você gera esse runner customizado do JRE.

6. partindo para a configuração do Exe é necessário [dessa aplicação](https://launch4j.sourceforge.net/)

7. logo em seguida dessa aplicação instalada, abra ela, e na aba `Basic` no campo `Output file:` coloque o caminho onde arquivo .exe será gerado, exemplo: `C:\Users\elias\Desktop\pastaresultado\resultado.exe` (nesse caso eu criei uma pasta na area de trabalho onde continha o JREcustom gerado no item 5 e o teste.jar gerado no item 2 e testado no item 3)

8. já no campo `Jar:` coloque o seu arquivo .jar gerado anteriormente, no nosso exemplo, o teste.jar: `C:\Users\elias\Desktop\pastaresultado\teste.jar`

9. Na aba `Header` apenas marque a caixa `Console`, pois nesse caso, como não é uma aplicação com interface grafica, é necessário marcar essa caixinha.

10. Na aba `JRE`, em `JRE paths:` coloque a pasta do seu runner customizado (DETALHE, ELE TEM QUE ESTAR NA MESMA PASTA DO ARQUIVO .EXE GERADO). exemplo: `JREcustom`

11. Após tudo isso, apenas clique em Build wrapper, no canto superior esquerdo, o icone de engrenagem. ao clicar vai pedir para gerar um arquivo XML de configuração, apenas escolha o caminho e renomeie ele com o nome de seu interesse (geralmente eu coloco o nome de cfg.xml e redireciono ele para a pasta que, nesse exemplo, é uma pasta na minha area de trabalho com o nome de pastaresultado)

12. Pronto, seu .exe foi gerado com sucesso. agora você pode fazer um zip dessa pasta e distribuir por ai como uma aplicação portatil.

# TUTORIAL DO INSTALADOR USANDO 7ZIP

1. Após feito tudo isso, vou supor que você já possui o [7zip](https://www.7-zip.org/) instalado na sua maquina windows.

2. Compacte a sua pastaresultado, usada no exemplo apenas com o .exe gerado e o JREcustom no formado .7z (nesse caso deixei o arquivo na area de trabalho)

3. Na raiz do sistema > `C:\Program Files\7-Zip` procure o arquivo entitulado `7z.sfx`.

4. Ao localizar ele copie e cole na area de trabalho, vou fazer tudo na area de trabalho para que facilite no entendimento do processo.

5. Apos tudo isso, no cmd localizado no desktop: `cd C:\Users\elias\Desktop` rode o comando `copy /b 7z.sfx + pastaresultado.7z Instalador.exe`

6. Ao rodar o comando, irá aparecer um arquivo chamado Instalador.exe na sua area de trabalho, ao clicar nele irá aparecer uma tela para o usuario extrair os arquivos da sua aplicação onde deseja e rodar ela sem maiores problemas.
