# Definição de uma função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Definição de uma função principal
def main():
    print("Bem-vindo ao sistema de cálculo de média!")
    nome = input("Digite seu nome: ")
    
    # Lista para armazenar as notas
    notas = []
    
    # Loop para coletar as notas do usuário
    num_notas = int(input("Quantas notas deseja inserir? "))
    for i in range(num_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    # Cálculo da média
    media = calcular_media(notas)
    
    # Estrutura de decisão para determinar a situação do aluno
    if media >= 7.0:
        situacao = "Aprovado"
    elif 5.0 <= media < 7.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    # Exibição do resultado
    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

# Execução do programa
if __name__ == "__main__":
    main()
