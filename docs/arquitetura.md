## agentes/

Contém os agentes especializados do IA-JOMARO.

Cada agente tem uma função específica e pode ser utilizado de forma independente ou em conjunto com outros agentes.

Exemplos:
- Assistente Principal
- Programador
- Professor
- Investigador
- Escritor

---

## prompts/

Guarda os prompts reutilizáveis do projeto.

Os prompts são instruções que ajudam os modelos de IA a responder de forma consistente.

---

## conhecimento/

Base de conhecimento do IA-JOMARO.

Esta pasta irá armazenar documentos, notas, PDFs e outras informações que poderão ser utilizadas pelos agentes para responder com maior contexto.

No futuro, será a base para implementar um sistema RAG (Retrieval-Augmented Generation).

---

## scripts/

Contém o código e as ferramentas do projeto.

Aqui serão desenvolvidos programas para:
- ligar modelos de IA;
- automatizar tarefas;
- processar documentos;
- integrar APIs;
- executar agentes.

---

## testes/

Área de experimentação.

Utilizada para testar modelos, prompts, agentes e novas funcionalidades antes de serem integrados no projeto.

---

## diario/

Registo da evolução do projeto.

Serve para documentar:
- decisões tomadas;
- problemas encontrados;
- soluções implementadas;
- aprendizagens.

---

# Arquitetura Geral

          Utilizador
               │
               ▼
    Assistente Principal
               │
     ┌─────────┼─────────┐
     ▼         ▼         ▼
 Agentes   Conhecimento  Prompts
     │         │         │
     └─────────┼─────────┘
               ▼
        Modelo de IA
(ChatGPT, Hugging Face,
 OpenRouter, AMÁLIA...)

---

# Filosofia do Projeto

O IA-JOMARO deverá ser:

- Modular.
- Simples de compreender.
- Independente do modelo de IA utilizado.
- Bem documentado.
- Evolutivo.

O objetivo é que qualquer pessoa consiga compreender o projeto e contribuir para a sua evolução.
