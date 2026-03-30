1. Primeiro peguei o codigo fonte Main.java e fiz a compilação usando o `javac Main.java`, gerando o arquivo: Main.class

2. apos isso fiz o manifest.txt > apontando que a classe principal do projeto é a Main, para gerar o .jar da aplicação usando o seguinte comando `jar cfm teste.jar manifest.txt Main.class` (sendo: Main.class + manifest.txt)

3. com o .jar gerado, já é possivel executar via terminal usando o `java -jar teste.jar`

4. depois é legal verificar as dependencias desse .jar usando o `jdeps --print-module-deps teste.jar` para fazer um runner customizado do JRE para o que você precisa

5. que é o proximo topico, com o seguinte comando `jlink --add-modules java.base --output JREcustom` você gera esse runner customizado do JRE.

6. partindo para a configuração do AppImage é necessário [dessa aplicação](https://github.com/AppImage/appimagetool/releases/tag/continuous)

7. logo em seguida dessa aplicação instalada, crie uma pasta no seguinte modelo
```
teste.AppDir/
|--AppRun
|-- teste.desktop
|-- icone.png
\-- usr/
    |-- bin/
    \-- lib/
```

8. No arquivo AppRun você coloca exatamente dessa maneira, sendo um arquivo shell script, onde a variavel HERE vai buscar a pasta atual, e executar um comando java logo em seguida. é necessario que na pasta `usr/lib/` esteja o seu runtime custom que você gerou anteriormente, neste exemplo sendo o JREcustom, e no local `usr/bin/` esteja o arquivo teste.jar, sendo gerado no item 2 e testado no item 3.
```
#!/bin/bash
HERE="$(dirname "$(readlink -f "$0")")"

"$HERE/usr/lib/JREcustom/bin/java" -jar "$HERE/usr/bin/teste.jar"
```
Após isso, dê a permissão de execução usando o `chmod +x AppRun` ou via interface grafica do seu sistema.

9. no arquivo teste.desktop você coloca os parametros para que seja gerado o .AppImage final. só preencher normalmente, sendo `Name=teste`, `Exec=AppRun` (o ponto de partida para abrir sua aplicação), `Icon=icone` auto explicativo, mas pelo amor de deus, nessa parte não coloca a extensão do arquivo, e também é recomendado usar .png, `Terminal=true` essa parte é opcional, vai de cada um. `Type=Application` determina apenas o tipo e `Categories=Utility;` determina a categioria e finaliza o arquivo .desktop
```
[Desktop Entry]
Name=teste
Exec=AppRun
Icon=icone
Terminal=true
Type=Application
Categories=Utility;
```

10. no fim de tudo, com isso tudo configurado dentro da pasta de exemplo teste.AppDir é só gerar o arquivo .AppImage usando o comando `chmod +x appimagetool-x86_64.AppImage` (dentro da pasta onde o appimage foi baixado) ou permitindo a execução do arquivo via interface grafica, e no terminal mesmo prossiga com o comando: `./appimagetool-x86_64.AppImage teste.AppDir`, assim finalizando com a compilação do seu .AppImage.

BONUS. o seu AppImage não vai abrir com um duplo clique, apenas via terminal usando o comando `./teste-x86_64.AppImage`. para criar um runner para essa aplicação abrir direto no terminal, você cria um arquivo chamado run.desktop com o seguinte conteudo.
```
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Run
Exec=sh -c '"$(dirname "%k")/teste-x86_64.AppImage"'
Terminal=true
Type=Application
```
ele reconhece o arquivo na pasta onde se encontra e executa ele no terminal, e assim o aplicativo fica mais facil de abrir, nesse caso, com um duplo clique.
