import sys

# Função para ler os dados do STDIN
def ler_dados_csv():
    dados = []
    for linha in sys.stdin:
        # Dividir a linha em colunas
        colunas = linha.strip().split(',')
        if colunas[0] == "_id":
            continue
        else:
            dado = {
                "_id": colunas[0],
                "index": int(colunas[1]),
                "dataEMD": colunas[2],
                "nome/primeiro": colunas[3],
                "nome/último": colunas[4],
                "idade": int(colunas[5]),
                "género": colunas[6],
                "morada": colunas[7],
                "modalidade": colunas[8],
                "clube": colunas[9],
                "email": colunas[10],
                "federado": colunas[11] == "true",
                "resultado": colunas[12] == "true"
            }
            dados.append(dado)
    return dados

# Ler os dados do STDIN
dados = ler_dados_csv()

# Extrair as modalidades desportivas únicas
modalidades = set()
for dado in dados:
    modalidades.add(dado["modalidade"])

# Ordenar as modalidades alfabeticamente
modalidades_ordenadas = sorted(modalidades)

print("Lista ordenada alfabeticamente das modalidades desportivas:")
for modalidade in modalidades_ordenadas:
    print(modalidade)


# Calcular as percentagens de atletas aptos e inaptos
total_atletas = len(dados)
total_aptos = sum(1 for dado in dados if dado["resultado"])
total_inaptos = total_atletas - total_aptos

percentagem_aptos = (total_aptos / total_atletas) * 100
percentagem_inaptos = (total_inaptos / total_atletas) * 100

print("\nPercentagem de atletas aptos:", percentagem_aptos)
print("Percentagem de atletas inaptos:", percentagem_inaptos)

# Distribuição de atletas por escalão etário (intervalo de 5 anos)
escaloes_etarios = {}
for dado in dados:
    idade = dado["idade"]
    escalao = idade // 5 * 5  # Agrupar por intervalo de 5 anos
    escaloes_etarios[escalao] = escaloes_etarios.get(escalao, 0) + 1

print("\nDistribuição de atletas por escalão etário:")
for escalao, quantidade in sorted(escaloes_etarios.items()):
    print(f"[{escalao}-{escalao + 4}]: {quantidade}")
