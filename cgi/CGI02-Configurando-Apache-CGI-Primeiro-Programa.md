# Configurando o Apache para CGI e testando com "hello world" em Python

Os usuários do servidor já podem publicar arquivos HTML mas por padrão não podem executar programas CGI. Para isso precisamos usar outro módulo do Apache e alterar nossa configuração do módulo <code>userdir</code> que acabamos de habilitar.

Começe habilitando o módulo <code>cgid</code> do Apache. Esse módulo é o responsável pela execução, através da interface CGI, de programas que estão hospedados em diretórios aos quais o servidor web tem acesso.

``` bash
a2enmod cgid
```

Agora abra o arquivo de configuração do módulo <code>userdir</code>

``` bash
vi /etc/apache2/mods-enabled/userdir.conf
```

Você vai acrescentar a opção <code> ExecCGI</code> na diretiva <code>Options</code> do diretório <code>/home/*/public_html</code>. 

Vai acrescentar também uma nova diretiva <code>SetHandler</code> com a opção <code>cgi-script</code>.


O arquivo <code>userdir.conf</code> vai ficar parecido com este:

``` apache
<IfModule mod_userdir.c>
    UserDir public_html
    UserDir disabled root

    <Directory /home/*/public_html>
        AllowOverride FileInfo AuthConfig Limit Indexes
        Options ExecCGI MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
        Require method GET POST OPTIONS
        SetHandler cgi-script
    </Directory>
</IfModule>
```

> Para poder inserir e apagar texto usando o editor <code>vi</code>, tecle <kbd>i</kbd>.
Para salvar as alterações e sair do <code>vi</code> tecle <kbd>ESC</kbd> depois <kbd>:</kbd> e escreva <code>wq</code> (_write_ e _quit_) e tecle <kbd>enter</kbd> para executar o comando.

Agora reinicie o Apache para carregar as novas configurações.

``` bash
systemctl restart apache2
```

## Hello World CGI

Vamos fazer um primeiro programa para testar a execução através da interface CGI.

Crie um arquivo chamado <code>hellopy</code> com este código.

``` python
#!/usr/bin/python3
print("Content-type: text/html\n\n")
print("Hello, World! <br>")
print("em <b>Python</b>)
```

Este é um script CGI escrito na linguagem Python. Para o Apache poder executá-lo precisamos dar permissão de execução para esse arquivo. 

``` bash
chmod o+x hellopy
```

> Note que a permissão de execução é para _others_ (outros usuários, que não são nem você e que não fazem parte do seu grupo de usuários).

Você pode também dar permissão de execução para você e experimentar rodar o script em linha de comando.

```bash
chmod u+x hellopy
```

Para executar o script no terminal do Linux digite o nome dele e tecle <kbd>enter</kbd>.
``` bash
hellopy
```
Você vai ver no terminal a saída do script
```
Content-type: text/html


Hello, World! <br>
em <b>Python</b>
```

Para executar o script através da interface CGI, de dentro do seu web browser, basta acessar o arquivo <code>hellopy</code> pelo browser como se ele fosse uma página HTML. Por exemplo, acessando o URL <code>http://69.164.209.100/~aluno/hellopy</code>

O restultado deve ser:

![Hello World em Python através da CGI](/img/cgi02/cgi02-hellopy.JPG)

