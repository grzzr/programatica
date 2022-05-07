# Para usar o compilador do C# em linha de comando, no Windows

### 1. Abra o prompt de comando (cmd.exe) e procure todas as possíveis cópias do arquivo do compilador (csc.exe) que existem no seu sistema (talvez não exista nenhuma). Use o comando:


> dir /s c:\Windows\csc.exe


Esse comando pesquisa (/s, significa search, que quer dizer "pesquisar") em toda a árvore de diretório <code>c:\Windows</code> ocorrências do arquivo <code>csc.exe</code>, que é o compilador do C#.

Se existir alguma cópia (provavelmente existirão várias) do csc.exe ela vai aparecer em uma listagem parecida com esta:
<pre>

 Directory of c:\Windows\Microsoft.NET\Framework\v3.5

2019-12-03  14:04         1,548,432 csc.exe
               1 File(s)      1,548,432 bytes

 Directory of c:\Windows\Microsoft.NET\Framework\v4.0.30319

2019-12-07  06:10         2,141,552 csc.exe
               1 File(s)      2,141,552 bytes

 Directory of c:\Windows\Microsoft.NET\Framework64\v2.0.50727

2019-11-08  14:44            91,256 csc.exe
               1 File(s)         91,256 bytes

 Directory of c:\Windows\Microsoft.NET\Framework64\v3.5

2019-11-08  14:44         2,290,808 csc.exe
               1 File(s)      2,290,808 bytes

 Directory of c:\Windows\Microsoft.NET\Framework64\v4.0.30319

2019-12-07  06:10         2,759,232 csc.exe
               1 File(s)      2,759,232 bytes

</pre>

Cada cópia é uma versão do compilador. Qualquer uma funciona. Sugiro escolher a versão mais alta. Neste caso é a versão 4.0 (que suporta até a versão 5 do C#, que não é a última versão).

### 2. Copie o caminho completo para o arquivo executável do compilador. Neste nosso exemplo, o caminho é:

<pre>
c:\Windows\Microsoft.NET\Framework\v4.0.30319
</pre>

### 4. Agora acrescente esse caminho à variável de ambiente PATH do seu usuário

### 5. Feche o prompt de comando e abra novamente. Fazemos isso para que a variável PATH seja lida novamente no ambiente, dessa vez contendo o caminho para o compilador que vamos usar.

Agora deve ser possível digitar diretamente na linha de comando:

> csc.exe

e ter a resposta do compilador do C#, que indica que ele executou

<pre>
Microsoft (R) Visual C# Compiler version 4.8.4084.0
for C# 5
Copyright (C) Microsoft Corporation. All rights reserved.

This compiler is provided as part of the Microsoft (R) .NET Framework, but only supports language versions up to C# 5, which is no longer the latest version. For compilers that support newer versions of the C# programming language, see http://go.microsoft.com/fwlink/?LinkID=533240

warning CS2008: No source files specified
error CS1562: Outputs without source must have the /out option specified

</pre>

Não se preocupe com as mensagens de <code>warning</code> (alerta) e <code>error</code> (erro) no final. Elas apareceram porque não dissemos para o compilador qual arquivo de código fonte ele deve compilar.