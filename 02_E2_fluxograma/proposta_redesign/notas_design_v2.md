# Notas de design - Fluxograma V2

## Objetivo da proposta

Esta versão reorganiza o mesmo algoritmo da primeira proposta. Ela não acrescenta funcionalidades ao programa. O objetivo é deixar a leitura mais natural, eliminar cruzamentos de setas e tornar o arquivo editável igual às versões em PDF e PNG.

## Organização visual

O fluxo principal está dividido em três áreas, lidas da esquerda para a direita:

1. **Entrada:** início, aviso, leitura do anúncio e validação do texto.
2. **Análise:** normalização do texto e busca das regras cadastradas.
3. **Saída:** apresentação dos resultados, cálculo do percentual, nova análise ou encerramento.

Dentro de cada área, a leitura acontece principalmente de cima para baixo. O caminho "Sim - nova análise" passa pela borda externa inferior e retorna ao bloco de leitura sem atravessar outras setas.

## Significado das formas e cores

- **Elipse azul-escura:** início ou fim do programa.
- **Paralelogramo verde:** entrada digitada ou informação exibida.
- **Losango amarelo:** decisão com caminhos diferentes.
- **Retângulo azul com linhas laterais:** chamada de função ou sub-rotina.
- **Painel cinza-claro:** agrupamento visual; não representa uma instrução do algoritmo.

As formas continuam identificando cada operação mesmo se o fluxograma for impresso em escala de cinza.

## Retornos das funções

Os blocos de sub-rotina mostram a variável que recebe cada retorno:

- `texto_normalizado = normalizar_texto(texto)`
- `resultados = analisar_vaga(texto_normalizado, termos)`
- `percentual = calcular_percentual(quantidade, total)`

Isso reforça que as funções recebem parâmetros e devolvem um resultado, conforme as regras do projeto.

## Como explicar o fluxo

1. O programa inicia e informa que a análise não é um parecer jurídico.
2. O usuário digita ou cola o texto de uma vaga.
3. Se o texto estiver vazio, o programa solicita a entrada novamente.
4. Se houver texto, `normalizar_texto` remove espaços externos e converte letras para minúsculas.
5. `analisar_vaga` percorre as regras, considera a exceção de contexto e devolve os resultados.
6. Se houver resultados, o programa mostra termo, categoria, explicação e sugestão. Caso contrário, informa que nenhuma regra cadastrada foi localizada.
7. `calcular_percentual` prepara o resumo numérico.
8. O programa deixa claro que o percentual não mede discriminação.
9. O usuário escolhe entre analisar outra vaga e encerrar.

## Quadro inferior das sub-rotinas

Os três cartões inferiores são material de apoio à leitura e não fazem parte da sequência de setas.

- **`normalizar_texto`:** prepara o texto para comparação.
- **`analisar_vaga`:** usa uma lista, um `for` e verificações simples para registrar ocorrências.
- **`calcular_percentual`:** divide a quantidade de resultados pelo total de regras e multiplica por 100.

## Divisão sugerida da apresentação

- **João:** objetivo, símbolos, área de entrada, validação e normalização.
- **Tulio:** análise das regras, apresentação dos resultados, percentual, repetição e limites éticos.

## Arquivos e formato de entrega

- O `.drawio` é a versão editável.
- O PDF vetorial em A3 paisagem é a versão recomendada para envio.
- O PNG tem 3508 x 2480 pixels e a mesma proporção A3/A4.
- As três versões usam a mesma composição, os mesmos textos e a mesma ordem de leitura.

## Conferências antes do envio

- Confirmar os nomes João Pedro Antunes e Tulio Amaral.
- Abrir o PDF e verificar se existe apenas uma página.
- Conferir se nenhuma seta atravessa outra.
- Testar a leitura em visualização A3 e em redução para A4.
- Revisar se o fluxograma e o código implementado continuam representando a mesma lógica.
- Reforçar durante a apresentação que os alertas dependem do contexto e exigem revisão humana.
