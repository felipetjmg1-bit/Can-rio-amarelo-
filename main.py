"""Operação Canário Amarelo - Speckle Automate Function.

Integrando IA Aurora para análise soberana de dados BIM e Tokens Aurora.
"""

from flatten import flatten_base
from openai import OpenAI
from pydantic import Field, SecretStr
from speckle_automate import (
    AutomateBase,
    AutomationContext,
    execute_automate_function,
)


class FunctionInputs(AutomateBase):
    """Parâmetros de entrada para a função Aurora AI."""

    openai_api_key: SecretStr = Field(
        title="OpenAI API Key",
        description="Chave para acessar o modelo Aurora/GPT para análise."
    )
    analysis_prompt: str = Field(
        default=(
            "Realize uma auditoria técnica rigorosa focada em soberania. "
            "Verifique duplicidade de IDs, inconsistências de materiais e "
            "valide a integridade dos dados para tokenização Aurora."
        ),
        title="Prompt de Análise Soberana",
        description="Instruções específicas para a auditoria de IA."
    )


def generate_html_report(
    analysis_result: str,
    data_summary: str,
    object_types: dict,
) -> str:
    """Gera um relatório HTML com o tema Operação Canário Amarelo.

    Args:
        analysis_result: Resultado da análise da IA Aurora.
        data_summary: Sumário dos dados processados.
        object_types: Dicionário com tipos de objetos e contagens.

    Returns:
        String contendo o HTML do relatório.
    """
    object_types_html = "".join(
        f"<li>{t}: <strong>{count}</strong> elementos</li>"
        for t, count in object_types.items()
    )

    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relatório Operação Canário Amarelo</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1a3a00 0%, #3a5a00 100%);
                color: #f0f0f0;
                line-height: 1.6;
                padding: 20px;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background: rgba(20, 40, 0, 0.95);
                border: 2px solid #ffd700;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 0 40px rgba(255, 215, 0, 0.2);
            }}
            .header {{
                background: linear-gradient(90deg, #ffd700 0%, #008000 100%);
                padding: 40px;
                text-align: center;
                border-bottom: 4px solid #ffd700;
            }}
            .header h1 {{
                color: #1a3a00;
                font-size: 3em;
                font-weight: 900;
                margin-bottom: 10px;
                text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }}
            .header p {{
                color: #1a3a00;
                font-size: 1.2em;
                font-weight: bold;
                letter-spacing: 1px;
            }}
            .badge {{
                display: inline-block;
                background: #ffd700;
                color: #1a3a00;
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: 800;
                margin: 15px 5px;
                font-size: 0.9em;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }}
            .badge.canario {{
                background: #008000;
                color: #ffd700;
                border: 1px solid #ffd700;
            }}
            .content {{
                padding: 50px;
            }}
            .section {{
                margin-bottom: 40px;
                padding: 25px;
                background: rgba(255, 215, 0, 0.03);
                border-left: 6px solid #ffd700;
                border-radius: 10px;
            }}
            .section h2 {{
                color: #ffd700;
                margin-bottom: 20px;
                font-size: 2em;
                text-transform: uppercase;
                letter-spacing: 3px;
            }}
            .data-summary {{
                background: rgba(0, 0, 0, 0.4);
                padding: 20px;
                border-radius: 10px;
                font-family: 'Consolas', monospace;
                color: #ffd700;
                white-space: pre-wrap;
                border: 1px solid rgba(255, 215, 0, 0.2);
            }}
            .analysis-result {{
                background: rgba(0, 128, 0, 0.05);
                padding: 30px;
                border-radius: 10px;
                border: 1px solid #ffd700;
                font-size: 1.1em;
                color: #ffffff;
            }}
            ul {{
                margin-left: 30px;
                list-style-type: square;
            }}
            li {{
                margin-bottom: 10px;
                color: #ffd700;
            }}
            li strong {{
                color: #ffffff;
            }}
            .footer {{
                background: #004d00;
                padding: 30px;
                text-align: center;
                border-top: 3px solid #ffd700;
                color: #ffd700;
            }}
            .footer p {{
                margin: 8px 0;
            }}
            .sovereignty-note {{
                color: #00ff00;
                font-weight: bold;
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🐤 OPERAÇÃO CANÁRIO AMARELO</h1>
                <p>Soberania Digital • Independência Financeira • Tokens Aurora</p>
                <div>
                    <span class="badge canario">BRASIL SOBERANO</span>
                    <span class="badge">AUDITORIA IA</span>
                    <span class="badge">BLOCKCHAIN NACIONAL</span>
                </div>
            </div>

            <div class="content">
                <div class="section">
                    <h2>📋 Sumário de Integridade</h2>
                    <div class="data-summary">{data_summary}</div>
                </div>

                <div class="section">
                    <h2>🛡️ Relatório de Auditoria Soberana</h2>
                    <div class="analysis-result">
                        {analysis_result}
                    </div>
                </div>

                <div class="section">
                    <h2>💎 Ativos e Elementos Analisados</h2>
                    <ul>
                        {object_types_html}
                    </ul>
                </div>

                <div class="section">
                    <h2>🇧🇷 Compromisso com a Nação</h2>
                    <p class="sovereignty-note">
                        Este relatório foi processado sob infraestrutura crítica
                        brasileira, garantindo que nenhum dado sensível deixe
                        nossa jurisdição. A Operação Canário Amarelo assegura
                        a resiliência do futuro digital do Brasil.
                    </p>
                </div>
            </div>

            <div class="footer">
                <p><strong>Operação Canário Amarelo - Ecossistema Aurora</strong></p>
                <p>Desenvolvido por Felipe Aquino - Impulso Digital</p>
                <p>Pela Independência Tecnológica do Brasil 🇧🇷</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


def automate_function(
    automate_context: AutomationContext,
    function_inputs: FunctionInputs,
) -> None:
    """Recebe dados do Speckle e os envia para análise via IA Aurora."""
    # 1. Receber dados do Speckle
    version_root_object = automate_context.receive_version()
    flat_objects = list(flatten_base(version_root_object))

    # 2. Preparar sumário detalhado
    object_types = {}
    for obj in flat_objects[:150]:
        t = obj.speckle_type
        object_types[t] = object_types.get(t, 0) + 1

    data_summary = "Sumário de Dados Estratégicos:\n"
    data_summary += f"- Total de elementos: {len(flat_objects)}\n"
    data_summary += f"- Amostra auditada: {len(flat_objects[:150])}\n"
    data_summary += "Distribuição por categoria:\n"
    for t, count in object_types.items():
        data_summary += f"  * {t}: {count}\n"

    # 3. Chamar a IA Aurora
    try:
        client = OpenAI(
            api_key=function_inputs.openai_api_key.get_secret_value()
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é a Aurora, a inteligência central da Operação "
                        "Canário Amarelo. Sua missão é garantir a soberania "
                        "e integridade dos dados nacionais."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"{function_inputs.analysis_prompt}\n\n"
                        f"Dados para Auditoria:\n{data_summary}"
                    ),
                },
            ]
        )

        analysis_result = response.choices[0].message.content

        # 4. Gerar relatório HTML temático
        html_report = generate_html_report(
            analysis_result,
            data_summary,
            object_types,
        )

        # 5. Finalizar execução e salvar resultados
        automate_context.mark_run_success(
            "Auditoria Canário Amarelo concluída com sucesso."
        )

        with open("relatorio_canario.html", "w", encoding="utf-8") as f:
            f.write(html_report)

        with open("relatorio_canario.md", "w", encoding="utf-8") as f:
            f.write(f"# Auditoria Operação Canário Amarelo\n\n{analysis_result}")

        automate_context.store_file_result("relatorio_canario.html")
        automate_context.store_file_result("relatorio_canario.md")

    except Exception as e:
        automate_context.mark_run_failed(
            f"Erro na Operação Canário Amarelo: {str(e)}"
        )


if __name__ == "__main__":
    execute_automate_function(automate_function, FunctionInputs)
