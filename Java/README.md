Nesta pasta são todas as coisas relacionadas a linguagem de programação: Java

# TUTORIAL VARIAVEL DE AMBIENTE

Para prosseguir com o tutorial das variaveis de ambiente em ambos os sistemas (Windows e Linux Mint), irei usar como base o [OpenJDK 26](https://jdk.java.net/26/).
Nesse caso, em ambos os sistemas são um arquivo zipado, no caso do windows é um arquivo unico, ja no Linux você baixa de acordo com a arquitetura de seu processador.

# Windows

1. Após baixar o arquivo .zip do OpenJDK 26 na sua maquina, você faz a extração desse arquivo e, recomendação minha, mova ele para a raiz do sistema, dentro da pasta: "arquivos de programas": `C:\Program Files`

2. Depois disso feito, vamos configurar as variaveis, são elas `JAVA_HOME` e `PATH`.

3. Abra o CMD do Windows e coloque o seguinte comando para colocar na SESSÃO ATUAL DO TERMINAL: set JAVA_HOME=(caminho_da_pasta). Exemplo `set JAVA_HOME=C:\Program Files\openjdk-26_windows-x64_bin\jdk-26`

4. Logo apos disso, no mesmo terminal altere a outra variavel: `set PATH=%JAVA_HOME%\bin`

5. Para colocar permanentemente no USUARIO ATUAL, utilize os seguintes comandos: `setx JAVA_HOME "C:\Program Files\openjdk-26_windows-x64_bin\jdk-26"` e `setx PATH "%JAVA_HOME%\bin"` (para entrar em vigor, feche a sessão atual do terminal e abra novamente)

6. Já para colocar permanentemente a NIVEL DE SISTEMA (todos os usuarios), acrescente o parametro `/M` ao final do comando, isso requer permissão root, de administrador: `setx JAVA_HOME "C:\Program Files\openjdk-26_windows-x64_bin\jdk-26" /M` e `setx PATH "%JAVA_HOME%\bin;%PATH%" /M` (ABRA O CMD COMO ADMINISTRADOR PARA QUE NÃO RETORNE ACESSO NEGADO AO RODAR O COMANDO)

7. Pronto, agora a sua variavel de ambiente JAVA está devidamente configurada no Windows! :)

# Linux Mint

1. Após baixar o arquivo .tar.gz do OpenJDK 26 na sua maquina, você faz a extração desse arquivo e, recomendação minha, mova ele para a raiz do sistema, dentro da pasta "opt": `/opt`

2. Depois disso feito, vamos configurar as variaveis, são elas `JAVA_HOME` e `PATH`.

3. Abra o Terminal do Linux Mint e coloque o seguinte comando para colocar na SESSÃO ATUAL DO TERMINAL: export JAVA_HOME=(caminho_da_pasta). Exemplo `export JAVA_HOME=/opt/jdk-26`

4. Logo apos disso, no mesmo terminal altere a outra variavel: `export PATH=$JAVA_HOME/bin`

5. Para colocar permanentemente no USUARIO ATUAL, cole esses dois comandos anteriores (`export JAVA_HOME=/opt/jdk-26` e `export PATH=$JAVA_HOME/bin:$PATH`) no final dos arquivos `~/.bashrc` e `~/.profile`, localizados na pasta do usuario.

6. Já para colocar permanentemente a NIVEL DE SISTEMA (todos os usuarios), acrescente a variavel PATH o caminho dos binarios do JAVA conforme o exemplo: `/opt/jdk-26/bin` no arquivo environment, localizado em `/etc/environment` (ABRA O ARQUIVO COMO ROOT PARA QUE NÃO RETORNE ACESSO NEGADO AO SALVAR)
```
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/jdk-26/bin"
```
Exemplo do que tem no meu arquivo environment (com o java previamente configurado), todos esses locais são variaveis do path, divididas por : pelo o que eu entendi. apenas acrescentei o caminho dos binarios do java no final para que funcione em todo o sistema linux.

7. Pronto, agora a sua variavel de ambiente JAVA está devidamente configurada no Linux Mint! :)

<!-- sudo apt install codeblocks build-essential -->
<!-- sudo apt install xterm -->
<!-- isso é apenas um save de uma coisa de c++ no linux, coisas vão vir por ai :P -->
