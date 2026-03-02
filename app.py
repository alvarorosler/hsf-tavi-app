import streamlit as st

# Configuração da Página
st.set_page_config(page_title="HSF-TAVI Risk Score", page_icon="🫀")

# Estilização Customizada
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #004b87; color: white; }
    .result-box { padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🫀 Escore HSF-TAVI")
st.subheader("Machine Learning Tool - Estratificação de Risco Hospitalar")
st.info("Ferramenta de apoio à decisão clínica baseada em modelos de IA (Regularização LASSO).")

# --- ENTRADA DE DADOS ---
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Fatores Técnicos")
        acesso = st.toggle("Acesso NÃO-Transfemoral", help="+4 pontos")
        protese = st.toggle("Prótese Auto-Expansível", help="+2 pontos")
        
    with col2:
        st.markdown("### Perfil Clínico")
        idade = st.toggle("Idade > 80 anos", help="+2 pontos")
        albumina = st.toggle("Albumina < 3.5 g/dL", help="+3 pontos")

    st.divider()
    
    st.markdown("### Comorbidades e Marcadores (+1 pt cada)")
    c1, c2, c3 = st.columns(3)
    with c1:
        clcr = st.toggle("ClCr < 45 ml/min")
        feve = st.toggle("FEVE < 45%")
    with c2:
        psap = st.toggle("PSAP > 60 mmHg")
        hb = st.toggle("Hemoglobina < 11 g/dL")
    with c3:
        sexo = st.toggle("Sexo Feminino")

# --- LÓGICA DO ESCORE ---
pontos = 0
if acesso: pontos += 4
if albumina: pontos += 3
if protese: pontos += 2
if idade: pontos += 2
if clcr: pontos += 1
if feve: pontos += 1
if psap: pontos += 1
if hb: pontos += 1
if sexo: pontos += 1

# --- EXIBIÇÃO DO RESULTADO ---
st.divider()
st.metric(label="Pontuação Total HSF-TAVI", value=f"{pontos} Pontos")

if pontos <= 4:
    color = "#d4edda" # Verde
    texto = "BAIXO RISCO"
    mortalidade = "3,2%"
elif pontos <= 8:
    color = "#fff3cd" # Amarelo
    texto = "RISCO INTERMEDIÁRIO"
    mortalidade = "7,9%"
else:
    color = "#f8d7da" # Vermelho
    texto = "ALTO RISCO"
    mortalidade = "25,0%"

st.markdown(f"""
    <div class="result-box" style="background-color: {color}; border: 1px solid black;">
        <h2 style="margin:0;">{texto}</h2>
        <p style="font-size: 1.2rem;">Mortalidade Hospitalar Estimada: <b>{mortalidade}</b></p>
    </div>
    """, unsafe_allow_html=True)

# Rodapé Técnico
st.sidebar.markdown("""
### Notas Técnicas
- **C-estatística:** 0,749
- **Especificidade (Alto Risco):** 92,7%
- **VPN:** 95,0%
- **Método:** Aprendizado Supervisionado via LASSO.
""")
