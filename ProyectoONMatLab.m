%[][]Solo codigo nada de conclusiones o texto, para eso mirar pdf[][]%

% [*] EJER 2-3 

% Começamos nosso programa definindo as funções f e phi da instrução, para
% isso usamos a notação @(x), o que indica que a função tem x como parâmetro em sua definição
f = @(x) (x - 1).^2;
phi = @(x) max(x, 0);

% Como no exercício 3 somos solicitados a resolver o problema para valores específicos de m, n 
% e k, agora os estabelecemos no código
n = 10; % Número de pontos de observação
k = 3;  % Número de pontos a validar
m = 2;  % Número de neurônios

% A seguir somos solicitados a formar os conjuntos O de observações e T de
% validações. Para isso utilizamos as funções conjO e conjT que aparecem definidas no final do 
% código.

% Passamos os parâmetros n e f para conjO e ele irá gerar n pontos no intervalo [0,3] com o comando linspace 
% e irá avaliá-los em f, retornando tanto os pontos gerados quanto o valor da função nesses pontos. Uma vez 
% que chamamos a função conjO comentamos para que os valores não sejam modificados

% [x_obs, y_obs] = conjO(n, f); 

% Desta forma obtemos que para os valores de n procurados o conjunto O tem a seguinte forma
x_obs = [0    0.3000    0.6000    0.9000    1.2000    1.5000    1.8000    2.1000    2.4000    2.7000    3.0000];
y_obs = [1.0000    0.4900    0.1600    0.0100    0.0400    0.2500    0.6400    1.2100    1.9600    2.8900    4.0000];

% Da mesma forma, passamos os parâmetros k e f para a função conjT que gera pontos no intervalo [0,3] seguindo uma 
% distribuição uniforme graças ao comando rand. Como antes, uma vez calculado o conjunto T comentamos sobre ele para 
% que os valores não sejam modificados

% [x_val, y_val] = conjT(k, f);

% Desta forma obtemos que para os valores de k procurados o conjunto T tem a seguinte forma
x_val = [1.5323    2.4529    2.3845];
y_val = [0.2834    2.1109    1.9168];

% Depois de calcularmos os conjuntos O e T, somos solicitados a resolver o problema de minimização da afirmação. 
% O primeiro método que usaremos para obter esta solução será utilizando a função fminunc que está integrada ao Matlab.

% Inicializamos os valores aleatórios dos parâmetros a e b, usando o comando rand novamente, para iniciar o método 
% iterativo para atingir o mínimo.

% Como antes, utilizamos a técnica de comentar o código uma vez gerados esses valores para não modificá-los.

% a0 = rand(m, 1);
a0 = [0.8443    0.1948];

% b0 = rand(m, 1);
b0 = [0.2259    0.1707];

% Juntamos os vetores iniciais em um único vetor de parâmetro
params0 = [a0; b0];

% Assim que tivermos os parâmetros iniciais, definimos a função de erro chamando a função computaError e definindo 
% params como parâmetro.

% Enviamos os parâmetros params, x_obs, y_obs, phi e m para a função computeError. O que ele vai fazer é calcular a 
% função g através de dois loops for e por fim retornar o valor da função a ser minimizada, que chamamos error

errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Então para usar a função fminunc, na seção de ajuda do Matlab podemos ver que seu funcionamento é o seguinte:
% x = fminunc(fun,x0,options) minimiza fun com as opções de otimização especificadas nas opções. Afirma que 
% optimoptions devem ser usadas para configurar essas opções.

% Configuramos as opções de otimização com optimoptions
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');
% 'fminunc': nome da função de otimização para a qual as opções estão sendo definidas.
% 'Display', 'iter': quantidade de informações exibidas na janela de comando durante a otimização. 'iter' significa 
% que as informações são exibidas em cada iteração do algoritmo de otimização.
% 'Algorithm', 'quasi-newton': algoritmo de otimização a ser usado. Neste caso, o método quase-Newton.

% Ao utilizar o método quase-Newton não é necessário calcular a matriz Hessiana, mas sim aproximá-la, tornando o 
% algoritmo mais eficiente em termos de memória e tempo de cálculo.

