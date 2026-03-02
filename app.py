import streamlit as st

# Configuração da Página
st.set_page_config(page_title="HSF-TAVI Risk Score", page_icon="🫀", layout="centered")

# Estilização Customizada
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; }
    .result-box { padding: 25px; border-radius: 15px; text-align: center; margin-top: 20px; border: 2px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🫀 Escore HSF-TAVI")
st.subheader("Ferramenta de IA para Estratificação de Risco")
st.caption("Cientista de Dados: Álvaro Rösler / Diretor Médico: Dr. Fernando Lucchese")
st.caption("Centro de Pesquisas em Cirurgia Cardiovascular - Hospital São Francisco")
st.markdown("---")

# --- ENTRADA DE DADOS ---
st.markdown("### Selecione os Fatores de Risco Presentes:")

col1, col2 = st.columns(2)

with col1:
    st.write("**Variáveis Técnicas (Maior Peso)**")
    acesso_val = st.toggle("Acesso NÃO-Transfemoral", help="Peso: +4 pontos")
    protese_val = st.toggle("Prótese Auto-Expansível", help="Peso: +2 pontos")

with col2:
    st.write("**Perfil do Paciente**")
    albumina_val = st.toggle("Albumina < 3.5 g/dL", help="Peso: +3 pontos")
    idade_val = st.toggle("Idade > 80 anos", help="Peso: +2 pontos")

st.markdown("---")
st.write("**Comorbidades e Marcadores (+1 ponto cada)**")
c1, c2, c3 = st.columns(3)

with c1:
    clcr_val = st.toggle("ClCr < 45 ml/min")
    feve_val = st.toggle("FEVE < 45%")
with c2:
    psap_val = st.toggle("PSAP > 60 mmHg")
    hb_val = st.toggle("Hemoglobina < 11 g/dL")
with c3:
    sexo_val = st.toggle("Sexo Feminino")

# --- LÓGICA DE SOMA ---
pontos = 0
if acesso_val: pontos += 4
if albumina_val: pontos += 3
if protese_val: pontos += 2
if idade_val: pontos += 2
if clcr_val: pontos += 1
if feve_val: pontos += 1
if psap_val: pontos += 1
if hb_val: pontos += 1
if sexo_val: pontos += 1

# --- EXIBIÇÃO DO RESULTADO COM AS FRASES SOLICITADAS ---
st.markdown("### Resultado da Avaliação")
st.metric(label="Pontuação Total HSF-TAVI", value=f"{pontos} pontos")

if pontos <= 4:
    cor_fundo = "#d4edda" # Verde
    titulo_risco = "BAIXO RISCO"
    frase_mortalidade = "Mortalidade estimada em torno de 3%"
    cor_texto = "#155724"
elif pontos <= 8:
    cor_fundo = "#fff3cd" # Amarelo
    titulo_risco = "RISCO INTERMEDIÁRIO"
    frase_mortalidade = "Mortalidade estimada em torno de 8%"
    cor_texto = "#856404"
else:
    cor_fundo = "#f8d7da" # Vermelho
    titulo_risco = "ALTO RISCO"
    frase_mortalidade = "Mortalidade estimada superior a 20%"
    cor_texto = "#721c24"

st.markdown(f"""
    <div class="result-box" style="background-color: {cor_fundo}; color: {cor_texto};">
        <h1 style="margin:0; font-size: 2.5rem;">{titulo_risco}</h1>
        <p style="font-size: 1.4rem; margin:15px 0 0 0; font-weight: bold;">{frase_mortalidade}</p>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.sidebar.markdown(f"""
### 📊 Dados do Modelo
- **C-estatística:** 0,749
- **Especificidade:** 92,7%
- **VPN:** 95,0%
---
* Desenvolvido via Machine Learning para predição de mortalidade hospitalar associada à realização de TAVI.*
""")
