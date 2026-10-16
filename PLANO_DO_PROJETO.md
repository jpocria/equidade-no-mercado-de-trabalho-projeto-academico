# Plano do Projeto A3 - Equidade no Mercado de Trabalho

## 1. Objetivo

Desenvolver, em Python 3, um programa simples que analise o texto de um anúncio de vaga e destaque termos potencialmente excludentes. A ferramenta deve explicar o motivo do alerta e sugerir revisão, sem afirmar que houve discriminação.

## 2. Escopo da primeira versão

### Entrada

- Um anúncio digitado ou colado em uma única entrada de texto.
- Uma resposta `s` ou `n` para decidir se outra vaga será analisada.

### Processamento

- Remover espaços no início e no final e converter o texto para minúsculas.
- Percorrer uma lista simples de termos.
- Ignorar a expressão contextualizada `jovem aprendiz` ao avaliar o termo `jovem`.
- Registrar cada regra localizada.
- Calcular a quantidade e o percentual de regras acionadas.

### Saída

Para cada regra encontrada, mostrar:

- termo identificado;
- categoria;
- explicação curta;
- sugestão de revisão.

Ao final, mostrar a quantidade e o percentual das expressões cadastradas encontradas. O percentual não representa probabilidade de discriminação nem nível jurídico de risco.

## 3. Regras iniciais

| Categoria | Expressões iniciais | Orientação geral |
|---|---|---|
| Idade | `até 30 anos`, `idade máxima`, `perfil jovem`, `jovem` | Descrever experiência, disponibilidade ou competência sem usar idade como substituto. |
| Sexo ou gênero | `vaga para homem`, `vaga para mulher`, `perfil masculino`, `perfil feminino` | Utilizar redação neutra e requisitos relacionados às atividades. |
| Estado civil ou família | `solteiro`, `solteira`, `sem filhos` | Retirar referências à situação familiar que não sejam necessárias para a função. |
| Deficiência ou capacidade física | `perfeita condição física`, `aptidão plena` | Descrever tarefas essenciais e considerar acessibilidade e adaptações. |
| Perfil estereotipado | `competitivo`, `dominante` | Preferir comportamentos observáveis e competências profissionais. |

## 4. Funções planejadas

- `normalizar_texto(texto)`: recebe o anúncio e retorna a versão preparada para comparação.
- `analisar_vaga(texto, termos)`: percorre as regras e retorna os índices das expressões encontradas.
- `calcular_percentual(quantidade, total)`: retorna o percentual de regras acionadas.

## 5. Fases e artefatos

### Fase 1 - E1: Documento de pesquisa

- **Status:** concluído.
- **Entrega oficial:** PDF de contextualização do problema.
- **Regra:** manter o arquivo original sozinho na pasta.

### Fase 2 - E2: Fluxograma

- **Prazo operacional:** 16/10/2026.
- **Entrega oficial:** PDF ou PNG.
- **Material de apoio:** notas de estudo para orientar a explicação do grupo.
- **Critério:** representar sequência, decisões, repetições e funções com simbologia correta.
- **Registro de 15/10/2026:** a V3 foi definida como versão oficial em PDF vetorial A3 e PNG. O redesenho preserva as três áreas, amplia as margens internas, separa melhor os conectores e foi conferido em tamanho A3 e em redução simulada para A4.

### Fase 3 - Checkpoint de código preliminar

- **Janela:** 26 a 30/10/2026.
- Implementar entrada, validação, normalização, condicionais e repetições.
- Apresentar uma versão incompleta, mas executável, para obter feedback do professor.
- Registrar o feedback antes de alterar a versão final.
- **Registro de 15/10/2026:** iniciada a versão preliminar com 15 regras organizadas em quatro listas paralelas: termos, categorias, explicações e sugestões. A primeira etapa foi executada para conferir a quantidade de regras cadastradas.

### Fase 4 - E3: Código-fonte

- **Janela:** 09 a 13/11/2026.
- Concluir as três funções, os avisos éticos e a repetição de novas análises.
- Entregar arquivo `.py` funcional e comentado.
- Manter o código compatível com instalação local, Google Colab e Replit.

### Fase 5 - Testes e ajustes

- **Janela:** 16 a 20/11/2026.
- Executar e documentar os casos de teste definidos neste plano.
- Registrar entrada, saída esperada, saída obtida e correção realizada.
- Conferir correspondência entre o código e o fluxograma.

### Fase 6 - E4: Relatório final

- **Janela:** 23 a 27/11/2026.
- Descrever o problema, a solução, as decisões, os testes e a divisão de tarefas.
- Analisar limites, falsos positivos, falsos negativos, acessibilidade e impacto social.
- Declarar de forma objetiva como ferramentas de IA apoiaram o trabalho.
- Gerar fonte editável e PDF final.

### Fase 7 - E5: Apresentação

- **Janela:** 30/11 a 05/12/2026.
- Preparar apresentação de aproximadamente 10 minutos e reservar tempo para perguntas.
- Incluir problema social, fluxograma, código em funcionamento e análise crítica.
- Dividir a fala entre João e Tulio e ensaiar a demonstração ao vivo.

## 6. Casos de teste obrigatórios

1. **Múltiplos alertas:** `Vaga para homem, até 30 anos, solteiro e sem filhos.` Deve localizar várias categorias.
2. **Exceção contextual:** `Oportunidade para Jovem Aprendiz.` Não deve gerar alerta apenas pela palavra `jovem`.
3. **Texto neutro:** anúncio baseado em competências deve informar que nenhuma regra foi localizada.
4. **Entrada vazia:** o programa deve pedir novamente o texto sem apresentar erro.
5. **Letras maiúsculas:** o resultado deve ser igual ao da versão em minúsculas.
6. **Nova análise:** o programa deve repetir ou encerrar de acordo com a resposta do usuário.

## 7. Limitações que devem ser mantidas transparentes

- A busca por palavras não compreende todo o contexto da vaga.
- Uma expressão pode ser adequada em um contexto e inadequada em outro.
- O programa pode gerar falsos positivos e falsos negativos.
- O percentual exibido mede apenas quantas regras cadastradas foram acionadas.
- Qualificações excessivas exigem leitura contextual e não serão classificadas automaticamente na primeira versão.
- A conclusão final sempre depende de revisão humana.

## 8. Controle de alinhamento

Antes de finalizar cada fase, confirmar:

- a lógica ainda corresponde ao fluxograma;
- as categorias ainda correspondem ao documento de pesquisa;
- as saídas usam linguagem cautelosa;
- os integrantes conseguem explicar o artefato;
- o arquivo está no formato solicitado e abre corretamente.

## 9. Controle de versão no GitHub

- Manter o projeto em um repositório do GitHub para registrar a evolução do trabalho.
- Fazer commits pequenos e descritivos ao concluir partes compreendidas e revisadas pelo grupo.
- Não criar alterações artificiais apenas para aumentar a quantidade de contribuições.
- Usar o histórico para mostrar a passagem entre pesquisa, fluxograma, código, testes, relatório e apresentação.
- Não publicar arquivos temporários, configurações locais ou dados sensíveis.
- Registrar no texto dos commits o que realmente foi produzido ou revisado pelo grupo.

