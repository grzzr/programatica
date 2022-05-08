# Modelo de Aplicação Desktop em C#

Este é um modelo para ajudar você a começar a escrever uma aplicação desktop em C#.

Ele dá para você apenas um ponto de partida mínimo. Esse mínimo é:

- uma classe para o primeiro objeto da sua aplicação, com um único método chamado <code>Iniciar()</code>
- uma classe com o método <code>Main()</code>

O método <code>Main()</code> é obrigatório por exigência do C#. A classe chamada <code>AppDesktop</code> é a classe o objeto inicial da sua aplicação e é ela que tem o método chamado <code>Iniciar()</code>.

Você começa a escrever sua aplicação acrescentando código ao método <code>Iniciar()</code> que já vem pronto. Depois basta compilar e executar o programa.

## Objetivo do modelo (por quê usá-lo?)

Pode parecer conveniente usar o método <code>Main()</code> para escrever o código da sua apliacação especialmente quando ela é muito simples. A implementação de um exercício de lógica, por exemplo, normalmente pode ser feita toda em um único método e poderíamos usar o método <code>Main()</code> para isso, já que ele é obrigatório e temos mesmo que escrevê-lo. 

O problema de usar o método <code>Main()</code> para essa finalidade tem a ver com a modelagem orientada a objetos. 

É que um sistema orientado a objetos é, conceitualmente, composto por um conjunto de objetos que trocam mensagens uns com os outros solicitando a execução de métodos. Quem solicita a execução do método <code>Main()</code> não é nenhum objeto do sistema que estamos criando, mas sim o Sistema Operacional, que além disso não é um objeto.

Isso deixa as coisas confusas do ponto de vista da modelagem do sistema porque:

- usando o método <code>Main()</code> para já escrever código da nossa aplicação estamos situando esse código em um ponto de passagem entre o Sistema Operacional (que é um sistema) e nosso programa (que é outro sistema) e assim não fica muito explícito que esse código que estamos escrevendo já faz parte de um novo sistema que está executando.
- nenhum objeto está enviando uma mensagem para nosso sistema para que ele inicie sua execução e é melhor ver esse momento, da primeira mensagem enviada, explícito no código.

O que este modelo de aplicação faz é dar para você um padrão de inicialização do sistema que vai deixar mais claro que o ponto inicial do seu sistema faz parte do seu sistema e não de outro e deixar explícita a mensagem inicial e para qual objeto ela é enviada e quem está enviando ela. Assim vamos nos livrar o quanto antes dessa passagem entre entre sistemas (vamos nos livrar do método <code>Main()</code>) e teremos um ponto claro de inicio para o nosso sistema que seja dele e de ninguém mais.

## Como o modelo funciona

Em C# as aplicações iniciam obrigatoriamente pelo método Main(). Sua declaração é:
<pre>
<code>public static void Main(string[] args)</code>
</pre>
Ele precisa estar definido em alguma classe da sua aplicação e apenas uma vez. No caso deste modelo ele está na classe <code>Program</code>. Porém, neste modelo não usaremos o método <code>Main()</code> para escrever nada da lógica da nossa aplicação. Nossa aplicação vai começar a ser escrita no método <code>Iniciar()</code> da classe <code>AppDesktop</code>. 

A aplicação que você vai escrever usando este modelo vai começar a executar de fato pelo método <code>Iniciar()</code> da classe <code>AppDesktop</code>. O método <code>Main()</code> da classe <code>Program</code> vai ser executado primeiro, por convenção do C#, mas a única coisa que esse método <code>Main()</code> vai fazer será criar um objeto da classe <code>AppDesktop</code> e em seguida enviar uma mensagem para esse objeto pedindo que ele execute o método <code>Iniciar()</code>. 

<pre>
public static void Main(string[] args)
{         
    AppDesktop objetoApp = new AppDesktop();
    objetoApp.Iniciar();                     
}
</pre>

Quando esse novo objeto da classe <code>AppDesktop</code> receber essa mensagem ele vai executar o método <code>Iniciar()</code> que está definido na classe <code>AppDesktop</code>.

<pre>
public void Iniciar()
{
    Console.WriteLine("Iniciando AppDesktop");
    /*
    restante do código vai daqui pra baixo
                .
                .
                .
    */
}
</pre>

Por isso é que vamos considerar que sua aplicação desktop vai começar a executar quando esse método <code>Iniciar()</code> da classe <code>AppDesktop</code> for executado. É porque ele é que contém o primeiro código relevante da aplicação. Tudo que foi executado até aqui foi apenas com o objetivo de atender os padrões de inicialização de uma aplicação escrita em C#.

## Como usar

Para usar esse modelo você começa a escrever sua aplicação modificando o código apenas de <code>AppDesktop</code>. Não é preciso alterar nada na classe <code>Program</code>, que é a que contém o método Main().

Faça assim:

1. Baixe os dois arquivos do modelo: <code>[Program.cs](Program.cs)</code> e <code>[AppDesktop.cs](AppDesktop.cs)</code> para uma diretório em seu computador
1. Abra o arquivo <code>AppDesktop.cs</code>
1. Escreva no corpo desse método <code>Iniciar()</code> as primeiras linhas código da sua aplicação (ou toda ela, caso ela seja muito curta, como a implementeção de um exercício de lógica de programação ;-) )
1. Compile passando como parâmetro para o compilador os dois arquivos deste modelo: <code>Program.cs</code> e <code>AppDesktop.cs</code>
1. Caso você tenha criado outras classes em outros arquivos <code>.cs</code>, passe esses arquivos para o compilador também
1. Execute sua aplicação rodando o arquivo <code>Program.exe</code> que será gerado pelo compilador - note que o arquivo executável gerado não se chama <code>AppDesktop.exe</code> porque a classe que contém o método <code>Main()</code> é a classe <code>Program</code>.

Exemplo:

Na classe AppDesktop inclua o código a seguir no corop do método Iniciar():

<pre>

public void Iniciar()
{
    //este é o código que você escreve

    Console.WriteLine("Qual é o seu nome? ");
    string umNome = Console.ReadLine();

    Console.WriteLine("Prazer, " + umNome +"!\nJá estudou C# hoje?");

    //aqui termina o seu código
}
</pre>



Para compilar
> <code>csc Program.cs AppDesktop.cs</code>

Para executar
> <code>Program.exe</code>

## Como personalizar o modelo para a sua aplicação

É simples. Começe mudando o nome das classes para algo que faça sentido para sua aplicação.

Por exemplo, se você está escrevendo uma aplicação que vai ler as notas de uma turma de alunos e calcular a média delas, pode trocar o nome da classe <code>AppDesktop</code> para <code>CalculadorDeMedias</code>. 

<pre>
public class CalculadorDeMedias
{
    //o restante do código pode ficar como está
}
</pre>

Na classe <code>Program</code> você vai precisar fazer a alteração correspondente. Não vai mais instanciar a classe <code>AppDesktop</code> mas agora a classe <code>CalculadorDeMedias</code>. Assim:

<pre>

// no método Main()

CalculadorDeMedias objetoApp = new CalculadorDeMedias();
objetoApp.Iniciar();

</pre>

Depois você pode mudar também o nome do método <code>Iniciar()</code> para algum outro que você prefira. Você pode mudar o nome do <code>namespace</code> do modelo... Fique à vontade. O código é para ser seu e ele deve ser expressivo e fazer sentido, primeiro, para você. Depois trataremos de fazer ele ter sentido para outras pessoas, que irão ler o seu código.