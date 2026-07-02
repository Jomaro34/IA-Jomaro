# Router simples do IA-JOMARO
# Simula a escolha de modelo (AMÁLIA, Llama, Mistral)

def escolher_modelo(pergunta: str) -> str:
    pergunta = pergunta.lower()

    # Regras simples de routing
    if any(palavra in pergunta for palavra in ["escreve", "texto", "português", "resumo", "explica"]):
        return "AMÁLIA (linguagem e português europeu)"

    elif any(palavra in pergunta for palavra in ["código", "python", "programa", "erro", "algoritmo"]):
        return "Llama (programação e lógica)"

    elif any(palavra in pergunta for palavra in ["rápido", "simples", "lista", "curto"]):
        return "Mistral (tarefas leves)"

    else:
        return "Llama (default - raciocínio geral)"


# 🔥 Testes rápidos
if __name__ == "__main__":
    perguntas = [
        "Explica inteligência artificial em português",
        "Escreve um código em Python para ordenar uma lista",
        "Dá-me uma lista rápida de ideias de projetos",
        "O que é um modelo de linguagem?"
    ]

    for p in perguntas:
        modelo = escolher_modelo(p)
        print(f"Pergunta: {p}")
        print(f"Modelo escolhido: {modelo}")
        print("-" * 50)
