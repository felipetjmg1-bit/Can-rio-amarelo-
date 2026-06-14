# Canário Amarelo - Análise BIM com Aurora AI 🇧🇷

Este repositório contém a implementação do **Canário Amarelo**, uma ferramenta inovadora para **análise BIM (Building Information Modeling)** que integra a **Inteligência Artificial Aurora** (baseada em GPT-4o-mini) com a plataforma **Speckle**. O objetivo principal é auditar modelos BIM, identificando automaticamente duplicidade de IDs, inconsistências de materiais e verificando a lógica da hierarquia espacial em projetos de construção.

## 🚀 Funcionalidades Principais

*   **Análise BIM Inteligente**: Utiliza IA para realizar auditorias técnicas rigorosas em modelos Speckle.
*   **Detecção de Inconsistências**: Identifica problemas como IDs duplicados, materiais inconsistentes e falhas na estrutura espacial.
*   **Integração Speckle**: Processa dados diretamente de modelos Speckle, aproveitando sua estrutura de dados.
*   **Interface Gradio**: Oferece uma interface web intuitiva para interação e visualização dos resultados da análise.
*   **Função Speckle Automate**: Pode ser executado como uma função automatizada dentro do ecossistema Speckle.

## 💻 Como Usar

O projeto pode ser utilizado de duas formas principais: através da interface web Gradio ou como uma função Speckle Automate.

### 1. Via Interface Web Gradio

A maneira mais fácil de interagir com o Canário Amarelo é através de sua interface web construída com Gradio. Para executá-la localmente:

1.  **Instale as dependências**: Certifique-se de ter Python 3.11 instalado e as dependências listadas em `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
2.  **Execute o aplicativo**: Inicie a interface Gradio.
    ```bash
    python app.py
    ```
3.  **Acesse a interface**: Abra seu navegador e navegue até o endereço fornecido pelo Gradio (geralmente `http://127.0.0.1:7860`).

Na interface, você precisará fornecer:

*   **OpenAI API Key**: Sua chave de API da OpenAI para acessar o modelo GPT-4o-mini. Você pode obtê-la em [OpenAI Platform](https://platform.openai.com/).
*   **Prompt de Análise**: Um prompt de texto que guiará a IA na auditoria. Um prompt padrão é fornecido.
*   **Modelo Speckle (JSON)**: O conteúdo JSON do seu modelo Speckle. Você pode exportar um modelo do Speckle para JSON ou usar um exemplo.

Clique em "Submit" para iniciar a análise e visualizar o relatório gerado pela Aurora AI diretamente na interface.

### 2. Como Função Speckle Automate

O Canário Amarelo foi projetado para funcionar como uma função dentro do ecossistema Speckle Automate. Ele recebe um `AutomationContext` e `FunctionInputs` para processar modelos Speckle de forma automatizada.

Os parâmetros de entrada esperados pela função são definidos na classe `FunctionInputs` em `main.py`:

*   `openai_api_key`: Chave de API da OpenAI.
*   `analysis_prompt`: Prompt de análise para a IA.

Um exemplo de como a função pode ser invocada em um ambiente Speckle Automate pode ser encontrado em `example.function_inputs.json`, embora os campos `whisperMessage` e `forbiddenSpeckleType` neste arquivo de exemplo estejam desatualizados em relação à implementação atual.

## 📂 Estrutura do Projeto

```
.github/
├── workflows/
│   └── main.yml
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── example.function_inputs.json
├── flatten.py
├── main.py
├── mise.toml
├── pyproject.toml
├── requirements.txt
└── tests/
    └── test_function.py
```

*   `main.py`: Contém a lógica principal da função Speckle Automate e a integração com a API da OpenAI para a análise Aurora AI.
*   `flatten.py`: Módulo auxiliar para achatar objetos Speckle, facilitando o processamento.
*   `app.py`: O ponto de entrada para a interface web Gradio, que encapsula a lógica de `main.py`.
*   `pyproject.toml`: Define os metadados do projeto e suas dependências, incluindo `specklepy`, `speckle-automate`, `openai` e `gradio`.
*   `requirements.txt`: Lista as dependências exatas do projeto.
*   `tests/`: Contém testes de integração para a função Speckle Automate. (Nota: Alguns testes podem refletir uma versão anterior da `FunctionInputs`).
*   `Dockerfile`: Configuração para construir uma imagem Docker do projeto.

## 🛡️ Propósito Estratégico: Soberania Tecnológica

Este projeto é um componente fundamental do ecossistema de **Soberania Tecnológica** da Impulso Digital. Nossa missão é prover independência digital para o Brasil através de soluções de IA e Blockchain que operam sob controle nacional e proteção de dados soberana.

### Pilares da Soberania

*   **Independência Tecnológica**: Desenvolvimento de soluções que não dependem de infraestruturas estrangeiras.
*   **Soberania de Dados**: Garantia de que informações estratégicas brasileiras permaneçam sob jurisdição nacional.
*   **Segurança e Resiliência**: Sistemas projetados para a proteção do futuro digital da nossa nação.

Ao integrar esta tecnologia, você fortalece a infraestrutura crítica brasileira e contribui para um Brasil tecnologicamente forte e independente.

## 📄 Licença

Este projeto está licenciado sob a licença Apache-2.0.

---
**Desenvolvido por Felipe Aquino - Impulso Digital**
*Liderando a revolução da IA Soberana no Brasil.*
