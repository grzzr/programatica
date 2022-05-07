# Modelo de Aplicação Desktop em C#

Um modelo para ajudar a começar a escrever uma aplicação desktop em C#.

Ele contém apenas um método <code>Main()</code>, que é obrigatório, e uma classe chamada <code>AppDesktop</code> que tem apenas um método chamado <code>Iniciar()</code>;

Você começa a escrever sua aplicação acrescentando código ao método <code>Iniciar()</code> que já vem pronto. Depois basta compilar e executar o programa.


## Como o modelo funciona

Em C# as aplicações iniciam obrigatoriamente pelo método Main(). Sua declaração é:
<pre>
<code>public static void Main(string[] args)</code>
</pre>
Ele precisa estar definido em alguma classe da sua aplicação e apenas uma vez. No caso deste modelo ele está na classe <code>Program</code>. Porém, neste modelo não usaremos o método Main() para escrever nada da lógica da nossa aplicação. Nossa aplicação vai começar a ser escrita no método Iniciar() da classe AppDesktop. 

A aplicação que você vai escrever usando este modelo vai começar a executar de fato pelo método Iniciar() da classe AppDesktop. O método Main() da classe Program vai ser executado primeiro, por convenção do C#, mas a única coisa que esse método Main() vai fazer será criar um objeto da classe AppDesktop e em seguida enviar uma mensagem para esse objeto pedindo que ele execute o método Iniciar(). 

<pre>
 public static void Main(string[] args)
        {         
            AppDesktop objetoApp = new AppDesktop();
            objetoApp.Iniciar();
                      
        }

</pre>

Quando esse novo objeto da classe AppDesktop receber essa mensagem ele vai executar o método Iniciar()) que está definido na classe AppDesktop.

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

Por isso é que sua aplicação desktop vai começar a executar, de fato, quando esse método Iniciar() da classe AppDesktop foi executado. Ele é que contém o primeiro código relevante da aplicação. Tudo que foi executado até aqui foi apenas com o objetivo de atender os padrões de inicialização de uma aplicação escrita em C#.

## Como usar

Para usar esse modelo você começa a escrever sua aplicação modificando o código apenas de AppDesktop. Não é preciso alterar nada na classe Program, que é a que contém o método Main().

Faça assim:

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

</pre>



Para compilar
>csc Program.cs AppDesktop.cs

Para executar
>Program.exe

## Como personalizar o modelo para a sua aplicação

É simples. Começe mudando o nome das classes para algo que faça sentido para sua aplicação.

Por exemplo, se você está escrevendo uma aplicação que vai ler as notas de uma turma de alunos e calcular a média delas, pode trocar o nome da classe <code>AppDesktop</code> para <code>CalculadorDeMedias</code>. 

<pre>
    public class CalculadorDeMedias
    {
        // e o restante do código fica como está
    }
</pre>

Na classe <code>Program</code> você vai precisar fazer a alteração correspondente. Não vai mais instanciar a classe <code>AppDesktop</code> mas agora a classe <code>CalculadorDeMedias</code>. Assim:

<pre>

    // no método Main()


    CalculadorDeMedias objetoApp = new CalculadorDeMedias();
    objetoApp.Iniciar();

</pre>

Depois você pode mudar também o nome do método <code>Iniciar()</code> para algum outro que você prefira... Fique à vontade. O código é para ser seu e ele deve ser expressivo e fazer sentido, primeiro, para você. Depois trataremos de fazer ele ter sentido para outras pessoas, que irão ler o seu código.