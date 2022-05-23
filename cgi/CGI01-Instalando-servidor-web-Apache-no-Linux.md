# Instalando um servidor web Apache (versão 2.4) no Linux (Debian 11/Ubuntu 22.04)

Começe atualizando seu sistema. No terminal do Ubuntu, digite:

``` bash
sudo apt update 
```

Aguarde a lista dos pacotes disponível para atualização. Agora digite:

```
sudo apt upgrade
```
O gerenciador de pacotes _apt_  vai baixar os pacotes atualizados, informar o espaço em disco que eles ocuparão e perguntar se você confirma a atualização. Confirme teclando <kbd>enter</kbd> ou <kbd>Y</kbd>.

Instale o pacote do Apache 2

``` bash
sudo apt install apache2
```

Após a instalação o servidor já é inicializado e já está servindo arquivos.

Teste a instalação acessando o endereço do seu servidor através de um web browser.

Você deve ver a seguinte página HTML padrão do Ubuntu.

![Página padrão do servidor Apache no Ubuntu](/img/cgi01/CGI01-pagina-padrao-apache-debian.JPG)
_página padrão do servidor Apache no Debian_

Isso quer dizer que o servidor Apache está rodando. Tudo certo até aqui!

## Diretório padrão do Apache no Debian/Ubuntu

Por padrão, as páginas HTML do seu servidor ficam no diretório

``` bash
/var/www/html
```

A página padrão que você acabou de ver está hospedada lá. Você pode conferir listando o diretório:

``` bash
ls -l /var/www/html
```
O resultado deve ser como o abaixo (exceto pela data e hora, claro):

``` bash
total 12
-rw-r--r-- 1 root root 10671 May 22 19:09 index.html
```

## Para criar um diretório _public_html_ para cada usuário

Nosso servidor Linux pode ter um servidor web como o Apache rodando para servir páginas HTML de um único site ou de vários sites.

Em um servidor com vários usuários podemos habilitar um diretório especial na conta de cada um deles e dar acesso a esse diretório ao Apache. Assim o Apache poderá servir páginas HTML a partir desse diretório particular de cada usuário.

Para isso, ative o módulo _mod_userdir_ do Apache. 

``` bash
a2enmod userdir
```

Esse módulo habilita o acesso do servidor web a um diretório chamado _public_html_ que deve ser criado no diretório padrão de cada usuário. Nesse diretório os usuários poderão colocar arquivos HTML que serão publicados pelo servidor web em um endereço que pode ser acessado pelo URL que tem a seguinte forma:

``` http
http://endereço.do.servidor/~login_do_usuário
```

Já vamos criar esse diretório e publicar um HTML. Antes disso, reinicie o servidor Apache para que a nova configuração seja lida e o módulo _mod_userdir_ começe a trabalhar.

``` bash
systemctl restart apache2
```

Agora sim faça login como algum usuário do seu sistema. Não use sua conta de usuário _root_. Crie um diretório chamado _public_html_ dentro do seu diretório padrão.

``` bash
cd ~
mkdir public_html
cd public_html
```

Teste o acesso ao seu diretório _public_html_ usando um browser para ver ser o Apache está servindo arquivos a partir dele.

Se seu servidor tem o endereço IP <code>69.164.209.100</code> e seu usuário tem login <code>aluno</code>, então o URL para acessar o diretório _public_html_ de seu usuário seria:

``` html
http://69.164.209.100/~aluno
```

Você deve ver no browser uma listagem de diretório assim:

![Listagem de diretório padrão do Apache](/img/cgi01/CGI01-userdir-listagem-padrao.JPG)

>Cuide para não esquecer o _~_ (til) antes do login!

Coloque algum arquivo HTML nesse diretório. Pode ser até mesmo um arquivo vazio. Para criar um arquivo vazio, use o comando <code>touch</code> do Linux. Por exemplo:

``` bash
touch index.html
````

Acessando novamente (ou recarregando) o mesmo URL agora você deve ver uma página em branco.