% Depois de definirmos as opções, chamamos a função fminunc para calibrar o modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% params_opt: valores dos parâmetros que minimizam a função objetivo errorFunction. É o vetor de parâmetros 
% ótimos encontrados pelo algoritmo.
% fval:  valor da função objetivo errorFunction avaliada em params_opt, ou seja, o valor mínimo alcançado pela 
% função objetivo com os parâmetros ótimos.
% ~: nós ignoramos exitflag, esse indica o motivo pelo qual o algoritmo de otimização parou
% output: estrutura que contém informações detalhadas sobre o processo de otimização:
%   iterations: número de iterações
%   funcCount: número de availações da função objetivo errorFunction
%   Uma mensagem descrevendo por que o algoritmo parou.

% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ótimos da função objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Agora somos solicitados a representar graficamente o caso n=10 e m=2.
% Chamamos a função plotFunctions para a qual passamos os parâmetros f, a_opt, b_opt, phi e n.
% Esta função gera 100 pontos no intervalo [0,3] em que avalia a função f e
% g, usando dois loops for muito semelhantes ao que vimos antes. Então desenha a função f em azul e a função
% g em vermelho com o comando plot e as funções aparecem sobrepostas graças ao comando hold on
plotFunctions(f, a_opt, b_opt, phi, n);
% Finalmente, calculamos o erro de validação chamando novamente a função computeError mas passamos como 
% parâmetros os parâmetros ótimos obtidos com fminunc e os valores validados do conjunto T.
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);

% [*] EJER 3.D 

% Aumentamos o número de neurônios
m = 10;

% O processo a seguir é o mesmo de antes, mas com o novo m
% a0 = rand(m, 1);
a0 = [0.2277    0.4357    0.3111    0.9234    0.2434    0.1848    0.9049    0.9797    0.6421    0.4302];
% b0 = rand(m, 1);
b0 = [0.4302    0.1848    0.9049    0.9797    0.6421    0.4357    0.3111    0.9234    0.2434    0.2277];
params0 = [a0; b0];

errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor óptimo da função objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f e g para o método quase-Newton, n = 10 m = 10
plotFunctions(f, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);


% [*] EJER 4.A

% Para n=10 e m=2 repetimos o processo mas com um método diferente
m = 2;
a0 = [0.2243    0.1148];
b0 = [0.2259    0.1107];
params0 = [a0; b0];

% Neste novo método vamos usar a função fminsearch que funciona da seguinte forma
% x = fminsearch(fun,x0,options) minimiza fun com as opções de otimização especificadas na 
% estrutura de opções. Use optimset para configurar essas opções.

% Configurar opciones de optimización para fminsearch
options = optimset('Display', 'iter');

% Assim como no outro método, as opções especificam que o número de iterações seja exibido na tela.

