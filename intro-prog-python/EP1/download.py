<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <meta name="author" content="" />
  <title>Segundo Exercício Programa (EP2) - Gemas</title>
  <style type="text/css">code{white-space: pre;}</style>
  <style type="text/css">
div.sourceCode { overflow-x: auto; }
table.sourceCode, tr.sourceCode, td.lineNumbers, td.sourceCode {
  margin: 0; padding: 0; vertical-align: baseline; border: none; }
table.sourceCode { width: 100%; line-height: 100%; }
td.lineNumbers { text-align: right; padding-right: 4px; padding-left: 4px; color: #aaaaaa; border-right: 1px solid #aaaaaa; }
td.sourceCode { padding-left: 5px; }
code > span.kw { color: #007020; font-weight: bold; } /* Keyword */
code > span.dt { color: #902000; } /* DataType */
code > span.dv { color: #40a070; } /* DecVal */
code > span.bn { color: #40a070; } /* BaseN */
code > span.fl { color: #40a070; } /* Float */
code > span.ch { color: #4070a0; } /* Char */
code > span.st { color: #4070a0; } /* String */
code > span.co { color: #60a0b0; font-style: italic; } /* Comment */
code > span.ot { color: #007020; } /* Other */
code > span.al { color: #ff0000; font-weight: bold; } /* Alert */
code > span.fu { color: #06287e; } /* Function */
code > span.er { color: #ff0000; font-weight: bold; } /* Error */
code > span.wa { color: #60a0b0; font-weight: bold; font-style: italic; } /* Warning */
code > span.cn { color: #880000; } /* Constant */
code > span.sc { color: #4070a0; } /* SpecialChar */
code > span.vs { color: #4070a0; } /* VerbatimString */
code > span.ss { color: #bb6688; } /* SpecialString */
code > span.im { } /* Import */
code > span.va { color: #19177c; } /* Variable */
code > span.cf { color: #007020; font-weight: bold; } /* ControlFlow */
code > span.op { color: #666666; } /* Operator */
code > span.bu { } /* BuiltIn */
code > span.ex { } /* Extension */
code > span.pp { color: #bc7a00; } /* Preprocessor */
code > span.at { color: #7d9029; } /* Attribute */
code > span.do { color: #ba2121; font-style: italic; } /* Documentation */
code > span.an { color: #60a0b0; font-weight: bold; font-style: italic; } /* Annotation */
code > span.cv { color: #60a0b0; font-weight: bold; font-style: italic; } /* CommentVar */
code > span.in { color: #60a0b0; font-weight: bold; font-style: italic; } /* Information */
  </style>
  <link rel="stylesheet" href="styles.css" type="text/css" />
</head>
<body>
<div id="header">
<h1 class="title">Segundo Exercício Programa (EP2) - Gemas</h1>
</div>
<div id="TOC">
<ul>
<li><a href="#informações-iniciais">Informações iniciais</a></li>
<li><a href="#o-jogo">O Jogo</a><ul>
<li><a href="#tabuleiro-e-gemas">Tabuleiro e gemas</a></li>
<li><a href="#dicas">Dicas</a></li>
</ul></li>
<li><a href="#o-que-seu-programa-deve-fazer">O que seu programa deve fazer</a><ul>
<li><a href="#função-main">Função <code>main ()</code></a></li>
<li><a href="#função-criar-num_linhas-num_colunas">Função <code>criar (num_linhas, num_colunas)</code></a></li>
<li><a href="#função-completar-tabuleiro-num_cores">Função <code>completar (tabuleiro, num_cores)</code></a></li>
<li><a href="#função-exibir-tabuleiro">Função <code>exibir (tabuleiro)</code></a></li>
<li><a href="#função-trocar-linha1-coluna1-linha2-coluna2-tabuleiro">Função <code>trocar (linha1, coluna1, linha2, coluna2, tabuleiro)</code></a></li>
<li><a href="#função-eliminar-tabuleiro">Função <code>eliminar (tabuleiro)</code></a></li>
<li><a href="#função-identificar_cadeias_horizontais-tabuleiro">Função <code>identificar_cadeias_horizontais (tabuleiro)</code></a></li>
<li><a href="#função-identificar_cadeias_verticais-tabuleiro">Função <code>identificar_cadeias_verticais (tabuleiro)</code></a></li>
<li><a href="#função-eliminar_cadeia-tabuleiro-cadeia">Função <code>eliminar_cadeia (tabuleiro, cadeia)</code></a></li>
<li><a href="#função-deslocar-tabuleiro">Função <code>deslocar (tabuleiro)</code></a></li>
<li><a href="#função-deslocar_coluna-tabuleiro-i">Função <code>deslocar_coluna (tabuleiro, i)</code></a></li>
<li><a href="#função-existem_movimentos_validos-tabuleiro">Função <code>existem_movimentos_validos (tabuleiro)</code></a></li>
<li><a href="#função-obter_dica-tabuleiro">Função <code>obter_dica (tabuleiro)</code></a></li>
</ul></li>
<li><a href="#informações-sobre-a-entrega-do-ep">Informações sobre a entrega do EP</a></li>
</ul>
</div>
<h2 id="informações-iniciais">Informações iniciais</h2>
<p>Neste EP você desenvolverá uma cópia simplificada do popular jogo Bejeweled, que chamaremos de Gemas (pedras preciosas).</p>
<p>Para isso, você deve saber:</p>
<ul>
<li>criar e manipular listas,</li>
<li>criar matrizes,</li>
<li>percorrer linhas e colunas de matrizes, e</li>
<li>escrever e utilizar funções que recebam e retornem matrizes e listas,</li>
</ul>
<p>além dos conhecimentos exigidos no EP1.</p>
<p><strong>Entrega até 4 de junho de 2017.</strong></p>
<h2 id="o-jogo">O Jogo</h2>
<p>O jogo <em>Gemas</em> consiste em um tabuleiro com <code>m</code> colunas e <code>n</code> linhas contendo gemas de <code>c</code> cores distintas. A cada passo do jogo o jogador ou jogadora deve permutar de posição duas gemas adjacentes de tal forma que se crie uma cadeia de 3 ou mais gemas da mesma cor. Quando tal cadeia é criada, as gemas correspondentes são <em>destruídas</em> (eliminadas), gerando pontos para o jogador (igual ao número de gemas destruídas) e fazendo com que as gemas que se encontram acima “caiam”, tomando o lugar das gemas destruídas. Ao cair, é possível que novas cadeias se formem, causando uma <em>reação em cadeia</em>. Os espaços vazios criados pelas gemas que caíram são então preenchidos por gemas geradas aleatoriamente. Esse passo também pode criar novas cadeias que são automaticamente eliminadas, reiniciando o ciclo.</p>
<p>Duas gemas são consideradas adjacentes se elas se encontram na mesma linha e em colunas adjacentes, ou se elas se encontram na mesma coluna e em linhas adjacentes (diagonais não fazem parte da adjacência).</p>
<p>O jogo termina quando não existem permutações que gerem cadeias.</p>
<h3 id="tabuleiro-e-gemas">Tabuleiro e gemas</h3>
<p>O tabuleiro deve ser representado por uma matriz <code>m</code>-por-<code>n</code> de strings, onde <code>m</code> e <code>n</code> são fornecidos pelo usuário. Cada tipo (cor) de gema é representado por uma letra maiúscula distinta, utilizando-se das <code>c</code> primeiras letras do alfabeto em caixa alta (<code>A</code>, <code>B</code>, <code>C</code>, …). Você pode assumir que o número de colunas e linhas é no máximo 10.</p> 
<h4 id="exemplos">Exemplos</h4>
<ol style="list-style-type: decimal">
<li>Tabuleiro 8-por-8 completo com 7 cores de gemas (o padrão em Bejeweled classic):</li>
</ol>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G A <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C C G C B B A A <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A A <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<ol start="2" style="list-style-type: decimal">
<li>Sequências de configurações com tabuleiro com 3-por-2 posições e 3 cores (<code>A</code>,<code>B</code> e <code>C</code>):</li>
</ol>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">     <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span>             <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span>              <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span>                <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span>              <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span>
   <span class="op">+-------+</span>         <span class="op">+-------+</span>          <span class="op">+-------+</span>            <span class="op">+-------+</span>          <span class="op">+-------+</span>
 <span class="dv">0</span> <span class="op">|</span> C C B <span class="op">|</span>  <span class="op">-=&gt;</span>  <span class="dv">0</span> <span class="op">|</span> C C B <span class="op">|</span> <span class="op">-=&gt;</span>    <span class="dv">0</span> <span class="op">|</span> C C B <span class="op">|</span>  <span class="op">-=&gt;</span>     <span class="dv">0</span> <span class="op">|</span>       <span class="op">|</span>  <span class="op">-=&gt;</span>   <span class="dv">0</span> <span class="op">|</span> A A B <span class="op">|</span>
 <span class="dv">1</span> <span class="op">|</span> B C A <span class="op">|</span>  <span class="op">-=&gt;</span>  <span class="dv">1</span> <span class="op">|</span> B C B <span class="op">|</span> <span class="op">-=&gt;</span>    <span class="dv">1</span> <span class="op">|</span> B C B <span class="op">|</span>  <span class="op">-=&gt;</span>     <span class="dv">1</span> <span class="op">|</span> C C B <span class="op">|</span>  <span class="op">-=&gt;</span>   <span class="dv">1</span> <span class="op">|</span> C C B <span class="op">|</span>
 <span class="dv">2</span> <span class="op">|</span> A A B <span class="op">|</span>  <span class="op">-=&gt;</span>  <span class="dv">2</span> <span class="op">|</span> A A A <span class="op">|</span> <span class="op">-=&gt;</span>    <span class="dv">2</span> <span class="op">|</span>       <span class="op">|</span>  <span class="op">-=&gt;</span>     <span class="dv">2</span> <span class="op">|</span> B C B <span class="op">|</span>  <span class="op">-=&gt;</span>   <span class="dv">2</span> <span class="op">|</span> B C B <span class="op">|</span>
   <span class="op">+-------+</span>         <span class="op">+-------+</span>          <span class="op">+-------+</span>            <span class="op">+-------+</span>          <span class="op">+-------+</span>

Estado inicial     Permutando <span class="im">as</span>      Que são então        As gemas acima     E novas gemas
                   gemas das          destruídas,          são deslocadas     são criadas
                   posições <span class="dv">1</span>,<span class="dv">2</span>       deixando             para preencher     aleatoriamente
                   e <span class="dv">2</span>,<span class="dv">2</span> cria<span class="op">-</span>se      espaços vazios       esse espaço        para preencher
                   uma cadeia de      em seus lugares                         os espaços
                   <span class="dv">3</span> gemas iguais                                             restantes</code></pre></div>
<h3 id="dicas">Dicas</h3>
<p>Durante o jogo, é possível obter dicas, que são fornecidas na forma da posição de uma gema cuja permutação com outra gema é válida. Cada dica obtida gera o desconto de 1 gema do total de pontos (dados pelo total de gemas destruídas).</p>
<h2 id="o-que-seu-programa-deve-fazer">O que seu programa deve fazer</h2>
<p>Você deverá basear a sua solução no <a href="esqueleto_ep2.py">esqueleto fornecido</a> (se você experienciar problemas ao vizualizar o arquivo, tente mudar a codificação em seu navegador ou editor de texto para UTF8). Sua tarefa será implementar as funções necessárias para que o programa implemente uma versão funcional do jogo. <strong>Todas as funções presentes no esqueleto devem estar na sua solução, com os mesmos argumentos e os mesmos valores de retorno</strong>. Você pode criar funções adicionais se desejar, que devem estar devidamente documentadas.</p>
<h3 id="função-main">Função <code>main ()</code></h3>
<p>Esta função contém o laço principal do jogo: ler comando, testar sua validade e executar comando. <strong>Sua implementação será fornecida no esqueleto do EP2 e não deve ser modificada.</strong></p>
<h3 id="função-criar-num_linhas-num_colunas">Função <code>criar (num_linhas, num_colunas)</code></h3>
<p>Cria uma matriz de <code>num_linhas</code> linhas por <code>num_colunas</code> colunas e as preenche com espaços vazios representados pela string <code>&quot; &quot;</code>.</p>
<h4 id="exemplo">Exemplo</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> tabuleiro <span class="op">=</span> criar (<span class="dv">8</span>, <span class="dv">8</span>)
<span class="op">&gt;&gt;&gt;</span> <span class="bu">print</span> (tabuleiro)
[[<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>],
 [<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>],
 [<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>],
 [<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>],
 [<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>],
 [<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>],
 [<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>],
 [<span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39; &#39;</span>]]</code></pre></div>
<h3 id="função-completar-tabuleiro-num_cores">Função <code>completar (tabuleiro, num_cores)</code></h3>
<p>Completa espaços vazios no tabuleiro gerando novas gemas cujas cores são escolhidas aleatoriamente entre as <code>num_cores</code> possíveis. <strong>Sua implementação será fornecida no esqueleto do EP2 e não deve ser modificada.</strong></p>
<h4 id="exemplo-1">Exemplo</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
   <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>       F G D B   <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> B B D F A A E   <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> A D C D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> G F G G B B A C <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> completar (tabuleiro, <span class="dv">7</span>)
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
   <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> A D F F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> B B D F A A E A <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> A D C D G A G E <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> G F G G B B A C <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> tabuleiro <span class="op">=</span> criar (<span class="dv">8</span>, <span class="dv">8</span>)
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>                 <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span>                 <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span>                 <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span>                 <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span>                 <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span>                 <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span>                 <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span>                 <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> completar (tabuleiro, <span class="dv">7</span>)
<span class="op">&gt;&gt;&gt;</span> <span class="bu">print</span> (tabuleiro)
[ [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;C&#39;</span>],
  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>],
  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>],
  [<span class="st">&#39;C&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>],
  [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>],
  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;G&#39;</span>],
  [<span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>],
  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;F&#39;</span>] ]</code></pre></div>
<h4 id="função-randrange-do-pacote-random">Função <code>randrange</code> do pacote <code>random</code></h4>
<p>Para gerar novas gemas de maneira aleatório, usamos a função <code>randrange</code>, que retorna um inteiro (<code>int</code>) em um dado intervalo. Existem duas maneiras de chamar a função:</p>
<ul>
<li><code>random.randrange(stop)</code></li>
</ul>
<p>retorna, com probabilidade uniforme, um inteiro entre <code>0</code> e <code>stop-1</code> (inclusive).</p>
<ul>
<li><code>random.randrange(start, stop[, step])</code></li>
</ul>
<p>retorna, com probabilidade uniforme, um inteiro entre <code>start</code> e <code>stop-1</code>. Se <code>step</code> for fornecido, então apenas números no interval <code>[start,start + step, start + 2step, ..., stop-1]</code> são retornados.</p>
<p>Note que essas funções propositadamente se assemelham a função <code>range</code>, que cria uma lista de inteiros.</p>
<h3 id="função-exibir-tabuleiro">Função <code>exibir (tabuleiro)</code></h3>
<p>Exibe o tabuleiro atual identificado linhas e colunas correspondentes.</p>
<h4 id="exemplo-2">Exemplo</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> tabuleiro <span class="op">=</span> [ [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;C&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39; &#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;G&#39;</span>],
                  [<span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;F&#39;</span>] ]
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G A <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C C G   C B A A <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A A <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<h3 id="função-trocar-linha1-coluna1-linha2-coluna2-tabuleiro">Função <code>trocar (linha1, coluna1, linha2, coluna2, tabuleiro)</code></h3>
<p>Tenta permutar as gemas das posições <code>linha1, coluna1</code> e <code>linha2, coluna2</code>. Se o movimento é inválido (não gera cadeias de 3 ou mais ou se as gemas não são adjacentes), retorna <code>False</code>, caso contrário retorna <code>True</code>.</p>
<h4 id="exemplo-3">Exemplo</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> tabuleiro <span class="op">=</span> [ [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;C&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;F&#39;</span>],
                  [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;G&#39;</span>],
                  [<span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;F&#39;</span>] ]
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G A <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C C G C E B A F <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A A <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> trocar (<span class="dv">0</span>, <span class="dv">2</span>, <span class="dv">1</span>, <span class="dv">2</span>, tabuleiro) <span class="co"># não altera o tabuleiro</span>
<span class="va">False</span>
<span class="op">&gt;&gt;&gt;</span> trocar (<span class="dv">3</span>, <span class="dv">2</span>, <span class="dv">3</span>, <span class="dv">2</span>, tabuleiro)
<span class="va">False</span>
<span class="op">&gt;&gt;&gt;</span> trocar (<span class="dv">3</span>, <span class="dv">2</span>, <span class="dv">3</span>, <span class="dv">3</span>, tabuleiro)
<span class="va">True</span>
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G A <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C C C G E B A F <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A A <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<h3 id="função-eliminar-tabuleiro">Função <code>eliminar (tabuleiro)</code></h3>
<p>Elimina cadeias substituindo gemas destruídas por <code>&quot; &quot;</code> e retorna número de gemas destruídas. <strong>Esta função deverá <em>necessariamente</em> fazer uso das funções:</strong></p>
<ul>
<li><code>identificar_cadeias_horizontais</code></li>
<li><code>identificar_cadeias_verticais</code></li>
<li><code>eliminar_cadeia</code></li>
</ul>
<h4 id="exemplo-4">Exemplo</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G A <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C C C G E B A A <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A A <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> eliminar (tabuleiro)
<span class="dv">6</span>
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span>       G E B A   <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A   <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>

<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro2)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B G <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E D <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F C D G A G G <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C G C C C B A C <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> eliminar (tabuleiro2)
<span class="dv">5</span>
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro2)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B G <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D   F A A E D <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F   D G A G G <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C G       B A C <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<h3 id="função-identificar_cadeias_horizontais-tabuleiro">Função <code>identificar_cadeias_horizontais (tabuleiro)</code></h3>
<p>Retorna uma lista contendo cadeias <em>horizontais</em> de 3 ou mais gemas. Cada cadeia é representada por uma lista <code>[linha, coluna_i, linha, coluna_f]</code>, onde:</p>
<ul>
<li><code>linha</code>: o número da linha das gemas cadeia</li>
<li><code>coluna_i</code>: o número da coluna da gema mais à esquerda (menor) da cadeia</li>
<li><code>coluna_f</code>: o número da coluna da gema mais à direita (maior) da cadeia</li>
</ul>
<p><em>Não modifica o tabuleiro.</em></p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> tabuleiro <span class="op">=</span> [ [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;C&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;*&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;F&#39;</span>],
                  [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;G&#39;</span>],
                  [<span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;F&#39;</span>] ]
<span class="op">&gt;&gt;&gt;</span> identificar_cadeias_horizontais (tabuleiro)
[[<span class="dv">0</span>, <span class="dv">0</span>, <span class="dv">0</span>, <span class="dv">2</span>], [<span class="dv">7</span>, <span class="dv">5</span>, <span class="dv">7</span>, <span class="dv">7</span>]]</code></pre></div>
<h3 id="função-identificar_cadeias_verticais-tabuleiro">Função <code>identificar_cadeias_verticais (tabuleiro)</code></h3>
<p>Retorna uma lista contendo cadeias <em>verticais</em> de 3 ou mais gemas. Cada cadeia é representada por uma lista <code>[linha_i, coluna, linha_f, coluna]</code>, onde:</p>
<ul>
<li><code>linha_i</code>: o número da linha da gema mais superior (menor) da cadeia</li>
<li><code>coluna</code>: o número da coluna das gemas da cadeia</li>
<li><code>linha_f</code>: o número da linha mais inferior (maior) da cadeia</li>
</ul>
<p><em>Não modifica o tabuleiro.</em></p>
<h3 id="função-eliminar_cadeia-tabuleiro-cadeia">Função <code>eliminar_cadeia (tabuleiro, cadeia)</code></h3>
<p>Elimina (substitui pela string espaço <code>&quot; &quot;</code>) as gemas compreendidas numa cadeia, representada por uma lista <code>[linha_inicio, coluna_inicio, linha_fim, coluna_fim]</code>, tal que:</p>
<ul>
<li><code>linha_i</code>: o número da linha da gema mais superior (menor) da cadeia</li>
<li><code>coluna_i</code>: o número da coluna da gema mais à esquerda (menor) da cadeia</li>
<li><code>linha_f</code>: o número da linha mais inferior (maior) da cadeia</li>
<li><code>coluna_f</code>: o número da coluna da gema mais à direita (maior) da cadeia</li>
</ul>
<p>Retorna o número de gemas eliminadas (note que se uma gema estiver em mais de uma cadeia, ela só deve é eliminada uma única vez).</p>
<p><em>Note que as funções <code>identifica_cadeias_horizontais</code> e <code>identifica_cadeias_verticais</code> retornam uma lista de cadeias (listas).</em></p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> tabuleiro <span class="op">=</span> [ [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;C&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;F&#39;</span>],
                  [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;A&#39;</span>],
                  [<span class="st">&#39;G&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;G&#39;</span>],
                  [<span class="st">&#39;E&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;D&#39;</span>, <span class="st">&#39;G&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>],
                  [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;C&#39;</span>, <span class="st">&#39;A&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;E&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;F&#39;</span>, <span class="st">&#39;F&#39;</span>]]
<span class="op">&gt;&gt;&gt;</span> eliminar_cadeia (tabuleiro, [<span class="dv">0</span>, <span class="dv">0</span>, <span class="dv">0</span>, <span class="dv">2</span>])
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>       F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G A <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C C C G E B A A <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A A <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<p>Repare que a função elimina qualquer cadeia especificada, mesmo que a cadeia não seja válida:</p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> eliminar_cadeia (tabuleiro, [<span class="dv">7</span>, <span class="dv">0</span>, <span class="dv">7</span>, <span class="dv">7</span>])
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>       F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G A <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> C C C G E B A A <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A A <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span>                 <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<h3 id="função-deslocar-tabuleiro">Função <code>deslocar (tabuleiro)</code></h3>
<p>Desloca gemas para baixo, de forma que nenhum espaço vazio apareça abaixo de uma gema. <strong>Esta função deve <em>necessariamente</em> fazer uso da função <code>deslocar_coluna</code>.</strong></p>
<h4 id="exemplo-5">Exemplo</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span>       G B B A   <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A   <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> deslocar (tabuleiro)
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>       F G D B   <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> B B D F A A E   <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> A D C D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> G F G G B B A C <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<h3 id="função-deslocar_coluna-tabuleiro-i">Função <code>deslocar_coluna (tabuleiro, i)</code></h3>
<p>Desloca as gemas na coluna i para baixo, ocupando espaços vazios abaixo.</p>
<h4 id="exemplo-6">Exemplo</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> B B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> A D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> G F G D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span>       G B B A   <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A   <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> deslocar_coluna (tabuleiro,<span class="dv">0</span>)
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>   B D F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> B D C F A A E C <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> A F G D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> G     G B B A   <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A   <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> deslocar_coluna (tabuleiro,<span class="dv">7</span>)
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>   B D F G D B   <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> B D C F A A E   <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> A F G D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> G     G B B A C <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> deslocar_coluna (tabuleiro,<span class="dv">0</span>)
<span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
    <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span>   B D F G D B   <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> B D C F A A E   <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> A F G D G A G   <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> G     G B B A C <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span></code></pre></div>
<h3 id="função-existem_movimentos_validos-tabuleiro">Função <code>existem_movimentos_validos (tabuleiro)</code></h3>
<p>Retorna <code>True</code> se existem permutações válidas e <code>False</code> caso contrário. <strong>Esta função deverá <em>necessariamente</em> utilizar a função <code>obter_dica</code>.</strong></p>
<h3 id="função-obter_dica-tabuleiro">Função <code>obter_dica (tabuleiro)</code></h3>
<p>Retorna uma dica: a posição <code>linha, coluna</code> de uma gema que faz parte de uma permutação válida.</p>
<p>Se não houver permutação válida, retorna <code>-1, -1</code>.</p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="op">&gt;&gt;&gt;</span> exibir (tabuleiro)
   <span class="dv">0</span> <span class="dv">1</span> <span class="dv">2</span> <span class="dv">3</span> <span class="dv">4</span> <span class="dv">5</span> <span class="dv">6</span> <span class="dv">7</span>
  <span class="op">+-----------------+</span>
<span class="dv">0</span> <span class="op">|</span> A D F F G D B C <span class="op">|</span>
<span class="dv">1</span> <span class="op">|</span> B B D F A A E A <span class="op">|</span>
<span class="dv">2</span> <span class="op">|</span> A D C D G A G E <span class="op">|</span>
<span class="dv">3</span> <span class="op">|</span> G F G G B B A B <span class="op">|</span>
<span class="dv">4</span> <span class="op">|</span> B D A D F D A C <span class="op">|</span>
<span class="dv">5</span> <span class="op">|</span> G D E C D B G G <span class="op">|</span>
<span class="dv">6</span> <span class="op">|</span> E C B A D G A E <span class="op">|</span>
<span class="dv">7</span> <span class="op">|</span> A C A E E A F F <span class="op">|</span>
  <span class="op">+-----------------+</span>
<span class="op">&gt;&gt;&gt;</span> obter_dica (tabuleiro)
<span class="dv">3</span>, <span class="dv">6</span>
<span class="op">&gt;&gt;&gt;</span> tabuleiro <span class="op">=</span> [ [<span class="st">&#39;A&#39;</span>, <span class="st">&#39;B&#39;</span>],
                  [<span class="st">&#39;C&#39;</span>, <span class="st">&#39;D&#39;</span>],
                  [<span class="st">&#39;B&#39;</span>, <span class="st">&#39;A&#39;</span>]]
<span class="op">&gt;&gt;&gt;</span> obter_dica (tabuleiro)
<span class="op">-</span><span class="dv">1</span>, <span class="op">-</span><span class="dv">1</span>                  </code></pre></div>
<h2 id="informações-sobre-a-entrega-do-ep">Informações sobre a entrega do EP</h2>
<p>A entrega deve ser feita até 4 de junho de 2017.</p>
<p>Sua solução deve se basear no <a href="esqueleto_ep2.py">esqueleto fornecido</a>.</p>
<p>Todo exercício-programa deve seguir as observações contidas <a href="http://www.ime.usp.br/~mac2166/infoepsPy">aqui</a>, onde estão descritas as diretrizes para forma de entrega do exercício, aspectos importantes na avaliação etc.</p>
</body>
</html>
