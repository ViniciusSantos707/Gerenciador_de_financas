# 💰 Gerenciador de Finanças Pessoais CLI

Um sistema simples e eficiente de **Gerenciamento de Finanças Pessoais** executado diretamente no terminal (CLI). O programa permite registrar receitas e despesas, calcula o saldo em tempo real e armazena os dados localmente de forma persistente.

## 🚀 Funcionalidades

- **Persistência de Dados:** Salva todas as transações automaticamente em um arquivo local (`financas.json`).
- **Validação de Entradas:** Impede erros de digitação (valores inválidos, letras no lugar de números ou opções inexistentes).
- **Cálculo de Saldo Automático:** Soma receitas e subtrai despesas instantaneamente.
- **Alertas de Segurança:** Exibe um aviso visual caso o saldo fique negativo.
- **Interface Amigável:** Menu interativo e simples via terminal.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca `json`** (Nativa do Python para manipulação de arquivos de dados)
- **Biblioteca `os`** (Nativa do Python para verificação do sistema de arquivos)

## 📋 Pré-requisitos

Você só precisa ter o **Python 3** instalado no seu computador. Para verificar se já possui instalado, execute o comando abaixo no terminal:

```bash
python --version
```

## 💻 Como Executar o Projeto

1. **Baixe ou clone** este repositório para a sua máquina.
2. Abra o terminal ou prompt de comando na pasta onde o arquivo do código está salvo.
3. Execute o programa com o comando:

```bash
python nome_do_seu_arquivo.py
```
*(Substitua `nome_do_seu_arquivo.py` pelo nome real do arquivo, por exemplo: `gerenciador.py`)*

## 📖 Como Usar

Ao iniciar o sistema, você verá o seguinte menu interativo:

```text
=================================
   GERENCIADOR DE FINANÇAS 1.0   
=================================
1. Adicionar Transação (Receita/Despesa)
2. Ver Extrato e Saldo Total
3. Sair do Sistema
Escolha uma opção (1-3):
```

- **Opção 1:** Digite a descrição (ex: *Salário* ou *Aluguel*), o valor (usando ponto para centavos, ex: *1500.50*) e o tipo (`R` para Receitas ou `D` para Despesas).
- **Opção 2:** Exibe uma lista numerada de todas as movimentações e o saldo final acumulado.
- **Opção 3:** Salva os dados de forma segura e encerra a execução do aplicativo.

## 📂 Estrutura do Arquivo de Dados

Os dados são salvos no mesmo diretório do script, estruturados da seguinte forma dentro do arquivo `financas.json`:

```json
[
    {
        "descricao": "Salário",
        "valor": 3000.0,
        "tipo": "Receita"
    },
    {
        "descricao": "Supermercado",
        "valor": -350.25,
        "tipo": "Despesa"
    }
]
```

## 📝 Licença

Este projeto é de código aberto e livre para modificações e estudos.
