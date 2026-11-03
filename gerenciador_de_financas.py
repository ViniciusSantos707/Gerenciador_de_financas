import json
import os

# Nome do arquivo onde os dados serão salvos no computador
ARQUIVO_DADOS = "financas.json"

def carregar_dados():
    """Carrega as transações do arquivo JSON automaticamente se ele existir."""
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("⚠️ Erro ao ler o arquivo de dados. Iniciando um novo.")
            return []
    return []

def salvar_dados(transacoes):
    """Salva a lista de transações no arquivo JSON."""
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(transacoes, arquivo, indent=4, ensure_ascii=False)
    except IOError:
        print("❌ Erro ao salvar os dados no disco.")

def adicionar_transacao(transacoes):
    """Adiciona uma nova entrada (receita) ou saída (despesa)."""
    print("\n--- ADICIONAR TRANSAÇÃO ---")
    descricao = input("Descrição da transação (Ex: Salário, Aluguel): ").strip()
    
    # Validação para garantir que o usuário digite um número válido
    while True:
        try:
            valor = float(input("Valor (utilize ponto para centavos, ex: 50.50): "))
            if valor <= 0:
                print("⚠️ O valor deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("❌ Entrada inválida. Digite apenas números.")

    # Validação para garantir o tipo correto
    while True:
        tipo = input("Tipo (R para Receita / D para Despesa): ").strip().upper()
        if tipo in ["R", "D"]:
            break
        print("❌ Opção inválida. Digite R ou D.")

    # Monta a estrutura da transação aplicando sinal negativo para despesas
    nova_transacao = {
        "descricao": descricao,
        "valor": valor if tipo == "R" else -valor,
        "tipo": "Receita" if tipo == "R" else "Despesa"
    }

    transacoes.append(nova_transacao)
    salvar_dados(transacoes)
    print(f"✅ '{descricao}' registrada com sucesso!")

def listar_transacoes(transacoes):
    """Lista o histórico e calcula o saldo em tempo real."""
    print("\n--- EXTRATO FINANCEIRO ---")
    if not transacoes:
        print("Nenhuma transação cadastrada até o momento.")
        return

    saldo = 0.0
    for i, t in enumerate(transacoes, 1):
        sinal = "+" if t["valor"] > 0 else ""
        print(f"{i}. {t['descricao']} | {t['tipo']} | R$ {sinal}{t['valor']:.2f}")
        saldo += t["valor"]

    print("-" * 40)
    print(f"💰 SALDO ATUAL: R$ {saldo:.2f}")
    if saldo < 0:
        print("⚠️ Atenção: Seu saldo está negativo!")

def principal():
    """Menu principal interativo via terminal."""
    transacoes = carregar_dados()

    while True:
        print("\n=================================")
        print("   GERENCIADOR DE FINANÇAS 1.0   ")
        print("=================================")
        print("1. Adicionar Transação (Receita/Despesa)")
        print("2. Ver Extrato e Saldo Total")
        print("3. Sair do Sistema")
        
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            adicionar_transacao(transacoes)
        elif opcao == "2":
            listar_transacoes(transacoes)
        elif opcao == "3":
            print("👋 Sistema encerrado. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()
