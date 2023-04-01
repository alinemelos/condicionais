# condicionais
códigos com tema da copa do mundo para aprender sobre estruturas de condições em python
<p> esses códigos são de uma lista de questões da minha graduação em ciência da computação. O assunto principal é estruturas de consições.</p>
<h3>Decisão pênaltis</h3>
<p>A missão é fazer a contagem de gols de uma disputa de pênaltis da copa e definir qual das seleções passa para próxima fase.</p>
<p>A entrada será formada primeiro pelo nome das duas seleções que estão disputando os pênaltis.</p>
<p>Depois, virão 10 entradas, no máximo, já que podem vir menos se a disputa acabar antes, mas nunca mais que 10 entradas. As possibilidades de entradas são:
“Gol”, “Errou”, “Na trave” e “Defendeu”, sendo que apenas a entrada “Gol” conta como gol para a seleção que bateu o pênalti. Além disso, as entradas de número 
ímpar são batidas pela seleção Nome1 e as entradas de número par batidas pela seleção Nome2.</p>
<h3>Escalação</h3>
<p>Vai analisar o desempenho dos jogadores nos jogos e treinos.</p>
<p>As entradas iniciais serão o nome do jogador e a sua disposição percentual durante o treino atual.</p>
<p>Após isso, novas variáveis serão analisadas de acordo com o percentual de disposição desses jogadores. Assim, se a disposição do treino for maior ou igual a 85%:
Será informada a posição e quantidade de chutes a gol ou passes dados por esse jogador.</p>
<p>OBS: Se for um atacante, o valor representará chutes, se for de qualquer outra posição, o valor representará passes.</p>
<p>Por outro lado, se a disposição do treino for de 50% a 85%: Você irá receber como entrada o desempenho do jogador no último jogo, sendo este um valor numérico.</p>
<p>Por fim, se a disposição for menor do que 50%: Você irá receber como entrada o desempenho do último treino realizado pelo jogador, também como um valor numérico.</p>
<h3>Futuro Copa</h3>
<p>a sua função é criar um programa que simule a final conforme descrito a seguir:</p>
<p>Suponha que os times sejam dados nessa ordem: Time A e Time B. Os aspectos técnicos dos times em três características que serão utilizadas:</p>
<p>Força de Ataque (0 a 30)/ Consistência da Defesa (0 a 30)/ Fôlego (0 a 5) </p>
<p>O jogo do programa, simulando o formato original de 2 tempos do Futebol, terá 4 turnos, nos quais um time estará atacando, e o outro estará defendendo. A ordem, baseada no exemplo dado, seria:</p>
<p>Time A atacando → Time B atacando → Time B atacando → Time A atacando</p>
<p>Em um turno de ataque, serão comparados a Força de Ataque do time atacante e a Consistência da Defesa do time que está defendendo. Caso a Força de Ataque seja superior ou igual a Consistência de defesa (Ataque>=Defesa), será marcado um gol pelo time atacante.Contudo, como nós sabemos, em todos os jogos há um leve aspecto de sorte, e Jovanney decidiu por incluir isso no sistema:</p>
<p>Todo turno, será recebido um valor do "fator sorte", sendo um número equivalente a 1 ou 2.</p>

<p>Caso seja 1, haverá um acréscimo de 2 pontos momentâneo na Força de Ataque do time atacante apenas nesse turno.<br>
Caso seja 2, haverá um acréscimo de 2 pontos momentâneo na Consistência da Defesa do time que está defendendo apenas nesse turno.<br>
Agora, a explicação de como a última característica, o Fôlego, afetará o programa:<br>
Jovanney decidiu que seria justo aplicar esse cansaço na simulação criando algo que denominou de: "Fator canseira" de cada time, que com o tempo diminuiria suas características. É um número menor que 1, porém maior que 0, que se calcularia desta forma:<br>
Fator canseira: 1 - ( (5 - Fôlego)/10)<br>
-No turno 1: Não haverá decréscimo nas características.<br>
-No turno 2 em diante: Características sofreriam decréscimos, tendo cada característica tendo seu valor igual a: (Valor da característica) * (Fator canseira)<br>
Obs: Apenas as características "Força de Ataque" e "Consistência da Defesa" serão afetadas por esse cansaço.
<br>
Obs2: Em caso de empate, vence o time atacante nas forças, vence o time atacante
<br>
Em resumo, todos os turnos terão 3 fases: A atribuição do cansaço, depois disso a aplicação do "fator sorte", e enfim a comparação das características em seu valor atual.</p>
<h3>Posicao Jogador</h3>
<p>A entrada será constituída de um nome:</p>
<p>A saída será da seguinte forma:<br>
“[nome_jogador] foi convocado e jogará como [posicao]!<br>
As posições são:<br>
<ul>
 <li>goleiro</li>
 <li>lateral</li>
 <li>zagueiro</li>
 <li>meia</li>
 <li>atacante</li>
</ul>
Caso o nome informado não seja de nenhum jogador convocado, você deverá responder o seguinte:<br>

“[nome_jogador] não foi convocado, mas quem sabe na próxima?”</p>