% Realizamos calibração de modelo com fminsearch
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);
[params_opt, fval, exitflag, output] = fminsearch(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ótimo da função objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f e g para o método Nelder-Mead, n = 10 m = 2
plotFunctions(f, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);


% [*] EJER 4.B

% Parâmetros iniciais
n = 20; % Número de pontos de observação aumentado em 10
m = 2;  % Número de neurônios

% Repetimos todo o primeiro método

% Geramos o conjunto O
% [x_obs, y_obs] = conjO(n, f); 
x_obs = [0    0.1579    0.3158    0.4737    0.6316    0.7895    0.9474    1.1053    1.2632    1.4211    1.5789    1.7368    1.8947    2.0526    2.2105    2.3684    2.5263    2.6842    2.8421    3.0000];
y_obs = [1.0000    0.7091    0.4681    0.2770    0.1357    0.0443    0.0028    0.0111    0.0693    0.1773    0.3352    0.5429    0.8006    1.1080    1.4654    1.8726    2.3296    2.8366    3.3934    4.0000];

% Geramos o conjunto T
% [x_val, y_val] = conjT(k, f);
x_val = [1.5323    2.4529    2.3845];
y_val = [0.2834    2.1109    1.9168];

% Começamos o método iterativo
% a0 = rand(m, 1);
a0 = [0.8443    0.1948];
% b0 = rand(m, 1);
b0 = [0.2259    0.1707];
params0 = [a0; b0];

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ótimo da função objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f e g para o método quase-Newton, n = 20 m = 2
plotFunctions(f, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);

% Parâmetros iniciais
m = 7;  % Número de neurônios aumentado en 5

% Repetimos o  método

% Começamos o método iterativo
% a0 = rand(m, 1);
a0 = [0.8147    0.9058    0.1270    0.9134    0.3049    0.5361    0.5469];
% b0 = rand(m, 1);
b0 = [0.2785    0.5469    0.9575    0.9649    0.2528    0.8533    0.9058];
params0 = [a0; b0];

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos a calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ótimo daa função objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f e g para o método quase-Newton, n = 20 m = 7
plotFunctions(f, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);


% [*] EJER 4.C

% Definimos a função com perturbação
fhat = @(x) f(x)+rand(1, 1)/4;

% Parametros iniciais
n = 10; % Número de pontos de observação
k = 3;  % Número de pontos a validar
m = 2;  % Número de neurônioss

% Geramos os conjuntos O e T com a função fhat y f. 

% [x_obs, y_obs] = conjO(n, fhat); 
x_obs = [0    0.3333    0.6667    1.0000    1.3333    1.6667    2.0000    2.3333    2.6667    3.0000];
y_obs = [1.0243    0.4687    0.1354    0.0243    0.1354    0.4687    1.0243    1.8021    2.8021    4.0243];
% y_obs tem perturbações, assim como queríamos.

% [x_val, y_val] = conjT(k, f);
x_val = [1.5323    2.4529    2.3845];
y_val = [0.2834    2.1109    1.9168];

% Começamos o método iterativo
% a0 = rand(m, 1);
a0 = [0.8443    0.1948];
% b0 = rand(m, 1);
b0 = [0.2259    0.1707];
params0 = [a0; b0];

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos a calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ópimo da funçao objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função fhat e g para o método quase-Newton, n = 10 m = 2
plotFunctions(fhat, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);


% [*] EJER 4.D
% % % 1.
% Definimos a função que queremos aproximar f = x^3
f1 = @(x) (x).^3;

% Geramos os conjuntos O e T.

% [x_obs, y_obs] = conjO(n, f1); 
x_obs = [0    0.3333    0.6667    1.0000    1.3333    1.6667    2.0000    2.3333    2.6667    3.0000];
y_obs = [0    0.0370    0.2963    1.0000    2.3704    4.6296    8.0000   12.7037   18.9630   27.0000];


%[x_val, y_val] = conjT(k, f1);
x_val = [0.2276    0.1619    1.5924];
y_val = [0.0118    0.0042    4.0379];

% Usamos os mesmos parâmetros iniciais das outras vezes

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos a calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ópimo da funçao objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f1 e g para o método quase-Newton, n = 10 m = 2
plotFunctions(f1, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);
% % % 2.
% Definimos a função que queremos aproximar f = x(x-1)(x-2)
f2 = @(x) x.*(x-1).*(x-2);

% Geramos os conjuntos O e T.

% [x_obs, y_obs] = conjO(n, f2); 
x_obs = [0    0.3333    0.6667    1.0000    1.3333    1.6667    2.0000    2.3333    2.6667    3.0000];
y_obs = [0    0.3704    0.2963         0   -0.2963   -0.3704         0    1.0370    2.9630    6.0000];


%[x_val, y_val] = conjT(k, f2);
x_val = [1.0114    0.4865    2.3829];
y_val = [-0.0114    0.3781    1.2616];

% Usamos os mesmos parâmetros iniciais das outras vezes

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos a calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ópimo da funçao objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f2 e g para o método quase-Newton, n = 10 m = 2
plotFunctions(f2, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);
% % % 3.
% Definimos a função que queremos aproximar f = ((x-1)^2-1)^2
f3 = @(x) ((x-1).^2-1).^2;

% Geramos os conjuntos O e T.

% [x_obs, y_obs] = conjO(n, f3); 
x_obs = [0    0.3333    0.6667    1.0000    1.3333    1.6667    2.0000    2.3333    2.6667    3.0000];
y_obs = [0    0.3086    0.7901    1.0000    0.7901    0.3086         0    0.6049    3.1605    9.0000];


% [x_val, y_val] = conjT(k, f3);
x_val = [1.5856    0.4969    1.8059];
y_val = [0.4317    0.5579    0.1228];

% Usamos os mesmos parâmetros iniciais das outras vezes

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos a calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ópimo da funçao objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f3 e g para o método quase-Newton, n = 10 m = 2
plotFunctions(f3, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);
% % % 4.
% Definimos a função que queremos aproximar f = e^x
f4 = @(x) exp(x);

% Geramos os conjuntos O e T.

% [x_obs, y_obs] = conjO(n, f4); 
x_obs = [0    0.3333    0.6667    1.0000    1.3333    1.6667    2.0000    2.3333    2.6667    3.0000];
y_obs = [1.0000    1.3956    1.9477    2.7183    3.7937    5.2945    7.3891   10.3123   14.3919   20.0855];


% [x_val, y_val] = conjT(k, f4);
x_val = [1.9622    2.0676    2.2445];
y_val = [7.1152    7.9062    9.4353];

% Usamos os mesmos parâmetros iniciais das outras vezes

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos a calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ópimo da funçao objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f4 e g para o método quase-Newton, n = 10 m = 2
plotFunctions(f4, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);
% % % 5.
% Definimos a função que queremos aproximar f = sin(x)
f5 = @(x) sin(x);

% Geramos os conjuntos O e T.

%[x_obs, y_obs] = conjO(n, f5); 
x_obs = [0    0.3333    0.6667    1.0000    1.3333    1.6667    2.0000    2.3333    2.6667    3.0000];
y_obs = [0    0.3272    0.6184    0.8415    0.9719    0.9954    0.9093    0.7231    0.4573    0.1411];

%[x_val, y_val] = conjT(k, f5);
x_val = [0.3810    2.7401    1.8971];
y_val = [0.3718    0.3908    0.9472];

% Usamos os mesmos parâmetros iniciais das outras vezes

% Definimos a função de erro
errorFunction = @(params) computeError(params, x_obs, y_obs, phi, m);

% Configuramos as opções de otimização
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newton');

% Realizamos a calibração de modelo
[params_opt, fval, ~, output] = fminunc(errorFunction, params0, options);
% Extraímos os parâmetros ótimos
a_opt = params_opt(1:m);
b_opt = params_opt(m+1:end);

% Mostramos todos os resultados:
disp('Valores ótimos de a:');
disp(a_opt);
disp('Valores ótimos de b:');
disp(b_opt);
disp('Valor ópimo da funçao objetivo:');
disp(fval);
disp('Número de iterações:');
disp(output.iterations);
disp('Número de vezes que a funçao foi avaliada:');
disp(output.funcCount);
% Gráfico da função f5 e g para o método quase-Newton, n = 10 m = 2
plotFunctions(f5, a_opt, b_opt, phi, n);
% Calculamos o erro de validação
errorval = computeError(params_opt, x_val, y_val, phi, m);
disp(errorval/k^2);




% TRAMO DE DEFINCION DE FUNCIONES !!!!!!
% Todas as funções utilizadas no programa aparecem aqui, o Matlab exige que apareçam sempre definidas no final
% Função para gerar o conjunto de observações O
function [x, y] = conjO(n, f)
    x = linspace(0, 3, n);
    y = f(x);
end

% Função para gerar o conjunto de validação T
function [x, y] = conjT(k, f)
    x = 3 * rand(1, k);
    y = f(x);
end

% Função para calcular o erro, a função objetivo que queremos minimizar
function error = computeError(params, x, y, phi, m)
    a = params(1:m);
    b = params(m+1:end);
    g = zeros(size(x));
    for i = 1:length(x)
        for j = 1:m
            g(i) = g(i) + phi(a(j) * x(i) + b(j));
        end
    end
    error = sum((y - g).^2);
end

% Função para representar graficamente f e g
function plotFunctions(f, a, b, phi, ~)
    x = linspace(0, 3, 100); % Vetor de pontos para avaliar
    y_f = f(x); % Avalie f nos pontos x
    y_g = zeros(size(x)); % Inicializar y_g
    m = length(a); % Número de funções básicas

    % Calcular g(x) = sum(phi(a_j x + b_j))
    for i = 1:length(x)
        for j = 1:m
            y_g(i) = y_g(i) + phi(a(j) * x(i) + b(j));
        end
    end

    % Gráfico f(x) e g(x)
    figure;
    plot(x, y_f, 'b-', 'LineWidth', 2); hold on;
    plot(x, y_g, 'r--', 'LineWidth', 2);
    legend('f(x)', 'g(x)');
    title('Comparação de f(x) e g(x)');
    xlabel('x');
    ylabel('y');
    grid on;
    hold off;
end



