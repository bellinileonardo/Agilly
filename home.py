import func as fct
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import streamlit as st

st.set_page_config(page_title="Agily - Implantação Express ", page_icon=":dizzy:",
                   layout="wide", initial_sidebar_state="expanded", menu_items=None)


perfis_pdv = ["NFCE01", "NFCE02", "NFCE03", "NFCE04", "NFCE05"]


# Defina as credenciais de login
credenciais = {
    "Processa": "123456",
}

# Função de login


def login():

    page_login = """
    <style>

    [data-testid="stMarkdown"]{
        padding: 2px;
    }
    [data-testid="stMarkdownContainer"]{
        color: white;
        font-size: 28px;
    }

    [data-testid="stHeader"]{
    background-color: rgb(255, 255, 255, 0.2);
    color: white;
    }

    [data-testid="stAppViewContainer"]{
        background-image: url("http://172.27.3.197/agillity/img/fundo_tela.jpg");
        background-color: #fff;
        background-size: cover;
        background-repeat: no-repeat;
    }

    [data-testid="stVerticalBlockBorderWrapper"]{
    background-color: transparent;

    }
    [data-testid="stVerticalBlock"]{
        background-color: transparent;
    }
    </style>
    """

    st.markdown(page_login, unsafe_allow_html=True)
    cola01, cola02, cola03 = st.columns([6, 3, 6])
    with cola01:
        pass
    with cola02:
        st.image("agilly_logo_login.png")
    with cola03:
        pass
    collogo01, collogo02, collogo03 = st.columns([1, 5, 1])
    with collogo01:
        pass
    with collogo02:

        username = st.text_input("Nome de usuário")
        senha = st.text_input("Senha", type="password")

        if st.button("Login", type='primary'):
            if username in credenciais and credenciais[username] == senha:
                return True
            else:
                st.error("Credenciais inválidas. Tente novamente.")
    with collogo03:
        pass


