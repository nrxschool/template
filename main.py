import os

# Estrutura do curso ""
estrutura = {
    "mod1": {
        "nome": "Introdução a Web3",
        "aulas": [
            "Introdução a web3",
            "O que é Criptografia",
            "O que é uma Wallet",
            "O que é um Dapp",
        ],
    },
    "mod2": {
        "nome": "Arquitetura de Dapp",
        "aulas": [
            "Login e connect Wallet",
            "Interação com blockchains (Leituras)",
            "Interação com blockchains (Escrita)",
            "Construindo nosso primeiro Dapp (Configuração | React)",
        ],
    },
    # ....
}

# Criar estrutura de diretórios e arquivos
for mod, dados in estrutura.items():
    modulo_path = os.path.join(os.getcwd(), mod)
    os.makedirs(modulo_path, exist_ok=True)

    for idx, aula in enumerate(dados["aulas"], start=1):
        aula_path = os.path.join(modulo_path, f"aula{idx}")
        os.makedirs(aula_path, exist_ok=True)
        roteiro_path = os.path.join(aula_path, "README.md")

        with open(roteiro_path, "w", encoding="utf-8") as f:
            f.write(f"# {aula}\n\nConteúdo da aula {idx} do módulo {dados['nome']}.")

print("Estrutura de aulas criada com sucesso!")
