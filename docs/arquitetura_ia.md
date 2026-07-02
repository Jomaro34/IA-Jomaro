# Arquitetura de IA do IA-JOMARO

## 🎯 Objetivo

Definir como o IA-JOMARO utiliza diferentes modelos de Inteligência Artificial de forma modular, permitindo trocar, combinar e escalar capacidades sem depender de um único modelo.

---

# 🧠 Princípio base

O IA-JOMARO não é um único modelo de IA.

É um sistema de orquestração de modelos especializados.

Cada modelo tem um papel específico.

---

# 🧩 Modelos disponíveis

## 🇵🇹 AMÁLIA

### Função principal:
- Linguagem em português europeu (pt-PT)
- Escrita de textos naturais
- Comunicação com utilizador
- Resumos de documentos em português
- Contexto cultural português

### Não deve ser usada para:
- programação avançada
- raciocínio matemático complexo
- tarefas técnicas pesadas

---

## 🧠 Llama (Meta)

### Função principal:
- raciocínio lógico
- programação (Python, JS, etc.)
- análise técnica
- resolução de problemas complexos

---

## ⚙️ Mistral

### Função principal:
- eficiência em tarefas rápidas
- execução local
- processamento leve
- apoio a agentes técnicos

---

# 🔄 Regra de decisão (Routing)

Quando o utilizador faz um pedido, o sistema IA-JOMARO deve decidir:

- Se é linguagem natural em português → usar AMÁLIA
- Se é código ou lógica → usar Llama
- Se é tarefa leve ou repetitiva → usar Mistral

---

# 🤖 Arquitetura de agentes

Cada agente do IA-JOMARO pode escolher ou sugerir o modelo mais adequado:

## Assistente Principal
- coordena todos os agentes
- decide qual modelo usar

## Agente Investigador
- analisa informação
- não executa código

## Agente Programador
- usa Llama/Mistral
- foca em código e automação

## Agente de Comunicação (futuro)
- usa AMÁLIA
- foco em português europeu

---

# 🧠 Filosofia do sistema

- Nenhum modelo é suficiente sozinho
- A inteligência vem da combinação dos modelos
- O sistema deve ser flexível e evolutivo
- O IA-JOMARO deve poder mudar de modelos sem reescrever o projeto

---

# 🚀 Evolução futura

## Próximos passos possíveis:
- Sistema automático de routing (router inteligente)
- Memória com RAG (documentos do utilizador)
- Agentes autónomos
- Integração direta com AMÁLIA local ou API