def pagina_protegida():
    page_home = """
    <style>


    [data-testid="stHeader"]{
    background-color: rgb(21, 0, 91, 0.8);

    }

    [data-testid="stAppViewContainer"]{
        
        background-color: #fff;
        background-size: cover;
        background-repeat: no-repeat;
    }

    [data-testid="stExpander"]{
        border-radius: 10px;
        background-color: rgb(255, 255, 255, 0.7) ;
    }
    </style>
    """
    st.markdown(page_home, unsafe_allow_html=True)
    # Configuração de Bancos para copia

    with st.sidebar.popover(f" :one: Configuração", use_container_width=True):
        col1, col2 = st.columns(2)
        with st.container(border=True):

            with col1:
                st.write("Banco Fonte:")
                numero_ip_alvo = st.text_input(
                    f"Digite o IP da loja alvo ", key="numero_ip_alvo", placeholder="192.168.1.248")
                nome_banco_dados_alvo = st.text_input(
                    "Digite o nome do banco de dados da loja alvo", key="nome_banco_dados_alvo", placeholder="DBMercadologic")
                nome_usuario_banco = st.text_input(
                    "Digite usuario de acesso ao Postgresql", key="nome_user_bd", placeholder="postgres")

            with col2:
                st.write("Banco Destino:")
                numero_ip_destino = st.text_input(
                    "Digite o IP da loja nova", key="numero_ip_destino", placeholder="192.168.1.249")
                nome_banco_dados_destino = st.text_input(
                    "Digite o nome do banco de dados da loja nova", key="nome_banco_dados_destino", placeholder="DBMercadologic")
                senha_usuario_banco = st.text_input(
                    "Digite a senha de acesso ao Postgresql", type="password", key="input_senha_banco")
            salvar_dados_config = st.button(
                "Salvar Dados de Conexão", type="primary", use_container_width=True)

            with st.container(border=True):
                if salvar_dados_config:
                    pass
    st.sidebar.caption(" Siga as passos :one:, :two: e :three: ")
    with st.sidebar:
        with st.expander("Status da Conexão", expanded=True):
            if numero_ip_alvo != "":
                st.markdown(f":white_check_mark: {numero_ip_alvo} \n :floppy_disk: {
                            nome_banco_dados_alvo}")
                st.markdown(f" ")
                st.markdown(f":twisted_rightwards_arrows: {
                            numero_ip_destino} \n :floppy_disk: {nome_banco_dados_destino}")

            else:
                st.html(
                    f"<div style='text-align:center; background: red; color: white; font-size: 15px;'>CONFIGURE A CONEXÃO DE DADOS ANTES DE INICIAR</div>")
        with st.expander(" :three: Documentação"):
            pass
        # BOTOES PARA IMPORTAÇÃO DE DADOS
        with st.expander(" :two: Opções de Importação"):
            if numero_ip_alvo != "":
                botao_opcoes_copia = st.checkbox(
                    "Importação", key="botao_copias_opcoes")
                botao_novos_dados = st.checkbox(
                    "IP - CSC - ID", key="botao_novos_dados_inseridos")
            else:
                st.html(
                    f"<div style='text-align:center; background: red; color: white; font-size: 10px;'></div>")
        # BOTOES PARA VISUALIZAÇÃO DE DADOS
        with st.expander(" :three: Visualiza Importação"):
            if numero_ip_alvo != "":
                vizu_motv_devolucao_btn = st.checkbox(
                    "Motivo Devolução", key="vizu_mot_devolucao")
                vizu_motv_desconto_btn = st.checkbox(
                    "Motivo Desconto", key="vizu_mot_desconto")
                vizu_motv_cancelamento_btn = st.checkbox(
                    "Motivo Cancelamento", key="vizu_mot_cancelamento")
                vizu_motv_suprimento_btn = st.checkbox(
                    "Motivo Suprimento", key="vizu_mot_suprimento")
                vizu_motv_sangria_btn = st.checkbox(
                    "Motivo Sangria", key="vizu_mot_sangria")
                vizu_config_geral_btn = st.checkbox(
                    "Config. Geral", key="vizu_config_geral")
                vizu_config_papel_btn = st.checkbox(
                    "Papel", key="vizu_config_papel")
                vizu_config_papel_central_btn = st.checkbox(
                    "Papel Central", key="vizu_config_papel_central")
                vizu_propriedade_perfil_btn = st.checkbox(
                    "Config. Perfil ", key="vizu_propried_perfil")
                vizu_formas_pagamento_btn = st.checkbox(
                    "F. Pagamento", key="verifica_formas_pagamento")

            else:
                st.html(
                    f"<div style='text-align:center; background: red; color: white; font-size: 10px;'></div>")
        # Documentação para Implantação
        with st.expander(" :four: Documentação"):
            if numero_ip_alvo != "":
                vizu_motv_devolucao_btn = st.checkbox(
                    "Motivo Devolução", key="vizu_mot_devolucao2")
        st.divider()
    # Engine de conexão com os bancos de dados
    with st.container(border=True):
        try:
            db1_url = f'postgresql+psycopg2://{nome_usuario_banco}:{
                senha_usuario_banco}@{numero_ip_alvo}:5432/{nome_banco_dados_alvo}'
            engine_db1 = create_engine(db1_url)
            Session_db1 = sessionmaker(bind=engine_db1)
            session_db1 = Session_db1()
            print("Conexão com o banco de dados 1 estabelecida com sucesso!")
        except Exception as e:
            print(
                "Ocorreu um problema ao tentar se conectar ao banco de dados 1.")
            if "does not exist" in str(e):
                print("Erro: O banco de dados especificado não existe.")
            elif "authentication failed" in str(e):
                print(
                    "Erro: Falha na autenticação. \n Por favor, verifique o nome de usuário e senha.")
            else:
                print(f"Detalhes do erro: {e}")
        try:
            db2_url = f'postgresql+psycopg2://{nome_usuario_banco}:{
                senha_usuario_banco}@{numero_ip_destino}:5432/{nome_banco_dados_destino}'
            engine_db2 = create_engine(db2_url)
            Session_db2 = sessionmaker(bind=engine_db2)
            session_db2 = Session_db2()
            print("Conexão com o banco de dados 2 estabelecida com sucesso!")
        except Exception as e:
            print(
                "Ocorreu um problema ao tentar se conectar ao banco de dados 2.")
            if "does not exist" in str(e):
                print("Erro: O banco de dados especificado não existe.")
            elif "authentication failed" in str(e):
                print(
                    "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
            else:
                print(f"Detalhes do erro: {e}")

    if numero_ip_alvo == '':
        st.html(
                f"<div style='text-align:center; font-size: 15px;'>O Agilly é um sistema web para abrir novas lojas e filiais no Mercadologic.\nImagine que você está montando uma nova filial para o cliente e precisa\nconfigurar tudo do zero. Com o Agilly, é como se você efetuasse um clone\nda loja principal! Com apenas alguns cliques, o Agilly copia todas as\ninformações importantes da sua loja principal para a nova, como Configurações,\nPerfis, Formas de pagamento e muito mais.\nIsso significa que você não precisa mais digitar tudo de novo, economizando\ntempo e evitando erros.</div>")


    
    def funcoes_copia_parametros(session_db1, session_db2, engine_db1, engine_db2):
        with st.container(border=False):
            st.html(
                f"<div style='text-align:center; background:red; color: white; font-size: 12px;'>SELECIONE A OPÇÃO DE IMPORTAÇÃO PARA COPIA</div>")
            col01, col02, col03 = st.columns(3)
            with col01:
                with st.status("Motivo de Devolução", state="error", expanded=False) as status_motiv_devol:
                    if st.button("Executar Copia", key="copia_motivo_devl"):
                        # Executar a função de transferência de dados
                        fct.Motivo_de_Devolução(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Motivo Desconto", state="error", expanded=False) as state_mot_desc:
                    if st.button("Executar Copia", key="copia_mot_desc"):
                        # Executar a função de transferência de dados
                        fct.Motivo_de_Desconto(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Motivo de Cancelamento", state="error", expanded=False) as status_mot_cancelamento:
                    if st.button("Executar Copia", key="copia_mot_cancel"):
                        # Executar a função de transferência de dados
                        fct.Motivo_de_Cancelamento(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Motivo de Suprimento", state="error", expanded=False) as status_motiv_suprimento:
                    if st.button("Executar Copia", key="copia_motivo_suprimento"):
                        # Executar a função de transferência de dados
                        fct.Motivo_de_Suprimento(
                            session_db1, session_db2, engine_db1, engine_db2)
                with st.status("Modalidade Frete", state="error", expanded=False) as status_mod_frete:
                    if st.button("Executar Copia", key="copia_modalidade_frete",):
                        # Executar a função de transferência de dados
                        fct.modalidade_frete(
                            session_db1, session_db2, engine_db1, engine_db2)        

            with col02:
                with st.status("Motivo de Sangria", state="error", expanded=False) as status_motiv_sangria:
                    if st.button("Executar Copia", key="copia_motivo_samgria"):
                        # Executar a função de transferência de dados
                        fct.Motivo_de_Sangria(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Configurações do Sistema", state="error", expanded=False) as status_config_sistema:
                    if st.button("Executar Copia", key="copia_config_sis"):
                        # Executar a função de transferência de dados
                        fct.Dados_Configuração_do_sistema(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Configurações de Papel", state="error", expanded=False) as status_papel_usuario:
                    if st.button("Executar Copia", key="copia_papel_username"):
                        # Executar a função de transferência de dados
                        fct.Configurações_de_Papel(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Configurações de Papel Central", state="error", expanded=False) as status_papel_central:
                    if st.button("Executar Copia", key="copia_papel_central"):
                        # Executar a função de transferência de dados
                        fct.Configuração_Papel_Central(
                            session_db1, session_db2, engine_db1, engine_db2)

            with col03:
                with st.status("Grupo de Propriedades", state="error", expanded=False) as status_propriedades_grupo:
                    if st.button("Executar Copia", key="copia_propriedades_grupo"):
                        # Executar a função de transferência de dados
                        fct.Configuração_Grupo_de_Propriedades(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Propriedades", state="error", expanded=False) as status_propriedades_sistema:
                    if st.button("Executar Copia", key="copia_propriedades_sistema"):
                        # Executar a função de transferência de dados
                        fct.Configuração_Propriedades(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Propriedades Perfil", state="error", expanded=False) as status_propriedades_perfil:
                    if st.button("Executar Copia", key="copia_propriedades_perfil"):
                        # Executar a função de transferência de dados
                        fct.Configuração_Propriedades_Perfil(
                            session_db1, session_db2, engine_db1, engine_db2)

                with st.status("Formas de Pagamento", state="error", expanded=False) as state_forma_pgto:
                    if st.button("Executar Copia"):
                        # Executar a função de transferência de dados
                        fct.Formas_de_Pagamento(
                            session_db1, session_db2, engine_db1, engine_db2)

                if st.button("Executar Todos", key="botao_executar_todas_copias", type="primary", use_container_width=True):
                    pass

    def inserir_novos_dados():
        with st.container():
            st.html(
                f"<div style='text-align:center; background: #000377; font-size: 12px; color: white;'>APLICAR DADOS</div>")
            col05, col06, col07 = st.columns(3)
            with col05:
                # with st.status("Aplica Novo IP", state="error", expanded=False) as status_motiv_devol:
                with st.status("Geral: Novo IP", state="error", expanded=False) as status_ip:
                    novo_ip_limpo = st.text_input(
                        "Digite o IP da nova loja.", help="IP do concentrador", placeholder="192.168.1.228")
                    novo_ip = "\\\\" + novo_ip_limpo
                    if st.button("Aplicar IP"):
                        fct.aplica_novo_ip(session_db2, engine_db2,
                                           novo_ip, novo_ip_limpo)
       
                with st.status("Frete: Compõe base ICMS"):
                    ativa_base_icms = st.button("Ativar", key="ativa_base_frete_icms", help=None, type="secondary", disabled=False, use_container_width=False)
                    if ativa_base_icms == True:
                            fct.ativa_frete_base_icms(session_db2, engine_db2)
                            st.write("Ativado com sucesso")                                
            with col06:
                with st.status("Empresa: Nova ID", state="error", expanded=False) as status_id:
                    nova_id = st.text_input(
                        "Digite a ID da nova loja", help="ID referente a loja no Director", placeholder="2")
                    if st.button("Aplicar ID"):
                        fct.aplica_nova_id(session_db2, engine_db2, nova_id)
       
                with st.status("Frete: Compõe base PIS/COFINS"):
                    ativa_base_pis_cofins = st.button("Ativar", key="ativa_base_frete_piscofins", help=None, type="secondary", disabled=False, use_container_width=False)
                    if ativa_base_pis_cofins == True:
                        fct.ativa_frete_base_piscofins(session_db2, engine_db2)
            with col07:
                with st.status("Perfil: Codigo CSC", state="error", expanded=False) as status_id:
                    csc_cliente = st.text_input(
                        "Digite o codigo CSC", help="Aplica o codigo CSC enviado pela contabilidade", placeholder="760F6400-C202-40FC-AE4E-A16CD0B918D8")
                    if st.button("Aplicar CSC"):
                        fct.aplica_csc_cliente(
                            session_db2, engine_db2, csc_cliente)

    with st.container():
        if numero_ip_alvo != "":
            with st.container():
                # Funções de Importação e Inserção de Dados
                if botao_opcoes_copia == True:
                    try:
                        funcoes_copia_parametros(
                            session_db1, session_db2, engine_db1, engine_db2)
                    except Exception as e:
                        if "session_db1" in str(e):
                            st.write(
                                "Erro: O banco de dados especificado não existe. session_db1")
                else:
                    st.write("")
                if botao_novos_dados == True:
                    try:
                        inserir_novos_dados()
                    except Exception as e:
                        if "session_db1" in str(e):
                            st.write(
                                "Erro: O banco de dados especificado não existe. session_db1")
                else:
                    st.write("")

            # Visualização de Dados Importados
            with st.container():
                if vizu_motv_devolucao_btn == True:
                    fct.visualiza_mot_devolucao_func(session_db2)

                if vizu_motv_desconto_btn == True:
                    fct.visualiza_mot_desc_func(session_db2)

                if vizu_motv_cancelamento_btn == True:
                    fct.visualiza_mot_cancelamento_func(session_db2)

                if vizu_motv_suprimento_btn == True:
                    fct.visualiza_mot_suprimento_func(session_db2)

                if vizu_motv_sangria_btn == True:
                    fct.visualiza_mot_sangria_func(session_db2)

                if vizu_config_geral_btn == True:
                    fct.visualiza_config_geral_func(session_db2)

                if vizu_config_papel_btn == True:
                    fct.visualiza_config_papel_func(session_db2)

                if vizu_config_papel_central_btn == True:
                    fct.visualiza_config_papel_central_func(session_db2)

                if vizu_propriedade_perfil_btn == True:
                    fct.visualiza_prop_perfil_func(session_db2)

                if vizu_formas_pagamento_btn == True:
                    fct.visualiza_forms_pag_func(session_db2)

    with st.sidebar:
        colsid01, colsid02, colsid03 = st.columns([1, 6, 1])
        with colsid01:
            pass
        with colsid02:
            st.image("agilly_logo.png")
            with st.popover("Sobre", use_container_width=True):
                st.text("O Agilly é um sistema web para abrir novas lojas no Mercadologic.\nImagine que você está montando uma nova filial para o cliente e precisa\nconfigurar tudo do zero. Com o Agilly, é como se você efetuasse um clone\nda loja principal! Com apenas alguns cliques, o Agilly copia todas as\ninformações importantes da sua loja principal para a nova, como Configurações,\nPerfis, Formas de pagamento e muito mais.\nIsso significa que você não precisa mais digitar tudo de novo, economizando\ntempo e evitando erros.")
        with colsid03:
            pass

    colbody01, colbody02, colbody03, colbody04 = st.columns(4)
    with colbody01:
        st.write("")
    with colbody02:
        st.write("")
    with colbody03:
        st.write("")
    with colbody04:
        st.write("")

    colrodp01, colrodp02, colrodp03 = st.columns([6, 1, 6])
    with colrodp01:
        st.write("---")
    with colrodp02:
        st.image("logo_P_P.png", width=40)
        # st.write("Implantação de Lojas Mercadologic")
    with colrodp03:
        st.write("---")


##########################################################################################
# METODOS DE VERIFICAÇÃO DE LOGIN
##########################################################################################
# Verifique o estado de autenticação
is_authenticated = False

# Verifique se o estado de autenticação está presente na sessão
if "is_authenticated" in st.session_state:
    # Se estiver presente, atualize a variável is_authenticated com o valor do estado
    is_authenticated = st.session_state.is_authenticated


# Se o usuário está autenticado, mostre a página protegida
if is_authenticated:
    pagina_protegida()

else:
    # Se o usuário não estiver autenticado, chame a função de login

    is_authenticated = login()

    # Se o usuário foi autenticado com sucesso
    if is_authenticated:
        # Defina o estado de autenticação como verdadeiro na sessão
        st.session_state.is_authenticated = True

        # Redirecione para a página protegida alterando os parâmetros da URL
        # st.query_params(authenticated="true")
        st.rerun()
