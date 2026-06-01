
"""
Chat-GPT Aurora - Speckle Automate Function
Integrando IA (Aurora) para análise inteligente de dados BIM no Speckle.
"""

import os
from pydantic import Field, SecretStr
from speckle_automate import (
    AutomateBase,
    AutomationContext,
    execute_automate_function,
)
from openai import OpenAI
from flatten import flatten_base
import json

class FunctionInputs(AutomateBase):
    """Parâmetros de entrada para a função Aurora AI."""
    
    openai_api_key: SecretStr = Field(
        title="OpenAI API Key",
        description="Chave para acessar o modelo Aurora/GPT para análise."
    )
    analysis_prompt: str = Field(
        default="Realize uma auditoria técnica rigorosa. Verifique se há duplicidade de IDs, inconsistências de materiais e se a hierarquia espacial faz sentido para um modelo de construção.",
        title="Prompt de Análise Avançada",
        description="Instruções específicas para a auditoria de IA."
    )

def run_aurora_analysis(
    version_root_object: dict,
    openai_api_key: str,
    analysis_prompt: str,
) -> str:
    """
    Função principal que executa a análise Aurora AI.
    Recebe o objeto raiz do Speckle, a chave da API OpenAI e o prompt de análise.
    """
    flat_objects = list(flatten_base(version_root_object))
    
    object_types = {}
    missing_params = []
    for obj in flat_objects[:150]: # Limitar a amostra para evitar sobrecarga em demos
        t = obj.speckle_type
        object_types[t] = object_types.get(t, 0) + 1
        
        if "Structure" in t and not hasattr(obj, "material"):
            missing_params.append(f"Objeto {obj.id} ({t}) sem material definido.")

    data_summary = f"Relatório de Dados BIM:\n"
    data_summary += f"- Total de objetos: {len(flat_objects)}\n"
    data_summary += f"- Amostra para análise profunda: {len(flat_objects[:150])}\n"
    data_summary += "Distribuição de tipos:\n"
    for t, count in object_types.items():
        data_summary += f"  * {t}: {count}\n"
    
    if missing_params:
        data_summary += "\nInconsistências detectadas por regras locais:\n"
        data_summary += "\n".join(missing_params[:10])

    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é a Aurora, uma especialista em análise de dados BIM e Speckle."},
                {"role": "user", "content": f"{analysis_prompt}\n\nDados do Modelo:\n{data_summary}"}
            ]
        )
        
        analysis_result = response.choices[0].message.content
        return analysis_result

    except Exception as e:
        return f"Falha na integração com Aurora AI: {str(e)}"

def automate_function(
    automate_context: AutomationContext,
    function_inputs: FunctionInputs,
) -> None:
    """
    Função que recebe dados do Speckle e os envia para análise via IA Aurora.
    """
    version_root_object = automate_context.receive_version()
    
    analysis_result = run_aurora_analysis(
        version_root_object,
        function_inputs.openai_api_key.get_secret_value(),
        function_inputs.analysis_prompt
    )

    if "Falha na integração" in analysis_result:
        automate_context.mark_run_failed(analysis_result)
    else:
        automate_context.mark_run_success(f"Análise Aurora concluída: {analysis_result[:200]}...")
        with open("relatorio_aurora.md", "w") as f:
            f.write(f"# Relatório de Análise Aurora AI\n\n{analysis_result}")
        automate_context.store_file_result("relatorio_aurora.md")


if __name__ == "__main__":
    # Este bloco será executado apenas se main.py for chamado diretamente, não via Gradio
    # Para uso com Speckle Automate, a função automate_function é o ponto de entrada.
    # Para testes locais ou integração com Gradio, use run_aurora_analysis diretamente.
    print("Este script é projetado para ser usado como uma função Speckle Automate ou via Gradio.")
    print("Para testar a função automate_function, use o ambiente Speckle Automate.")
    print("Para testar a função run_aurora_analysis, chame-a diretamente com os parâmetros necessários.")
