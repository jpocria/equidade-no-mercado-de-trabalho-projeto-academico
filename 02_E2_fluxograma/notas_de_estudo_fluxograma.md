# Notas de estudo - Fluxograma do analisador

## O que deve ser enviado

O arquivo oficial recomendado para envio no AVA é `fluxograma_analisador.pdf`, correspondente à V3. O PNG é uma alternativa aceita pelo enunciado.

## Como ler os símbolos

- **Elipse:** início ou fim do programa.
- **Paralelogramo:** entrada digitada pelo usuário ou mensagem exibida na tela.
- **Retângulo:** processamento interno.
- **Losango:** pergunta que possui caminhos diferentes, normalmente `Sim` e `Não`.
- **Retângulo com linhas laterais:** chamada de uma função ou subrotina.
- **Seta:** ordem de execução.

## Explicação do fluxo principal

1. O programa começa exibindo o título e o aviso ético.
2. O usuário informa o anúncio da vaga.
3. Se a entrada estiver vazia, o programa pede o texto novamente.
4. A função `normalizar_texto` converte o texto para minúsculas e remove espaços extras nas pontas.
5. A função `analisar_vaga` percorre a lista de termos e registra os encontrados.
6. Se houver resultados, o programa mostra termo, categoria, explicação e sugestão. Caso contrário, informa que nenhuma regra cadastrada foi localizada.
7. A função `calcular_percentual` prepara o resumo numérico.
8. O programa avisa que o percentual não é uma probabilidade de discriminação.
9. O usuário escolhe entre analisar outra vaga e encerrar.

## O que acontece nas funções

### `normalizar_texto`

Recebe o texto original, aplica `strip()` e `lower()` e devolve o texto normalizado. Essa função permite encontrar uma mesma expressão mesmo que o usuário use letras maiúsculas.

### `analisar_vaga`

Cria uma lista vazia e usa um `for` para verificar cada termo. Quando encontra `jovem aprendiz`, evita marcar apenas a palavra `jovem`. Para as demais regras, registra o índice da expressão encontrada e devolve a lista de resultados.

### `calcular_percentual`

Divide a quantidade de regras encontradas pelo total de regras e multiplica por 100. O valor serve somente para demonstrar a proporção das regras cadastradas que apareceu no texto.

## Divisão sugerida da explicação oral

- **João:** objetivo, entrada, validação, normalização e fluxo principal.
- **Tulio:** repetição da lista de termos, exceção contextual, resultados, percentual e limites éticos.

## Pontos importantes para responder ao professor

- O analisador não acusa empresas e não substitui uma análise jurídica.
- A busca usa regras simples porque o trabalho precisa demonstrar os fundamentos de algoritmos.
- O `for` percorre os termos; o `while` permite analisar novas vagas.
- As funções evitam repetição e deixam o código organizado.
- A expressão `jovem aprendiz` mostra que o contexto pode mudar o significado de uma palavra.
- Qualificações excessivas ficaram fora da primeira versão porque não podem ser avaliadas com segurança por uma lista simples.

