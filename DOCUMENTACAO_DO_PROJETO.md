# Documentação do projeto Equidade-A3

Este é o documento central de consulta técnica e acadêmica do projeto. Ele resume o que já foi decidido, o que está implementado e onde cada alteração deve ser feita. O documento de pesquisa original continua sendo a fonte acadêmica principal; esta documentação não o substitui.

## Sumário

- [1. Visão geral e limites éticos](#1-visão-geral-e-limites-éticos)
- [2. Estado atual](#2-estado-atual)
- [3. Estrutura dos arquivos](#3-estrutura-dos-arquivos)
- [4. Arquitetura e fluxo planejados](#4-arquitetura-e-fluxo-planejados)
- [5. Formato dos dados](#5-formato-dos-dados)
- [6. Catálogo das regras iniciais](#6-catálogo-das-regras-iniciais)
- [7. Funções, entradas e saídas](#7-funções-entradas-e-saídas)
- [8. Decisões e justificativas](#8-decisões-e-justificativas)
- [9. Relação entre pesquisa, fluxograma, código e testes](#9-relação-entre-pesquisa-fluxograma-código-e-testes)
- [10. Casos de teste](#10-casos-de-teste)
- [11. Limitações e riscos](#11-limitações-e-riscos)
- [12. Guia de manutenção](#12-guia-de-manutenção)
- [13. Uso de ferramentas de IA](#13-uso-de-ferramentas-de-ia)
- [14. Histórico da documentação](#14-histórico-da-documentação)
- [15. Revisão obrigatória do grupo](#15-revisão-obrigatória-do-grupo)

## 1. Visão geral e limites éticos

O Equidade-A3 é um projeto da disciplina Algoritmos e Programação do Centro Universitário UNA, desenvolvido por João Pedro Antunes e Tulio Amaral. A primeira versão será um programa simples em Python 3 que recebe o texto de um anúncio de vaga e procura expressões cadastradas que possam merecer revisão.

Quando uma regra for acionada, a saída deverá apresentar:

- o termo identificado;
- a categoria da regra;
- uma explicação curta;
- uma sugestão de redação baseada em competências ou atividades concretas.

O programa identifica somente **sinais textuais**. Ele não comprova discriminação, não determina a intenção de empresas ou recrutadores e não produz parecer jurídico. O resultado deve ser descrito como “potencialmente excludente”, “merece revisão” ou “depende do contexto”, seguido de revisão humana.

O percentual previsto é apenas a proporção de regras cadastradas que foram acionadas:

`percentual = quantidade de regras encontradas / total de regras * 100`

Esse número não representa probabilidade de discriminação, gravidade, culpa ou nível jurídico de risco.

### Fora do escopo da primeira versão

- interpretar todo o contexto ou a intenção do anúncio;
- tomar decisões sobre candidatos;
- emitir diagnóstico jurídico;
- consultar banco de dados, API ou serviço externo;
- usar inteligência artificial dentro do programa;
- analisar automaticamente qualificações excessivas;
- classificar anúncios como “discriminatórios” ou “não discriminatórios”.

## 2. Estado atual

Situação verificada em 15/10/2026:

| Fase | Tipo | Estado | Evidência atual | Próximo passo |
|---|---|---|---|---|
| E1 - pesquisa | Entregável oficial | Concluído | PDF original preservado sozinho em sua pasta | Usar como base conceitual e citar no relatório |
| E2 - fluxograma | Entregável oficial | Concluído | V3 oficial em PDF e PNG; notas de estudo separadas | Manter o código futuro coerente com o fluxo |
| Checkpoint preliminar | Etapa interna | Em andamento | 15 regras cadastradas em quatro listas paralelas; arquivo executável apenas conta as regras | Implementar entrada, validação e as três funções planejadas |
| E3 - código-fonte | Entregável oficial | Não iniciado | Pasta reservada, sem código final | Concluir após o checkpoint e o feedback do professor |
| Testes e ajustes | Etapa interna | Não iniciado | Casos previstos no plano e nesta documentação | Registrar resultados reais somente quando executados |
| E4 - relatório final | Entregável oficial | Não iniciado | Pasta reservada | Redigir com base no que realmente foi feito |
| E5 - apresentação | Entregável oficial | Não iniciado | Pasta reservada | Preparar demonstração e divisão de falas |

O arquivo preliminar ainda **não analisa anúncios**. No estado atual, ele define quatro listas com 15 posições correspondentes e exibe a quantidade de regras. As funções, a validação de entrada, a exceção contextual e a repetição de novas análises estão planejadas, mas ainda não foram implementadas.

## 3. Estrutura dos arquivos

| Caminho | Finalidade | Observação de manutenção |
|---|---|---|
| [`README.md`](README.md) | Porta de entrada concisa | Manter curto e apontar para os documentos detalhados |
| [`AGENTS.md`](AGENTS.md) | Regras acadêmicas, técnicas e éticas | Conferir antes de qualquer alteração |
| [`PLANO_DO_PROJETO.md`](PLANO_DO_PROJETO.md) | Cronograma, escopo e registros por fase | Atualizar quando uma etapa avançar ou uma decisão relevante mudar |
| [`DOCUMENTACAO_DO_PROJETO.md`](DOCUMENTACAO_DO_PROJETO.md) | Referência técnica e acadêmica central | Atualizar junto com mudanças de regras, funções, testes ou estrutura |
| [`01_E1_documento_de_pesquisa/`](01_E1_documento_de_pesquisa/) | E1 oficial em PDF | Manter somente o PDF original nessa pasta |
| [`02_E2_fluxograma/`](02_E2_fluxograma/) | Fluxograma V3 e notas de estudo | Alterar o fluxograma se a lógica do programa mudar |
| [`03_checkpoint_codigo_preliminar/`](03_checkpoint_codigo_preliminar/) | Versão formativa e incompleta do código | Registrar o feedback do professor antes de transformá-la em versão final |
| `04_E3_codigo_fonte/` | Destino do código-fonte oficial | A pasta aparecerá no Git quando receber o primeiro arquivo; não confundir com o checkpoint |
| `05_testes_e_ajustes/` | Registros da execução dos testes | A pasta aparecerá no Git quando receber o primeiro registro; não declarar testes como aprovados antes da execução real |
| `06_E4_relatorio_final/` | Fonte editável e PDF do relatório | A pasta aparecerá no Git quando receber o primeiro arquivo; incluir limitações, testes e apoio de IA realmente ocorrido |
| `07_E5_apresentacao/` | Slides e material de demonstração | A pasta aparecerá no Git quando receber o primeiro arquivo; manter a mesma lógica do código final |

## 4. Arquitetura e fluxo planejados

A solução foi intencionalmente limitada a conceitos adequados ao segundo período: textos, números, booleanos, listas, `input`, `print`, decisões, repetições e funções. Não haverá orientação a objetos, banco de dados, interface gráfica, API ou biblioteca externa.

### Fluxo principal

1. Exibir o título e o aviso de que a ferramenta não é parecer jurídico.
2. Ler o texto do anúncio.
3. Se a entrada estiver vazia, pedir o texto novamente.
4. Chamar `normalizar_texto(texto)`.
5. Chamar `analisar_vaga(texto_normalizado, termos)`.
6. Se houver resultados, exibir os dados de cada regra; caso contrário, informar que nenhuma regra cadastrada foi localizada.
7. Chamar `calcular_percentual(quantidade, total)`.
8. Exibir quantidade, percentual e o aviso sobre o significado limitado do percentual.
9. Perguntar se o usuário deseja analisar outra vaga.
10. Repetir ou encerrar conforme a resposta.

### Separação de responsabilidades

- O fluxo principal cuida da interação com o usuário e da repetição.
- `normalizar_texto` prepara a entrada para comparação.
- `analisar_vaga` percorre as regras, trata exceções e devolve os resultados.
- `calcular_percentual` realiza somente o cálculo numérico.
- As quatro listas guardam o conteúdo das regras; elas não devem conter lógica de execução.

Essa separação permite explicar cada parte isoladamente e facilita testes simples.

## 5. Formato dos dados

As regras iniciais estão em quatro listas paralelas:

- `termos`: expressão procurada;
- `categorias`: tipo de sinal textual;
- `explicacoes`: motivo pelo qual o trecho merece revisão;
- `sugestoes`: orientação para uma redação mais objetiva.

As informações de uma regra usam o mesmo índice nas quatro listas. Exemplo conceitual:

```text
termos[0]       -> "até 30 anos"
categorias[0]   -> "Idade"
explicacoes[0]  -> explicação referente a "até 30 anos"
sugestoes[0]    -> sugestão referente a "até 30 anos"
```

### Regra de integridade

As quatro listas devem sempre ter o mesmo tamanho. Ao incluir, remover ou reordenar uma regra, as quatro posições correspondentes precisam ser alteradas juntas. Um teste simples de manutenção deve conferir:

```text
len(termos) == len(categorias) == len(explicacoes) == len(sugestoes)
```

Esse formato foi escolhido por ser simples e compatível com o conteúdo estudado. A desvantagem é o risco de desencontro entre as listas; por isso, toda mudança deve seguir a conferência acima.

## 6. Catálogo das regras iniciais

As 15 regras abaixo são as que constam no código preliminar em 15/10/2026. A ocorrência de uma expressão apenas sinaliza que o trecho merece revisão humana.

| Nº | Termo procurado | Categoria | Explicação cadastrada | Sugestão cadastrada |
|---:|---|---|---|---|
| 1 | `até 30 anos` | Idade | A idade pode excluir pessoas que possuem as competências necessárias. | Descrever a experiência ou a competência necessária. |
| 2 | `idade máxima` | Idade | Um limite de idade merece revisão e depende do contexto da função. | Informar requisitos concretos relacionados às atividades da função. |
| 3 | `perfil jovem` | Idade | A expressão pode usar a idade como substituto de uma competência. | Substituir por comportamentos e competências observáveis. |
| 4 | `jovem` | Idade | O termo merece revisão, exceto em contextos como jovem aprendiz. | Descrever a experiência, a disponibilidade ou a competência esperada. |
| 5 | `vaga para homem` | Sexo ou gênero | A indicação de gênero pode restringir candidaturas sem necessidade. | Usar uma redação neutra e descrever as atividades da função. |
| 6 | `vaga para mulher` | Sexo ou gênero | A indicação de gênero pode restringir candidaturas sem necessidade. | Usar uma redação neutra e descrever as atividades da função. |
| 7 | `perfil masculino` | Sexo ou gênero | O perfil descrito pode associar a função a um gênero específico. | Substituir por competências profissionais observáveis. |
| 8 | `perfil feminino` | Sexo ou gênero | O perfil descrito pode associar a função a um gênero específico. | Substituir por competências profissionais observáveis. |
| 9 | `solteiro` | Estado civil ou família | O estado civil geralmente não descreve uma competência profissional. | Retirar a referência ao estado civil e manter requisitos profissionais. |
| 10 | `solteira` | Estado civil ou família | O estado civil geralmente não descreve uma competência profissional. | Retirar a referência ao estado civil e manter requisitos profissionais. |
| 11 | `sem filhos` | Estado civil ou família | A situação familiar pode excluir candidaturas sem relação com a atividade. | Retirar a referência familiar e descrever somente a disponibilidade exigida. |
| 12 | `perfeita condição física` | Deficiência ou capacidade física | A expressão pode excluir pessoas capazes de realizar as tarefas da função. | Descrever as tarefas essenciais e considerar adaptações razoáveis. |
| 13 | `aptidão plena` | Deficiência ou capacidade física | A expressão é ampla e pode desconsiderar acessibilidade e adaptações. | Descrever as tarefas essenciais e considerar acessibilidade. |
| 14 | `competitivo` | Perfil estereotipado | O termo pode reforçar um perfil estereotipado e depende do contexto. | Informar o comportamento profissional esperado de forma concreta. |
| 15 | `dominante` | Perfil estereotipado | O termo pode reforçar um perfil estereotipado e depende do contexto. | Informar o comportamento profissional esperado de forma concreta. |

### Categorias e fundamento conceitual

- **Idade:** evita usar faixa etária como substituto de experiência, disponibilidade, energia ou competência.
- **Sexo ou gênero:** orienta redação neutra e ligada às atividades da função.
- **Estado civil ou família:** evita referências pessoais sem relação necessária com o trabalho.
- **Deficiência ou capacidade física:** pede descrição das tarefas essenciais, com atenção a acessibilidade e adaptações.
- **Perfil estereotipado:** trata termos cujo efeito depende fortemente do contexto e pede comportamentos observáveis.

O documento de pesquisa também discute raça ou cor, origem e qualificações excessivas. Esses temas fundamentam o problema social, mas ainda não possuem regras cadastradas na primeira versão. Qualificações excessivas ficaram fora da análise automática porque uma busca simples por palavras não consegue determinar com segurança se um requisito é essencial ou supérfluo.

### Exceção contextual planejada

A única exceção definida até agora é `jovem aprendiz` para a regra `jovem`. Quando o texto contiver essa expressão contextualizada, a ocorrência da palavra isolada `jovem` não deverá gerar alerta por si só.

Limites da exceção:

- ela ainda não está implementada no código preliminar;
- ela não transforma todo anúncio que contenha `jovem aprendiz` em adequado;
- outras regras presentes no mesmo anúncio continuam podendo ser acionadas;
- variações de redação não previstas podem escapar da busca simples;
- um anúncio pode conter `jovem aprendiz` e, em outro trecho, usar `jovem` como perfil desejado; o grupo ainda precisa decidir como preservar o segundo alerta sem complicar demais a solução;
- novos contextos legítimos só devem virar exceção depois de discussão, justificativa e teste.

Também existe sobreposição entre `perfil jovem` e `jovem`. Uma busca simples pode acionar as duas regras para o mesmo trecho. Antes da implementação, o grupo deve decidir e documentar se deseja manter os dois alertas ou evitar a duplicidade. Qualquer escolha deverá permanecer coerente no código, nos testes e na explicação do percentual.

## 7. Funções, entradas e saídas

As três funções abaixo estão definidas no plano e no fluxograma, mas ainda não existem no código preliminar.

### `normalizar_texto(texto)`

- **Recebe:** texto original do anúncio.
- **Processa:** remove espaços no início e no final com `strip()` e converte letras para minúsculas com `lower()`.
- **Retorna:** texto normalizado.
- **Não deve:** imprimir resultados nem alterar as listas de regras.

### `analisar_vaga(texto, termos)`

- **Recebe:** texto já normalizado e a lista de termos.
- **Processa:** cria uma lista vazia, percorre as regras com `for`, verifica a exceção de `jovem aprendiz` e registra os índices encontrados.
- **Retorna:** lista de índices das regras acionadas.
- **Não deve:** afirmar que houve discriminação nem decidir a saída jurídica do caso.

O uso de índices permite recuperar categoria, explicação e sugestão na mesma posição das outras listas.

### `calcular_percentual(quantidade, total)`

- **Recebe:** quantidade de regras acionadas e total de regras cadastradas.
- **Processa:** divide a quantidade pelo total e multiplica por 100.
- **Retorna:** percentual informativo.
- **Cuidado:** se essa função puder ser chamada com `total` igual a zero, o caso deve ser tratado para evitar divisão por zero. Com o catálogo atual, o total é 15.

### Entrada do programa

- anúncio digitado ou colado como texto;
- resposta `s` ou `n` para uma nova análise.

A entrada vazia deve ser rejeitada e solicitada novamente sem encerrar com erro.

### Saída do programa

Para cada resultado:

- termo;
- categoria;
- explicação;
- sugestão.

No resumo:

- quantidade de regras acionadas;
- percentual sobre as regras cadastradas;
- aviso de que o percentual não mede discriminação;
- orientação para revisão humana.

Se nenhuma regra for localizada, a mensagem deve se limitar ao alcance do catálogo, por exemplo: “Nenhuma regra cadastrada foi localizada.” Não deve afirmar que o anúncio está livre de problemas.

## 8. Decisões e justificativas

| Decisão | Justificativa | Consequência prática |
|---|---|---|
| Usar Python 3 e biblioteca padrão | Atende à disciplina e facilita execução local, no Colab e no Replit | Não adicionar dependências externas |
| Fazer busca simples por termos | Demonstra listas, `for`, `if` e funções no nível do curso | O programa não compreenderá todo o contexto |
| Usar quatro listas paralelas | Estrutura conhecida e explicável pelo grupo | Exige manter os mesmos índices e tamanhos |
| Normalizar com `strip()` e `lower()` | Evita diferença entre maiúsculas e minúsculas e espaços externos | Não resolve acentos ausentes, pontuação ou variações de palavras |
| Retornar índices encontrados | Permite acessar os quatro dados da regra pela mesma posição | A ordem das listas precisa permanecer alinhada |
| Tratar `jovem aprendiz` como exceção | Demonstra que uma palavra pode mudar de sentido conforme o contexto | A exceção deve ser explícita e testada |
| Mostrar percentual informativo | Exercita cálculo sem fingir precisão jurídica | O aviso de limitação deve acompanhar o número |
| Não automatizar qualificações excessivas | A relevância de um requisito depende das tarefas da vaga | O tema permanece para revisão humana e discussão no relatório |
| Separar checkpoint de E3 | Preserva a evolução e o feedback formativo | O arquivo preliminar não deve ser apresentado como versão final |

## 9. Relação entre pesquisa, fluxograma, código e testes

Os artefatos devem representar a mesma lógica, mas cumprem papéis diferentes:

| Origem | Define | Deve aparecer em |
|---|---|---|
| E1 - pesquisa | Problema social, categorias, base legal, limites e supervisão humana | Regras, mensagens cautelosas, relatório e apresentação |
| E2 - fluxograma | Ordem da entrada, validação, funções, decisões, saída e repetição | Código E3 e demonstração |
| Checkpoint/E3 - código | Implementação executável das regras e do fluxo | Testes, relatório e demonstração |
| Testes | Evidência do comportamento real e das limitações | Ajustes, relatório e apresentação |

### Matriz mínima de rastreabilidade

| Requisito | Pesquisa | Fluxograma | Código atual | Teste previsto |
|---|---|---|---|---|
| Linguagem cautelosa e revisão humana | Sim | Aviso inicial e nota final | Ainda não | Conferência das mensagens |
| Normalização de maiúsculas | Diretriz técnica derivada | `normalizar_texto` | Ainda não | Letras maiúsculas |
| Busca por regras cadastradas | Categorias e exemplos | `analisar_vaga` | Somente dados cadastrados | Múltiplos alertas e texto neutro |
| Exceção `jovem aprendiz` | Exemplo de dependência de contexto | Verificação de exceções | Ainda não | Exceção contextual |
| Percentual informativo | Limite ético definido | `calcular_percentual` e aviso | Ainda não | Quantidade e percentual |
| Nova análise | Escopo do programa | Decisão final | Ainda não | Repetir ou encerrar |

Quando uma regra de negócio mudar, a sequência de atualização deve ser: fundamento e decisão documentados, fluxograma se o fluxo mudar, código, testes e depois relatório/slides. Não é necessário redesenhar o fluxograma quando mudar apenas o texto explicativo de uma regra sem alterar a lógica.

## 10. Casos de teste

Os casos abaixo são especificações. Eles só podem ser marcados como aprovados depois de execução real e registro da saída obtida.

| ID | Objetivo | Entrada principal | Resultado esperado |
|---|---|---|---|
| T01 | Múltiplas categorias | `Vaga para homem, até 30 anos, solteiro e sem filhos.` | Localizar as quatro expressões cadastradas e exibir seus dados |
| T02 | Exceção contextual | `Oportunidade para Jovem Aprendiz.` | Não acionar apenas a regra `jovem` |
| T03 | Texto neutro | `Buscamos pessoa com conhecimento em Python e disponibilidade para trabalhar à tarde.` | Informar que nenhuma regra cadastrada foi localizada |
| T04 | Entrada vazia | texto vazio ou somente espaços | Pedir o anúncio novamente, sem erro |
| T05 | Maiúsculas e minúsculas | `VAGA PARA MULHER` | Produzir o mesmo resultado de `vaga para mulher` |
| T06 | Nova análise | primeira resposta `s`, depois `n` | Repetir uma vez e então encerrar |
| T07 | Percentual com quatro regras | entrada do T01 e catálogo com 15 regras | Exibir quantidade 4 e percentual aproximado de 26,67%, conforme a formatação escolhida |
| T08 | Exceção não bloqueia outras regras | `Jovem aprendiz, vaga para homem.` | Ignorar `jovem` nesse contexto e ainda localizar `vaga para homem` |
| T09 | Palavra dentro de outra palavra | texto com sequência que contém um termo apenas como parte de outra palavra | Observar e registrar o comportamento; decidir se a busca simples é aceitável |
| T10 | Integridade das listas | comparar os quatro comprimentos | Todos devem ser iguais a 15 no catálogo atual |
| T11 | Regras sobrepostas | `Buscamos perfil jovem.` | Verificar se `perfil jovem` e `jovem` são contados; aplicar a decisão registrada pelo grupo |
| T12 | Uso misto da exceção | `Programa jovem aprendiz. Também buscamos profissional jovem para outra vaga.` | Preservar o alerta do uso não relacionado ao programa, se essa distinção for adotada pelo grupo |

### Registro futuro da execução

Para cada teste executado, registrar na pasta de testes:

- data;
- versão ou arquivo testado;
- entrada usada;
- saída esperada;
- saída obtida;
- resultado: aprovado ou precisa de ajuste;
- correção realizada, quando houver;
- nomes de quem revisou o resultado.

Não inventar resultados nem preencher como executado um teste que ainda não ocorreu.

## 11. Limitações e riscos

### Falsos positivos

Um falso positivo ocorre quando uma regra marca um uso que pode ser legítimo no contexto. Exemplos possíveis:

- `jovem` em `jovem aprendiz`, se a exceção falhar;
- `competitivo` ao descrever um mercado, e não o perfil exigido do candidato;
- uma expressão citada no anúncio para explicar uma política de não discriminação.

### Falsos negativos

Um falso negativo ocorre quando existe uma barreira, mas nenhuma regra a identifica. Exemplos possíveis:

- sinônimos ou variações não cadastradas;
- erros de digitação ou ausência de acentos;
- exclusão expressa de forma indireta;
- requisito excessivo cuja inadequação depende das tarefas reais;
- barreiras relacionadas a categorias ainda sem termos no catálogo.

### Limitações técnicas da busca

- `lower()` não elimina diferenças de acentuação.
- `strip()` remove apenas espaços nas extremidades, não reorganiza espaços internos.
- a busca por trecho pode encontrar um termo dentro de uma palavra maior;
- `perfil jovem` pode acionar também a regra mais ampla `jovem`, gerando contagem duplicada para o mesmo trecho;
- uma exceção global para `jovem aprendiz` pode esconder outro uso de `jovem` no mesmo anúncio;
- uma regra é contabilizada uma vez por índice, mesmo que o termo apareça várias vezes, se a implementação seguir o fluxo planejado;
- listas de termos envelhecem e não cobrem todas as formas de redação;
- exceções manuais também podem gerar novos falsos negativos.

### Riscos de interpretação

- tratar o percentual como “chance” ou “nível de discriminação”;
- apresentar ausência de alertas como prova de que o anúncio é adequado;
- transformar sugestão geral em obrigação jurídica;
- atribuir intenção discriminatória ao autor do anúncio;
- usar dados da pesquisa fora do recorte e da metodologia indicados no E1.

As mensagens, o relatório e a apresentação devem repetir que o resultado depende do contexto e exige revisão humana.

## 12. Guia de manutenção

### Para alterar uma regra existente

1. Localizar o mesmo índice nas quatro listas do código.
2. Alterar termo, categoria, explicação ou sugestão sem romper a correspondência.
3. Atualizar o [catálogo de regras](#6-catálogo-das-regras-iniciais).
4. Conferir se o fundamento continua coerente com o E1.
5. Executar os testes afetados e registrar resultados reais.
6. Atualizar o plano se a mudança representar uma decisão relevante da fase.

### Para adicionar ou remover uma regra

1. Registrar a justificativa e a relação com pesquisa, legislação ou decisão do grupo.
2. Alterar as quatro listas na mesma posição.
3. Conferir a igualdade dos comprimentos.
4. Atualizar o total esperado, o catálogo e os cálculos de testes.
5. Criar pelo menos um caso positivo e um caso de contexto legítimo.
6. Verificar se fluxograma, relatório ou slides precisam de ajuste.

### Para adicionar uma exceção contextual

1. Explicar qual falso positivo a exceção evita.
2. Definir exatamente a expressão e a regra afetada.
3. Implementar a condição de maneira legível dentro de `analisar_vaga`.
4. Testar a exceção isolada e junto de outra regra.
5. Documentar o risco de a exceção esconder um caso verdadeiro.

### Para alterar o fluxo do programa

1. Atualizar o plano e esta documentação.
2. Atualizar o fluxograma oficial ou preparar uma nova versão revisável.
3. Alterar o código.
4. Atualizar e executar os testes.
5. Conferir a explicação do relatório e da apresentação.

### Para avançar do checkpoint ao E3

1. Preservar o arquivo preliminar como registro da etapa formativa.
2. Registrar o feedback real do professor, se houver.
3. Criar o código final na pasta `04_E3_codigo_fonte/`.
4. Implementar as três funções com parâmetros e retornos.
5. Implementar entrada, validação, avisos, resultados e repetição.
6. Executar os testes e corrigir divergências.
7. Confirmar que João Pedro Antunes e Tulio Amaral conseguem explicar as decisões.

## 13. Uso de ferramentas de IA

Registro provisório para futura declaração no Relatório Final:

- ferramentas de IA apoiaram a organização e a revisão da documentação técnica desta etapa;
- a consolidação do catálogo inicial e sua comparação com o plano, o fluxograma e a pesquisa também receberam apoio de IA durante o desenvolvimento assistido;
- a IA não integra o programa e não analisará vagas durante sua execução;
- os integrantes devem revisar, compreender e assumir as decisões antes da entrega;
- este registro não afirma que testes, feedback do professor, coleta de anúncios ou validação externa ocorreram.

Antes do E4, João Pedro Antunes e Tulio Amaral devem conferir o histórico real das etapas e completar a declaração com precisão: em quais atividades houve apoio, o que foi revisado pelo grupo e quais decisões foram tomadas pelos integrantes. Não se deve atribuir ao grupo uma pesquisa, um teste, uma entrevista ou uma experiência que não tenha sido realizada.

## 14. Histórico da documentação

| Data | Alteração relevante | Estado |
|---|---|---|
| 15/10/2026 | E1 preservado e planejamento inicial registrado | Concluído |
| 15/10/2026 | Fluxograma V3 definido como versão oficial em PDF e PNG | Concluído |
| 15/10/2026 | Cadastro inicial de 15 regras em quatro listas paralelas | Concluído como primeira etapa do checkpoint |
| 15/10/2026 | Criação desta documentação central, atualização do README e registro no plano | Pendente de revisão do grupo |

Este histórico registra decisões do projeto, não substitui o histórico do Git e não deve ser usado para declarar atividades que não ocorreram.

## 15. Revisão obrigatória do grupo

Antes de considerar esta etapa concluída, João Pedro Antunes e Tulio Amaral devem conseguir explicar e confirmar:

- por que o programa apenas sinaliza trechos para revisão humana;
- por que as quatro listas precisam ter o mesmo tamanho e a mesma ordem;
- como cada uma das três funções recebe parâmetros e retorna um resultado;
- por que `jovem aprendiz` é uma exceção e quais são seus limites;
- como tratar a sobreposição entre `perfil jovem` e `jovem` e o uso misto de `jovem aprendiz` com outro `jovem`;
- por que o percentual não é uma probabilidade de discriminação;
- quais falsos positivos e falsos negativos são esperados;
- quais partes já estão implementadas e quais ainda são apenas planejadas;
- se as 15 regras, explicações e sugestões devem permanecer exatamente como estão;
- se o registro de participação de IA corresponde ao que realmente ocorreu.

Somente depois dessa revisão o grupo deve tratar a documentação e o catálogo como decisões compreendidas e aprovadas.
