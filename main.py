import google.generativeai as genai
import json

# Configuração da API
genai.configure(api_key="SUA_CHAVE_AQUI")

# Como AI Engineer, você configura o modelo para garantir respostas estruturadas (JSON)
model = genai.GenerativeModel('gemini-2.5-flash')

def processar_receita_para_json(receita_base, porcoes_originais, porcoes_desejadas):
    prompt = f"""
    Você é uma API de processamento de dados de receitas.
    Receita base para {porcoes_originais} pessoas: {receita_base}
    
    Recalcule as proporções para {porcoes_desejadas} pessoas.
    
    Sua saída DEVE ser estritamente um objeto JSON com a seguinte estrutura:
    {{
      "porcoes_calculadas": {porcoes_desejadas},
      "lista_de_compras": {{
        "acougue": ["item 1", "item 2"],
        "hortifruti": ["item 1", "item 2"],
        "mercearia": ["item 1"]
      }}
    }}
    Não inclua formatação Markdown, retorne apenas o JSON puro.
    """
    
    resposta = model.generate_content(prompt)
    
    # Tratamento de dados - convertendo a string da IA para um dicionário Python
    try:
        dados_estruturados = json.loads(resposta.text.strip())
        return dados_estruturados
    except json.JSONDecodeError:
        return {"erro": "O modelo não retornou um JSON válido."}

# Testando a integração
receita_caldo = "Caldo de carne com mandioca usando 70% acém e 30% maçã de peito, cebola, alho e cheiro-verde."
resultado_json = processar_receita_para_json(receita_caldo, 18, 30)

print(json.dumps(resultado_json, indent=4, ensure_ascii=False))