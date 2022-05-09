# Arquitetura de um programa orientado a objetos

Programas são coisas muito complexas, e trabalhar com objetos em uma linguagem de programação é uma forma de lidar com essa complexidade.

Programas orientados a objeto são concebidos como uma imensa rede de troca de mensagens entre objetos que estão todos colaborando entre si para a realização de uma tarefa complexa, que é a tarefa do sistema ao qual eles pertencem. 

A inspiração para o uso desse tipo de estrutura veio da biologia, do modo como células, cada uma especializada em uma tarefa, interagem para realizar tarefas complexas em conjunto.


![Células especializadas realizando tarefa em conjunto](/img/poo02/POO02-Celulas-especializadas-relizando-tarefa-em-conjunto.png)

Cada objeto é especializdo em uma tarefa. Ele pode precisar realizar diversas funções para conseguir realizar essa sua tarefa e por isso ele pode ter vários métodos, mas conceitualmente a tarefa de cada objeto é uma só. 

No exemplo do disco-voador, sua tarefa é, por exemplo, ser um disco-voador e não uma vaca.

O sistema que estamos fazendo pode até ser sobre a interação de discos-voadores com vacas que, aliás, é muito comum de acontecer. O que não é comum é um programa orientado a objetos romper a estrutura inerente aos objetos do tipo Vaca e Disco-Voador reais, que existem no mundo, e modelar eles no computador como se fossem parte da mesma estrutura, por exemplo: uma vaca com lasers ou um disco-voador que rumina.

## Encapsulamento e troca de mensagens

Digamos que nosso sistema vai modelar o processo de abdução de uma vaca por um disco-voador. Em algum momento a vaca vai estar dentro do disco-voador. Isso não significa, porém, que agora o disco-voador é um pouco vaca também. Não. O que acontece é uma interação entre eles, uma colaboração na qual nenhum deixa de ser o que é e cada um cumpre seu papel para a realização de uma ação em comum.

Vamos imaginar três objetos participando dessa operação de abdução: o disco-voador; a vaca; e você, no comando do disco-voador. Um programa orientado a objetos modelaria a abdução assim:

O <code>Comandante</code> (você) envia a mensagem <code>disco-voador abduzir vaca</code> para o objeto <code>disco-voador</code> solicitando a execução do método <code>abduzir</code> e passando como parâmetro a <code>vaca</code>.

Em Java, C#, C++, a linha de código com essa mensagem seria:

<pre>

disco.abduzir(vaca);

</pre>

> O objeto que envia a mensagem não aparece escrito no código. Devemos sempre fazer o trabalho de nos colocarmos no lugar desse objeto ao escrever o código. É algo que faz parte daquele exercício de abstrair ao qual me referi antes, e você vai ter que ficar bom nisso para programar.

Note no exemplo acima como cada objeto teve um papel bem definido na execução da operação de abdução:

- Você, por exemplo, não executou a tarefa <code>abduzir</code>. Você foi quem solicitou.
- Quem executou a tarefa foi o <code>disco-voador</code>, mas ele não teria feito se você não tivesse enviado a mensagem pedindo.
- A vaca também não sabia, tampouco você, como realizar a tarefa <code>abduzir</code>. Só o <code>disco-voador</code> sabia.
- A <code>vaca</code> não entrou no <code>disco-voador</code> por que quis. Ela foi o objeto da abdução, o parâmetro enviado na mensagem que chamou o método <code>abduzir</code>
- Quem passou a <code>vaca</code> como parâmetro foi você, que enviou a mensagem. Isso significa que coube a você a tarefa de, primeiro, identificar qual era a vaca (isso não aparece no código do exemplo, mas é lógico supor que precisou ter acontecido)

Nenhum objeto interferiu diretamente nem nas ações nem nas propriedades ou estados dos outros para realizar essa tarefa. Cada um cuidou das suas coisas. 

![Encapsulamento e troca de mensagens - objetos](/img/poo02/POO02-Encapsulamento-e-troca-de-mensagens-objetos.png)


Além disso, não foi solicitado ao objeto que ele fizesse algo que não saberia ou que não poderia fazer. O método <code>abduzir</code>, que recebe uma <code>Vaca</code> como parâmetro, estava definido para o <code>disco-voador</code> - alguém escreveu o código para esse método. 

## Por quê *arquitetura*?

A palavra <code>arquitetura</code> significa <code>"colocar arcos"</code>. A ideia aqui é que para criar uma construção o importante é saber como planejar a colocação dos arcos que sustentarão a estrutura. É claro que para o projeto de uma construção são necessários mais do que apenas arcos, mas a origem da palavra vem dessa ideia e dessa estrutura de design muito básica, que é o <code>arco</code>.

No caso de um sistema computacional, os "arcos" são as relações entre seus componenente e, no caso de usarmos uma linguagem orientada o objetos, as relações entre os objetos.

As principais relações entre os objetos que precisamos saber definir são as duas que vimos há pouco:

- quais as partes do objeto (propriedades e estados)
- como ele se comunica com outros objetos (métodos/mensagens)

São esses relacionamentos entre os objetos que sustentarão a aplicação. Isso é o que chamamos de <code>arquitetura</code> do sistema. 

Normalmente a arquitetura de um sistema é a definição do sistema em um nível bastante abstrato, uma visão geral do sistema. Você já deve ter ouvido falar de uma arquitetura de sistemas chamada "cliente-servidor". Essa arquitetura relaciona dois tipos de objetos que pertencerão ao sistema: uns chamados de "clientes" e outros chamados "servidores". A arquitetura caracteriza esses objetos segundo o modo como eles se relacionam:

- servidores: são os que executam tarefas para os clientes
- clientes: são os que solicitam tarefas para os servidores

Parecido com o modelo de comunicação que vimos para objetos, não é? O emissor da mensagem é o cliente e o objeto que recebe a mensagem e executa o método é o servidor. 

Na próxima sessão vamos ver uma arquitetura para sistemas que têm uma interface com o usuário. Ela também vai se parecer com o modelo de objetos que acabamos de ver...