## QUESTÃO 1 de 2 – Lista Encadeada 
Enunciado: Com a finalidade de melhorar o atendimento e priorizar os casos mais urgentes, a direção de um hospital criou um sistema de triagem em que um profissional da saúde classifica a ordem de atendimento com base numa avaliação prévia do paciente, entregando-lhe um cartão numerado verde (V) ou amarelo (A), que define o menor ou maior grau de urgência da ocorrência, respectivamente. Para informatizar esse processo, a direção do hospital contratou você para desenvolver uma fila de chamada seguindo as seguintes regras: 
+ Pacientes com cartão numerado amarelo (A) são chamados antes dos pacientes com cartão numerado verde (V) 
+ Entre os pacientes com cartão numerado amarelo (A), os que tem numeração menor são atendidos antes. 
+ Entre os pacientes com cartão numerado verde (V), os que tem numeração menor são atendidos antes. 
+ As numerações dos cartões amarelos (A) iniciam em 201. 
+ As numerações dos cartões verdes (V) inicial em 1.

## QUESTÃO 2 de 2 – Tabela Hash 
Enunciado: Com o objetivo de criar um sistema novo de emplacamento de veículos, deputados em do Distrito Federal – DF, decidiram que o último número da placa dos veículos, irá representar o estado de registro dele. Para isso, sua equipe de desenvolvedores foi encarregada de desenvolver uma Tabela Hash com endereçamento em cadeia de 10 posições (cada posição do vetor deve ser uma lista encadeada), representando os números de 0 a 9 que irão representar os 26 estados e o Distrito Federal (total 27). 
+ A função hash deve seguir as seguintes regras: 
+ A entrada da função hash deve ser uma string com 2 letras, representando a sigla do estado e/ou distrito federal. 
+ Caso a sigla seja DF (Distrito Federal), por questões de superstição, os deputados solicitaram que o retorno da função seja 7 sempre. 
+ Caso contrário, a função deve retornar a posição com base no valor ASCII das duas letras.
