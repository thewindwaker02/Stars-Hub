import streamlit as st
import requests
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="STARS Intelligence Hub", 
    page_icon="⭐", 
    layout="wide"
)

# 2. CSS CUSTOMIZADO (Fundo escuro puro, sem azul)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #121212 0%, #1c1c1c 45%, #000000 100%) !important;
    }
    
    .stMetric {
        background-color: rgba(35, 35, 35, 0.7); 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #D5B642;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    }
    
    .custom-card {
        background-color: rgba(35, 35, 35, 0.7); 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #D5B642; 
        height: 100%;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIALIZAÇÃO DA MEMÓRIA
if "pagina_tel" not in st.session_state:
    st.session_state.pagina_tel = 0

if "pagina_email" not in st.session_state:
    st.session_state.pagina_email = 0

if "dados_reais" not in st.session_state:
    st.session_state.dados_reais = None

# 4. CABEÇALHO
st.image("logo.png", width=250)
st.title("Hub de Inteligência de Dados")
st.write("Análise de Compliance e Risco em Tempo Real")
st.divider()

# 5. INTERRUPTOR E TÍTULO FIXO (Para o nome da empresa nunca sumir)
modo_apresentacao = st.toggle("⭐ Ativar Modo Apresentação (Mostrar Exemplo 100% Integrado)")

if modo_apresentacao:
    st.success("✅ Protocolo de Análise Gerado (MODO DEMONSTRAÇÃO)!")
    st.subheader("🏢 EMPRESA DE TECNOLOGIA STARS S.A.")
    st.caption("Nome Fantasia: STARS Bank") # <--- LINHA ADICIONADA AQUI
elif st.session_state.dados_reais and st.session_state.dados_reais not in ["ERROR", "API_ERROR"]:
    st.success("✅ Protocolo de Análise Ativo (BUSCA REAL)!")
    st.subheader(f"🏢 {st.session_state.dados_reais.get('nome')}")
    st.caption(f"Nome Fantasia: {st.session_state.dados_reais.get('fantasia', 'Não informado')}") # <--- LINHA ADICIONADA AQUI

# =========================================================================
# MODO DE APRESENTAÇÃO
# =========================================================================
if modo_apresentacao:
    
    # --- Bloco 1: Receita ---
    st.write("### 🏛️ Dados Oficiais (Receita Federal)")
    
    col1, col2, col3, col4 = st.columns([1.5, 1, 1, 1])
    
    with col1:
        st.markdown("""
            <div class='custom-card'>
                <p style='margin:0; font-size:14px; color:#888;'>CNPJ</p>
                <p style='margin:5px 0 0 0; font-size:20px; font-weight:bold; color:#FFF; white-space:nowrap;'>12.345.678/0001-99</p>
            </div>
            """, unsafe_allow_html=True)
            
    with col2: 
        st.metric(label="Status", value="ATIVA")
        
    with col3: 
        st.metric(label="Tipo", value="MATRIZ")
        
    with col4: 
        st.metric(label="+ de 1 ano?", value="Sim (5 anos)")
    
    st.write("")
    
    col5, col6 = st.columns(2)
    
    with col5: 
        st.info("📞 **Tel Registrado na Receita:** (11) 4002-8922")
        
    with col6: 
        st.info("📧 **E-mail na Receita:** contato@stars.com.br")
    
    st.write("")
    st.write("📍 **Endereço Completo (Receita Federal):**")
    st.info("Av. Faria Lima, 1000 - Andar 5 - Itaim Bibi, São Paulo/SP - CEP: 01451-001")
    
    st.divider()
    
    # --- Bloco 2: Vadu ---
    st.write("### 🔄 Histórico de Alterações Cadastrais (Fonte: Vadu)")
    
    col_alt1, col_alt2 = st.columns(2)
    
    with col_alt1: 
        st.warning("⚠️ **Última Alteração (15/04/2026):** Entrada de novo Sócio Majoritário (STARS Participações S.A.) e saída de antigo investidor.")
        
    with col_alt2: 
        st.warning("⚠️ **Alteração de Capital (10/01/2025):** Capital Social aumentado de R$ 1.000.000,00 para R$ 5.000.000,00.")
        
    st.divider()
    
    # --- Bloco 3: Cruzamento ---
    st.write("### 🔎 Cruzamento nas Plataformas (Assertiva, Vadu, Allcheck)")
    
    col_emails, col_tels = st.columns(2)
    
    # PAGINAÇÃO DE E-MAILS (Limite 8 e agrupado: Vadu -> Assertiva -> Allcheck)
    with col_emails:
        st.write("**📧 E-mails mapeados nas plataformas:**")
        
        emails_plataformas = [
            "1. financeiro@stars.com (Fonte: Vadu)",
            "2. juridico@stars.com (Fonte: Vadu)",
            "3. faturamento@stars.com.br (Fonte: Vadu)",
            "4. contabilidade@stars.com (Fonte: Vadu)",
            "5. diretoria@stars.com.br (Fonte: Assertiva)",
            "6. rh@stars.com (Fonte: Assertiva)",
            "7. operacional@stars.com (Fonte: Assertiva)",
            "8. contato@stars.com.br (Fonte: Allcheck)",
            "9. sac@stars.com.br (Fonte: Allcheck)",
            "10. suporte@stars.com.br (Fonte: Allcheck)"
        ]
        
        emails_por_pagina = 8
        total_paginas_email = (len(emails_plataformas) - 1) // emails_por_pagina + 1
        
        inicio_e = st.session_state.pagina_email * emails_por_pagina
        fim_e = inicio_e + emails_por_pagina
        emails_mostrar = emails_plataformas[inicio_e:fim_e]
        
        for email in emails_mostrar:
            st.info(f"**{email}**")
            
        if len(emails_plataformas) > emails_por_pagina:
            ce_esq, ce_meio, ce_dir = st.columns([1, 2, 1])
            
            with ce_esq:
                if st.session_state.pagina_email > 0:
                    if st.button("◀ Voltar E-mail", use_container_width=True):
                        st.session_state.pagina_email -= 1
                        st.rerun()
                        
            with ce_meio:
                st.write(f"<div style='text-align: center; margin-top: 10px;'>Pág {st.session_state.pagina_email + 1} de {total_paginas_email}</div>", unsafe_allow_html=True)
                
            with ce_dir:
                if st.session_state.pagina_email < total_paginas_email - 1:
                    if st.button("Mais E-mails ▶", use_container_width=True):
                        st.session_state.pagina_email += 1
                        st.rerun()
        
    # PAGINAÇÃO DE TELEFONES (Limite 8 e agrupado: Vadu (menos) -> Assertiva -> Allcheck)
    with col_tels:
        st.write("📱 **Telefones mapeados nas plataformas:**")
        
        telefones_plataformas = [
            "1. (11) 98888-2222 (Fonte: Vadu)",
            "2. (11) 92222-0000 (Fonte: Vadu)",
            "3. (11) 99999-1111 (Fonte: Assertiva)",
            "4. (11) 91111-0000 (Fonte: Assertiva)",
            "5. (11) 94444-0000 (Fonte: Assertiva)",
            "6. (11) 97777-0000 (Fonte: Assertiva)",
            "7. (11) 3333-4444 (Fonte: Allcheck)",
            "8. (11) 93333-0000 (Fonte: Allcheck)",
            "9. (11) 96666-0000 (Fonte: Allcheck)",
            "10. (11) 95555-0000 (Fonte: Allcheck)"
        ]
        
        tels_por_pagina = 8
        total_paginas_tel = (len(telefones_plataformas) - 1) // tels_por_pagina + 1
        
        inicio_t = st.session_state.pagina_tel * tels_por_pagina
        fim_t = inicio_t + tels_por_pagina
        telefones_mostrar = telefones_plataformas[inicio_t:fim_t]
        
        for tel in telefones_mostrar:
            st.error(f"**{tel}**")
            
        if len(telefones_plataformas) > tels_por_pagina:
            ct_esq, ct_meio, ct_dir = st.columns([1, 2, 1])
            
            with ct_esq:
                if st.session_state.pagina_tel > 0:
                    if st.button("◀ Voltar Tel", use_container_width=True):
                        st.session_state.pagina_tel -= 1
                        st.rerun()
                        
            with ct_meio:
                st.write(f"<div style='text-align: center; margin-top: 10px;'>Pág {st.session_state.pagina_tel + 1} de {total_paginas_tel}</div>", unsafe_allow_html=True)
                
            with ct_dir:
                if st.session_state.pagina_tel < total_paginas_tel - 1:
                    if st.button("Mais Tels ▶", use_container_width=True):
                        st.session_state.pagina_tel += 1
                        st.rerun()

# =========================================================================
# MODO DE BUSCA REAL
# =========================================================================
else:
    col_busca, col_vazia = st.columns([1, 2])
    
    with col_busca:
        cnpj_digitado = st.text_input("Insira o CNPJ da Empresa (Busca Real):", key="cnpj_input")
        botao_buscar = st.button("Executar Análise Real", type="primary")

    if botao_buscar:
        if cnpj_digitado:
            cnpj_limpo = cnpj_digitado.replace(".", "").replace("/", "").replace("-", "")
            
            with st.spinner('Consultando bases de dados oficiais...'):
                resposta = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj_limpo}")
                
                if resposta.status_code == 200:
                    dados_recebidos = resposta.json()
                    
                    if dados_recebidos.get("status") == "ERROR":
                        st.session_state.dados_reais = "ERROR"
                    else:
                        st.session_state.dados_reais = dados_recebidos
                else:
                    st.session_state.dados_reais = "API_ERROR"

    if st.session_state.dados_reais:
        if st.session_state.dados_reais == "ERROR":
            st.error("❌ CNPJ Inválido ou não encontrado na base de dados.")
            
        elif st.session_state.dados_reais == "API_ERROR":
            st.error("❌ Falha na comunicação com o servidor da API. Tente novamente.")
            
        else:
            d = st.session_state.dados_reais
            
            st.write("### 🏛️ Dados Oficiais (Receita Federal)")
            
            c1, c2, c3, c4 = st.columns([1.5, 1, 1, 1])
            
            with c1:
                st.markdown(f"""
                    <div class='custom-card'>
                        <p style='margin:0; font-size:14px; color:#888;'>CNPJ</p>
                        <p style='margin:5px 0 0 0; font-size:20px; font-weight:bold; color:#FFF; white-space:nowrap;'>{d.get('cnpj')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
            with c2: 
                st.metric(label="Status Cadastral", value=d.get('situacao'))
                
            with c3: 
                st.metric(label="Tipo", value=d.get('tipo'))
                
            with c4:
                antiguidade = "Sim"
                try:
                    data_abertura = datetime.strptime(d.get('abertura'), "%d/%m/%Y")
                    dias_passados = (datetime.now() - data_abertura).days
                    if dias_passados < 365: 
                        antiguidade = "Não"
                except:
                    antiguidade = "Erro no cálculo"
                    
                st.metric(label="+ de 1 ano?", value=antiguidade)
            
            st.write("")
            
            c5, c6 = st.columns(2)
            
            if d.get('telefone'):
                telefone_real = d.get('telefone')
            else:
                telefone_real = 'Não informado'
                
            if d.get('email'):
                email_real = d.get('email')
            else:
                email_real = 'Não informado'
            
            with c5: 
                st.info(f"📞 **Tel Registrado:** {telefone_real}")
                
            with c6: 
                st.info(f"📧 **E-mail na Receita:** {email_real}")

            st.write("")
            st.write("📍 **Endereço Completo (Receita Federal):**")
            
            logradouro = d.get('logradouro', '')
            numero = d.get('numero', 'S/N')
            
            if d.get('complemento'):
                complemento = f" - {d.get('complemento')}"
            else:
                complemento = ""
                
            bairro = d.get('bairro', '')
            municipio = d.get('municipio', '')
            uf = d.get('uf', '')
            cep = d.get('cep', '')
            
            endereco_completo_real = f"{logradouro}, {numero}{complemento} - {bairro}, {municipio}/{uf} - CEP: {cep}"
            
            st.info(endereco_completo_real)
            
            st.divider()
            st.info("💡 Faltam as APIs: Assertiva, Vadu e Allcheck. Quando tivermos as chaves, as alterações cadastrais e as paginações de dados extras vão entrar aqui embaixo.")
