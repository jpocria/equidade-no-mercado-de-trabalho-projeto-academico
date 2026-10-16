"""Versão preliminar do analisador de anúncios de vaga."""

# As informações de uma mesma regra ocupam a mesma posição nas quatro listas.
termos = [
    "até 30 anos",
    "idade máxima",
    "perfil jovem",
    "jovem",
    "vaga para homem",
    "vaga para mulher",
    "perfil masculino",
    "perfil feminino",
    "solteiro",
    "solteira",
    "sem filhos",
    "perfeita condição física",
    "aptidão plena",
    "competitivo",
    "dominante",
]

categorias = [
    "Idade",
    "Idade",
    "Idade",
    "Idade",
    "Sexo ou gênero",
    "Sexo ou gênero",
    "Sexo ou gênero",
    "Sexo ou gênero",
    "Estado civil ou família",
    "Estado civil ou família",
    "Estado civil ou família",
    "Deficiência ou capacidade física",
    "Deficiência ou capacidade física",
    "Perfil estereotipado",
    "Perfil estereotipado",
]

explicacoes = [
    "A idade pode excluir pessoas que possuem as competências necessárias.",
    "Um limite de idade merece revisão e depende do contexto da função.",
    "A expressão pode usar a idade como substituto de uma competência.",
    "O termo merece revisão, exceto em contextos como jovem aprendiz.",
    "A indicação de gênero pode restringir candidaturas sem necessidade.",
    "A indicação de gênero pode restringir candidaturas sem necessidade.",
    "O perfil descrito pode associar a função a um gênero específico.",
    "O perfil descrito pode associar a função a um gênero específico.",
    "O estado civil geralmente não descreve uma competência profissional.",
    "O estado civil geralmente não descreve uma competência profissional.",
    "A situação familiar pode excluir candidaturas sem relação com a atividade.",
    "A expressão pode excluir pessoas capazes de realizar as tarefas da função.",
    "A expressão é ampla e pode desconsiderar acessibilidade e adaptações.",
    "O termo pode reforçar um perfil estereotipado e depende do contexto.",
    "O termo pode reforçar um perfil estereotipado e depende do contexto.",
]

sugestoes = [
    "Descrever a experiência ou a competência necessária.",
    "Informar requisitos concretos relacionados às atividades da função.",
    "Substituir por comportamentos e competências observáveis.",
    "Descrever a experiência, a disponibilidade ou a competência esperada.",
    "Usar uma redação neutra e descrever as atividades da função.",
    "Usar uma redação neutra e descrever as atividades da função.",
    "Substituir por competências profissionais observáveis.",
    "Substituir por competências profissionais observáveis.",
    "Retirar a referência ao estado civil e manter requisitos profissionais.",
    "Retirar a referência ao estado civil e manter requisitos profissionais.",
    "Retirar a referência familiar e descrever somente a disponibilidade exigida.",
    "Descrever as tarefas essenciais e considerar adaptações razoáveis.",
    "Descrever as tarefas essenciais e considerar acessibilidade.",
    "Informar o comportamento profissional esperado de forma concreta.",
    "Informar o comportamento profissional esperado de forma concreta.",
]

print("Primeira etapa do analisador de vagas")
print("Regras cadastradas:", len(termos))

