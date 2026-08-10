# Variáveis
velocidade_internet = 400
print(velocidade_internet)

# Números inteiros(int)
idade = 15

# Números decimais(float)
nota = 8.5

# Textos(string)(str)
nome_completo = "Felipe Bravo"

# Booleanos(True ou False)
pode_entrar = True

print(type(idade))
print(type(nota))
print(type(nome_completo))
print(type(pode_entrar))

# problema 1 - Valor por hora
# Escreva um programa que retorna o valor hora de uma funcionário
# com  base no seu salário mensal e horas trabalhadas por mês



'''
# Método 5Q's para montar um algoritimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreenda completamente o problema.)

1. Quais são os dados de entrada necessários?
- Salário mensal
- Horas trabalhadas por mês

2. O que devo fazer com estes dados?
- Calcular o valor por hora

3. Quais são as restrições deste problema?
- Precisa ter um valor do salário mensal
- Precisa ter um valor das horas trabalhadas por mês

4. Qual é o resultado esperado?
- Exibir o valor por hora da pessoa com base no seu salário mensal e horas trabalhadas por mês

5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
- receber salário mensal
- receber horas trabalhadas por mês
- calcular o valor por hora
- exibir o valor por hora

'''

salario_mensal = float(input('Digite o valor do seu salário mensal: '))
horas_trabalhadas_por_mes = int(input('Digite a quantidade de horas trabalhadas por mês: '))

valor_por_hora = salario_mensal / horas_trabalhadas_por_mes

print(valor_por_hora)

