# Sistema de Gestão de Peças - Linha de Montagem
# Trabalho de Algoritmos e Lógica de Programação

# listas principais que vao guardar os dados
pecas_cadastradas = []
caixas_fechadas = []

# caixa atual que ta sendo preenchida
caixa_atual = []
numero_caixa = 1


# verifica se a peca passa nos criterios de qualidade
def verificar_peca(peso, cor, comprimento):
    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("peso fora do limite (deve ser entre 95g e 105g)")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("cor invalida (deve ser azul ou verde)")

    if comprimento < 10 or comprimento > 20:
        motivos.append("comprimento fora do limite (deve ser entre 10cm e 20cm)")

    if len(motivos) == 0:
        return True, []
    else:
        return False, motivos


# coloca a peca aprovada na caixa, fecha se tiver cheio
def colocar_na_caixa(peca):
    global caixa_atual, numero_caixa, caixas_fechadas

    caixa_atual.append(peca["id"])

    # se a caixa chegou em 10 pecas, fecha ela e abre uma nova
    if len(caixa_atual) == 10:
        caixas_fechadas.append({
            "numero": numero_caixa,
            "pecas": caixa_atual.copy()
        })
        print(f"\n  [!] Caixa {numero_caixa} fechada com 10 pecas! Abrindo caixa {numero_caixa + 1}...")
        caixa_atual = []
        numero_caixa += 1


def cadastrar_peca():
    print("\n--- Cadastrar Nova Peca ---")

    id_peca = input("ID da peca: ").strip()

    # verifica se ja existe uma peca com esse id
    for p in pecas_cadastradas:
        if p["id"] == id_peca:
            print("Ja existe uma peca com esse ID!")
            return

    try:
        peso = float(input("Peso (em gramas): "))
        comprimento = float(input("Comprimento (em cm): "))
    except ValueError:
        print("Valor invalido! Digite numeros para peso e comprimento.")
        return

    cor = input("Cor da peca: ").strip()

    aprovada, motivos = verificar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "aprovada": aprovada,
        "motivos": motivos
    }

    pecas_cadastradas.append(peca)

    if aprovada:
        print(f"\n  APROVADA! Peca {id_peca} adicionada na caixa {numero_caixa}.")
        colocar_na_caixa(peca)
    else:
        print("\n  REPROVADA! Motivo(s):")
        for m in motivos:
            print(f"    - {m}")


def listar_pecas():
    print("\n--- Lista de Pecas ---")

    if len(pecas_cadastradas) == 0:
        print("Nenhuma peca cadastrada ainda.")
        return

    aprovadas = [p for p in pecas_cadastradas if p["aprovada"]]
    reprovadas = [p for p in pecas_cadastradas if not p["aprovada"]]

    print(f"\n  APROVADAS ({len(aprovadas)}):")
    if len(aprovadas) == 0:
        print("    Nenhuma")
    else:
        for p in aprovadas:
            print(f"    ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")

    print(f"\n  REPROVADAS ({len(reprovadas)}):")
    if len(reprovadas) == 0:
        print("    Nenhuma")
    else:
        for p in reprovadas:
            print(f"    ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
            for m in p["motivos"]:
                print(f"      -> {m}")


def remover_peca():
    global caixa_atual

    print("\n--- Remover Peca ---")
    id_peca = input("Digite o ID da peca que deseja remover: ").strip()

    encontrou = False
    for p in pecas_cadastradas:
        if p["id"] == id_peca:
            encontrou = True

            # se ela estava aprovada, tira da caixa atual tambem
            if p["aprovada"] and id_peca in caixa_atual:
                caixa_atual.remove(id_peca)

            pecas_cadastradas.remove(p)
            print(f"Peca {id_peca} removida com sucesso!")
            break

    if not encontrou:
        print("Peca nao encontrada.")


def listar_caixas():
    print("\n--- Caixas Fechadas ---")

    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa foi fechada ainda.")
    else:
        for c in caixas_fechadas:
            print(f"\n  Caixa {c['numero']} - {len(c['pecas'])} pecas:")
            print(f"    Pecas: {', '.join(c['pecas'])}")

    # mostra tambem a caixa que ta aberta no momento
    if len(caixa_atual) > 0:
        print(f"\n  Caixa {numero_caixa} (aberta) - {len(caixa_atual)}/10 pecas:")
        print(f"    Pecas: {', '.join(caixa_atual)}")
    else:
        print(f"\n  Caixa {numero_caixa} (aberta) - vazia")


def gerar_relatorio():
    print("\n========== RELATORIO FINAL ==========")

    total = len(pecas_cadastradas)
    aprovadas = [p for p in pecas_cadastradas if p["aprovada"]]
    reprovadas = [p for p in pecas_cadastradas if not p["aprovada"]]

    print(f"Total de pecas cadastradas : {total}")
    print(f"Total de pecas aprovadas   : {len(aprovadas)}")
    print(f"Total de pecas reprovadas  : {len(reprovadas)}")

    # conta quantas caixas foram usadas (fechadas + a atual se tiver algo)
    total_caixas = len(caixas_fechadas)
    if len(caixa_atual) > 0:
        total_caixas += 1

    print(f"Caixas utilizadas          : {total_caixas}")
    print(f"  - Caixas fechadas        : {len(caixas_fechadas)}")
    if len(caixa_atual) > 0:
        print(f"  - Caixa em aberto       : 1 ({len(caixa_atual)} pecas)")

    if len(reprovadas) > 0:
        print("\nMotivos de reprovacao:")
        # conta quantas vezes cada motivo apareceu
        contagem = {}
        for p in reprovadas:
            for m in p["motivos"]:
                if m in contagem:
                    contagem[m] += 1
                else:
                    contagem[m] = 1

        for motivo, qtd in contagem.items():
            print(f"  - {motivo}: {qtd} vez(es)")

    print("=====================================")


# menu principal
def menu():
    while True:
        print("\n====== SISTEMA DE GESTAO DE PECAS ======")
        print("1. Cadastrar nova peca")
        print("2. Listar pecas aprovadas/reprovadas")
        print("3. Remover peca cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatorio final")
        print("0. Sair")
        print("=========================================")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida! Tente novamente.")


# inicia o programa
menu()
