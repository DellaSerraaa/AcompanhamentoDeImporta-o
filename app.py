import streamlit as st

# Função para gerar nomes fictícios de clientes
def gerar_nomes_clientes(num_clientes):
    return [f"Cliente {i+1}" for i in range(num_clientes)]

# Lista de etapas do processo
etapas = [
    "Solicitação Enviada",
    "Solicitação Recebida",
    "Extrato Importado",
    "Extrato Verificado",
    "Processo Concluído"
]

# Inicializando o progresso dos clientes no session_state
if 'progresso_clientes' not in st.session_state:
    st.session_state.progresso_clientes = {nome: [False for _ in etapas] for nome in gerar_nomes_clientes(100)}

# Layout do Dashboard
st.title('Dashboard de Acompanhamento de Importação de Extratos Bancários')

# Sidebar com lista de clientes para seleção
cliente_selecionado = st.sidebar.selectbox('Selecionar Cliente', list(st.session_state.progresso_clientes.keys()))

# Atualizar progresso do cliente
def atualizar_progresso(cliente, etapa):
    st.session_state.progresso_clientes[cliente][etapa] = not st.session_state.progresso_clientes[cliente][etapa]

# Mostrar o progresso do cliente selecionado
st.header(f"Progresso do Cliente: {cliente_selecionado}")

for i, etapa in enumerate(etapas):
    # Checkbox para cada etapa
    checked = st.checkbox(f"{etapa}", value=st.session_state.progresso_clientes[cliente_selecionado][i], key=f"{cliente_selecionado}-{i}")
    if checked != st.session_state.progresso_clientes[cliente_selecionado][i]:
        atualizar_progresso(cliente_selecionado, i)

# Visualização do progresso em uma linha do tempo (simplificada)
progresso = st.session_state.progresso_clientes[cliente_selecionado]
st.write("Linha do Tempo do Progresso:")
st.progress(sum(progresso) / len(progresso))
