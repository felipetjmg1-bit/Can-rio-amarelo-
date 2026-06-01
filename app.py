
import gradio as gr
import os
from main import run_aurora_analysis
import json

def gradio_interface(openai_api_key: str, analysis_prompt: str, speckle_model_json: str) -> str:
    """
    Interface Gradio para a função de análise Aurora AI.
    """
    try:
        # Simular o objeto raiz do Speckle a partir do JSON de entrada
        version_root_object = json.loads(speckle_model_json)
        
        result = run_aurora_analysis(version_root_object, openai_api_key, analysis_prompt)
        return result
    except json.JSONDecodeError:
        return "Erro: O JSON do modelo Speckle é inválido. Por favor, forneça um JSON válido."
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"


iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(label="OpenAI API Key", type="password"),
        gr.Textbox(label="Prompt de Análise", value="Realize uma auditoria técnica rigorosa. Verifique se há duplicidade de IDs, inconsistências de materiais e se a hierarquia espacial faz sentido para um modelo de construção."),
        gr.Textbox(label="Modelo Speckle (JSON)", placeholder="Cole aqui o JSON do seu modelo Speckle...")
    ],
    outputs="text",
    title="Canário Amarelo - Análise BIM com Aurora AI",
    description="Analise seus modelos BIM do Speckle usando a IA Aurora (GPT-4o-mini). Forneça sua chave da API OpenAI, um prompt de análise e o JSON do seu modelo Speckle."
)

iface.launch()
