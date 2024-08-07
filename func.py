﻿import streamlit as st
import pandas as pd
from sqlalchemy.sql import text

############################ Funções de Inserção e Copia de dados #########################


def Dados_Configuração_do_sistema(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_configuracao_conc = text(
            "SELECT chave, valor FROM configuracao")
        resultado_query_configuracao = session_db1.execute(
            query_configuracao_conc).fetchall()
        # resultado_query_configuracao

        for row_config in resultado_query_configuracao:
            # row_config
            insert_query_configuracao = text(
                """UPDATE public.configuracao
                            SET
                            valor = :valor
                            WHERE chave= :chave;
                        """
            )
            params_empresa_config = {
                'chave': row_config[0],
                'valor': row_config[1] or None
            }
            session_db2.execute(insert_query_configuracao,
                                params_empresa_config)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Formas_de_Pagamento(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_formas_pag_conc = text("SELECT * from formapagamento")
        resultado_query_formas_pag = session_db1.execute(
            query_formas_pag_conc).fetchall()

        ################################
        for row_formas_pag in resultado_query_formas_pag:
            insert_query_formas_pag = text(
                """INSERT INTO public.formapagamento (
                            id, nome, ordemenvio, permitetroco, enviaimpressora, permitesangria, funcaoteclado,
                            crediario, forma_pagamento_sefaz, modificado, desativado, cartao_pos, limite_sangria,
                            exibir_pdv, id_forma_pai, convenio, incluir_cliente_crediario, limite_valor_cheque,
                            limite_troco_cheque, validar_cliente, solicitar_fiscal, uid, converte_troco_em_vale_compra,
                            integra_tef, id_operacao, venda_a_prazo, solicita_confirmacao, identificar_cliente
                        ) VALUES (
                            :id, :nome, :ordemenvio, :permitetroco, :enviaimpressora, :permitesangria, :funcaoteclado,
                            :crediario, :forma_pagamento_sefaz, :modificado, :desativado, :cartao_pos, :limite_sangria,
                            :exibir_pdv, :id_forma_pai, :convenio, :incluir_cliente_crediario, :limite_valor_cheque,
                            :limite_troco_cheque, :validar_cliente, :solicitar_fiscal, :uid, :converte_troco_em_vale_compra,
                            :integra_tef, :id_operacao, :venda_a_prazo, :solicita_confirmacao, :identificar_cliente
                        )
                        ON CONFLICT (id)
                        DO UPDATE SET
                            nome = EXCLUDED.nome,
                            ordemenvio = EXCLUDED.ordemenvio,
                            permitetroco = EXCLUDED.permitetroco,
                            enviaimpressora = EXCLUDED.enviaimpressora,
                            permitesangria = EXCLUDED.permitesangria,
                            funcaoteclado = EXCLUDED.funcaoteclado,
                            crediario = EXCLUDED.crediario,
                            forma_pagamento_sefaz = EXCLUDED.forma_pagamento_sefaz,
                            modificado = EXCLUDED.modificado,
                            desativado = EXCLUDED.desativado,
                            cartao_pos = EXCLUDED.cartao_pos,
                            limite_sangria = EXCLUDED.limite_sangria,
                            exibir_pdv = EXCLUDED.exibir_pdv,
                            id_forma_pai = EXCLUDED.id_forma_pai,
                            convenio = EXCLUDED.convenio,
                            incluir_cliente_crediario = EXCLUDED.incluir_cliente_crediario,
                            limite_valor_cheque = EXCLUDED.limite_valor_cheque,
                            limite_troco_cheque = EXCLUDED.limite_troco_cheque,
                            validar_cliente = EXCLUDED.validar_cliente,
                            solicitar_fiscal = EXCLUDED.solicitar_fiscal,
                            uid = EXCLUDED.uid,
                            converte_troco_em_vale_compra = EXCLUDED.converte_troco_em_vale_compra,
                            integra_tef = EXCLUDED.integra_tef,
                            id_operacao = EXCLUDED.id_operacao,
                            venda_a_prazo = EXCLUDED.venda_a_prazo,
                            solicita_confirmacao = EXCLUDED.solicita_confirmacao,
                            identificar_cliente = EXCLUDED.identificar_cliente;
                        """
            )

            params_formas_pag = {
                'id': row_formas_pag[0],
                'nome': row_formas_pag[1],
                'ordemenvio': row_formas_pag[2] or None,
                'permitetroco': row_formas_pag[3] or False,
                'enviaimpressora': row_formas_pag[4] or False,
                'permitesangria': row_formas_pag[5] or False,
                'funcaoteclado': row_formas_pag[6] or True,
                'crediario': row_formas_pag[7] or False,
                'forma_pagamento_sefaz': row_formas_pag[8] or True,
                'modificado': row_formas_pag[9] or True,
                'desativado': row_formas_pag[10] or None,
                'cartao_pos': row_formas_pag[11] or False,
                'limite_sangria': row_formas_pag[12],
                'exibir_pdv': row_formas_pag[13] or True,
                'id_forma_pai': row_formas_pag[14] or None,
                'convenio': row_formas_pag[15] or False,
                'incluir_cliente_crediario': row_formas_pag[16] or False,
                'limite_valor_cheque': row_formas_pag[17] or 0,
                'limite_troco_cheque': row_formas_pag[18] or 0,
                'validar_cliente': row_formas_pag[19] or False,
                'solicitar_fiscal': row_formas_pag[20] or False,
                'converte_troco_em_vale_compra': row_formas_pag[21] or False,
                'integra_tef': row_formas_pag[22] or False,
                'id_operacao': row_formas_pag[23],
                'venda_a_prazo': row_formas_pag[24] or False,
                'solicita_confirmacao': row_formas_pag[25] or False,
                'uid': row_formas_pag[26],
                'identificar_cliente': row_formas_pag[27] or False
            }
            session_db2.execute(insert_query_formas_pag, params_formas_pag)
        ################################
        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Motivo_de_Desconto(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_motivo_desc = text("select * from motivo_desconto")
        resultado_query_motivo_desc = session_db1.execute(
            query_motivo_desc).fetchall()
        # resultado_query_motivo_desc

        ################################
        for row_motivo_desc in resultado_query_motivo_desc:
            insert_query_motivo_desc = text(
                """INSERT INTO public.motivo_desconto (id, descricao, modificado, desativado)
                            VALUES(:id, :descricao, :modificado, :desativado)
                            ON CONFLICT (id)
                            DO UPDATE SET descricao = EXCLUDED.descricao,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado;
                            """
            )
            params_motivo_desc = {
                'id': row_motivo_desc[0],
                'descricao': row_motivo_desc[1],
                'modificado': row_motivo_desc[2] or True,
                'desativado': row_motivo_desc[3] or None
            }
            session_db2.execute(
                insert_query_motivo_desc, params_motivo_desc)

        # Confirmar transações
        session_db2.commit()

        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Motivo_de_Cancelamento(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_motivo_canc = text("select  * from motivocancelamento")
        resultado_query_motivo_canc = session_db1.execute(
            query_motivo_canc).fetchall()
        # resultado_query_motivo_canc

        for row_motivo_canc in resultado_query_motivo_canc:
            insert_query_motivo_canc = text(
                """INSERT INTO public.motivocancelamento (id, descricao, modificado, desativado)
                            VALUES(:id, :descricao, :modificado, :desativado)
                            ON CONFLICT (id)
                            DO UPDATE SET descricao = EXCLUDED.descricao,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado;
                            """
            )
            params_motivo_canc = {
                'id': row_motivo_canc[0],
                'descricao': row_motivo_canc[1],
                'modificado': row_motivo_canc[2] or True,
                'desativado': row_motivo_canc[3] or None
            }
            session_db2.execute(
                insert_query_motivo_canc, params_motivo_canc)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Motivo_de_Devolução(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_motivo_dev = text("select  * from motivo_devolucao")
        resultado_query_motivo_dev = session_db1.execute(
            query_motivo_dev).fetchall()
        # resultado_query_motivo_dev

        for row_motivo_dev in resultado_query_motivo_dev:
            insert_query_motivo_dev = text(
                """INSERT INTO public.motivo_devolucao (id, descricao, modificado, desativado)
                            VALUES(:id, :descricao, :modificado, :desativado)
                            ON CONFLICT (id)
                            DO UPDATE SET descricao = EXCLUDED.descricao,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado;
                            """
            )
            params_motivo_dev = {
                'id': row_motivo_dev[0],
                'descricao': row_motivo_dev[1],
                'modificado': row_motivo_dev[2] or False,
                'desativado': row_motivo_dev[3] or None
            }
            session_db2.execute(insert_query_motivo_dev, params_motivo_dev)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Motivo_de_Sangria(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_motivo_san = text("select  * from motivo_sangria")
        resultado_query_motivo_san = session_db1.execute(
            query_motivo_san).fetchall()
        # resultado_query_motivo_san

        for row_motivo_san in resultado_query_motivo_san:
            insert_query_motivo_san = text(
                """INSERT INTO public.motivo_sangria (id, descricao,existe_envelope, modificado, desativado)
                            VALUES(:id, :descricao, :existe_envelope, :modificado, :desativado)
                            ON CONFLICT (id)
                            DO UPDATE SET descricao = EXCLUDED.descricao,
                                        existe_envelope = EXCLUDED.existe_envelope,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado;
                            """
            )
            params_motivo_san = {
                'id': row_motivo_san[0],
                'descricao': row_motivo_san[1],
                'existe_envelope': row_motivo_san[2] or False,
                'modificado': row_motivo_san[3] or False,
                'desativado': row_motivo_san[4] or None
            }
            session_db2.execute(insert_query_motivo_san, params_motivo_san)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Motivo_de_Suprimento(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_motivo_sup = text("select  * from motivo_suprimento")
        resultado_query_motivo_sup = session_db1.execute(
            query_motivo_sup).fetchall()
        # resultado_query_motivo_sup

        for row_motivo_sup in resultado_query_motivo_sup:
            insert_query_motivo_sup = text(
                """INSERT INTO public.motivo_suprimento (id, descricao,modificado, desativado)
                            VALUES(:id, :descricao, :modificado, :desativado)
                            ON CONFLICT (id)
                            DO UPDATE SET descricao = EXCLUDED.descricao,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado;
                            """
            )
            params_motivo_sup = {
                'id': row_motivo_sup[0],
                'descricao': row_motivo_sup[1],
                'modificado': row_motivo_sup[2] or False,
                'desativado': row_motivo_sup[3] or None
            }
            session_db2.execute(insert_query_motivo_sup, params_motivo_sup)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Configurações_de_Papel(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_papel_usuario = text("select  * from papel")
        resultado_query_papel_usuario = session_db1.execute(
            query_papel_usuario).fetchall()
        resultado_query_papel_usuario

        for row_papel_usuario in resultado_query_papel_usuario:
            insert_query_papel_usuario = text(
                """INSERT INTO public.papel (id, nome, modificado, desativado, perc_desc_max_final_cupom,perc_desc_max_item, uid )
                            VALUES(:id, :nome, :modificado, :desativado, :perc_desc_max_final_cupom, :perc_desc_max_item, :uid)
                            ON CONFLICT (id)
                            DO UPDATE SET nome = EXCLUDED.nome,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado,
                                        perc_desc_max_final_cupom = EXCLUDED.perc_desc_max_final_cupom,
                                        perc_desc_max_item = EXCLUDED.perc_desc_max_item,
                                        uid = EXCLUDED.uid ;
                            """
            )
            params_papel_usuario = {
                'id': row_papel_usuario[0],
                'nome': row_papel_usuario[1],
                'modificado': row_papel_usuario[2] or True,
                'desativado': row_papel_usuario[3] or None,
                'perc_desc_max_final_cupom': row_papel_usuario[3] or 0,
                'perc_desc_max_item': row_papel_usuario[3] or 0,
                'uid': row_papel_usuario[3] or None
            }
            session_db2.execute(insert_query_papel_usuario,
                                params_papel_usuario)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Configuração_Papel_Central(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_papel_central = text("select  * from papelconcentrador")
        resultado_query_papel_central = session_db1.execute(
            query_papel_central).fetchall()
        # resultado_query_papel_central

        for row_papel_central in resultado_query_papel_central:
            insert_query_papel_central = text(
                """INSERT INTO public.papelconcentrador (id, nome, modificado, desativado)
                            VALUES(:id, :nome, :modificado, :desativado)
                            ON CONFLICT (id)
                            DO UPDATE SET nome = EXCLUDED.nome,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado;
                            """
            )
            params_papel_central = {
                'id': row_papel_central[0],
                'nome': row_papel_central[1],
                'modificado': row_papel_central[2] or False,
                'desativado': row_papel_central[3] or None
            }
            session_db2.execute(insert_query_papel_central,
                                params_papel_central)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


# (Depende dos usuarios cadastrados, não e util.)
def Configuração_Papel_Central_Tela(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_papel_central_tela = text(
            "select  * from papelconcentradortela")
        resultado_query_papel_central_tela = session_db1.execute(
            query_papel_central_tela).fetchall()
        # resultado_query_papel_central_tela

        for row_papel_central_tela in resultado_query_papel_central_tela:
            insert_query_papel_central_tela = text(
                """INSERT INTO public.papelconcentradortela (id, idtela, idpapelconcentrador, modificado, desativado)
                            VALUES(:id, :idtela, :idpapelconcentrador, :modificado, :desativado)
                            ON CONFLICT (id)
                            DO UPDATE SET idtela = EXCLUDED.idtela,
                                        idpapelconcentrador = EXCLUDED.idpapelconcentrador,
                                        modificado = EXCLUDED.modificado,
                                        desativado = EXCLUDED.desativado;
                            """
            )
            params_papel_central_tela = {
                'id': row_papel_central_tela[0],
                'idtela': row_papel_central_tela[1],
                'idpapelconcentrador': row_papel_central_tela[2],
                'modificado': row_papel_central_tela[3] or False,
                'desativado': row_papel_central_tela[4] or None
            }
            session_db2.execute(insert_query_papel_central_tela,
                                params_papel_central_tela)

        # Confirmar transações
        session_db2.commit()
        # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


# (Colocar Seletor de  PDV para copia.)
def Configuração_Propriedades_Perfil(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_prop_perfil = text(
            "select * from propriedadeperfil p where p.idperfilpdv = '1'")
        resultado_query_prop_perfil = session_db1.execute(
            query_prop_perfil).fetchall()
        # resultado_query_prop_perfil

        for row_prop_perfil in resultado_query_prop_perfil:
            insert_query_prop_perfil = text(
                """INSERT INTO public.propriedadeperfil (id, desativado, modificado,  idperfilpdv, valor )
                                VALUES(:id, :desativado, :modificado, :idperfilpdv, :valor)
                                ON CONFLICT (id)
                                DO UPDATE SET desativado = EXCLUDED.desativado,
                                            modificado = EXCLUDED.modificado,
                                            idperfilpdv = EXCLUDED.idperfilpdv,
                                            valor = EXCLUDED.valor;
                                """
            )
            params_prop_perfil = {
                'id': row_prop_perfil[0],
                'desativado': row_prop_perfil[1] or None,
                'modificado': row_prop_perfil[2] or True,
                'idpropriedade': row_prop_perfil[3] or None,
                'idperfilpdv': 1,
                'valor': row_prop_perfil[5]
            }
            session_db2.execute(insert_query_prop_perfil,
                                params_prop_perfil)

            # Confirmar transações
            session_db2.commit()
            # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()
    # Fechar as sessões
    session_db1.close()
    session_db2.close()
    # Fechar os engines
    engine_db1.dispose()
    engine_db2.dispose()


def Configuração_Propriedades(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_propriedades = text(
            "select * from propriedade p ")
        resultado_query_propriedades = session_db1.execute(
            query_propriedades).fetchall()
        # resultado_query_propriedades

        for row_propriedades in resultado_query_propriedades:
            insert_query_propriedades = text(
                """INSERT INTO public.propriedade (id, nome, descricao, idgrupopropriedade, modificado, desativado, versao, tipo, valor_padrao )
                                VALUES(:id, :nome, :descricao, :idgrupopropriedade, :modificado, :desativado, :versao, :tipo, :valor_padrao)
                                ON CONFLICT (nome)
                                DO UPDATE SET id = EXCLUDED.id,
                                            descricao = EXCLUDED.descricao,
                                            idgrupopropriedade = EXCLUDED.idgrupopropriedade,
                                            modificado = EXCLUDED.modificado,
                                            desativado = EXCLUDED.desativado,
                                            versao = EXCLUDED.versao,
                                            tipo = EXCLUDED.tipo,
                                            valor_padrao = EXCLUDED.valor_padrao;
                                """
            )
            params_propriedades = {
                'id': row_propriedades[0],
                'nome': row_propriedades[1],
                'descricao': row_propriedades[2],
                'idgrupopropriedade': row_propriedades[3],
                'modificado': row_propriedades[4] or False,
                'desativado': row_propriedades[5] or None,
                'versao': row_propriedades[6] or None,
                'tipo': row_propriedades[7],
                'valor_padrao': row_propriedades[8]
            }
            session_db2.execute(insert_query_propriedades,
                                params_propriedades)

            # Confirmar transações
            session_db2.commit()
            # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def Configuração_Grupo_de_Propriedades(session_db1, session_db2, engine_db1, engine_db2):
    try:
        query_Grupo_propriedades = text(
            "select * from grupopropriedade g")
        resultado_query_Grupo_propriedades = session_db1.execute(
            query_Grupo_propriedades).fetchall()
        # resultado_query_Grupo_propriedades

        for row_Grupo_propriedades in resultado_query_Grupo_propriedades:
            insert_query_Grupo_propriedades = text(
                """INSERT INTO public.grupopropriedade (id, nome, desativado, modificado, idperfilgrupo )
                                VALUES(:id, :nome, :desativado, :modificado, :idperfilgrupo)
                                ON CONFLICT (id)
                                DO UPDATE SET nome = EXCLUDED.nome,
                                            desativado = EXCLUDED.desativado,
                                            modificado = EXCLUDED.modificado,
                                            idperfilgrupo = EXCLUDED.idperfilgrupo;
                                """
            )
            params_Grupo_propriedades = {
                'id': row_Grupo_propriedades[0],
                'nome': row_Grupo_propriedades[1],
                'desativado': row_Grupo_propriedades[2] or None,
                'modificado': row_Grupo_propriedades[3] or False,
                'idperfilgrupo': row_Grupo_propriedades[4]
            }
            session_db2.execute(insert_query_Grupo_propriedades,
                                params_Grupo_propriedades)

            # Confirmar transações
            session_db2.commit()
            # Fechar as sessões
        session_db1.close()
        session_db2.close()
        # Fechar os engines
        engine_db1.dispose()
        engine_db2.dispose()
        st.write("Copia Efetuada com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def aplica_novo_ip(session_db2, engine_db2, novo_ip, novo_ip_limpo):
    try:
        ################################
        insert_aplica_ip = text(
            f"""UPDATE public.configuracao SET valor='{novo_ip}\Mercadologic\Importacao', descricao='Indica o caminho onde se encontra os arquivos na máquina local a serem importados.', modificado=true, desativado=NULL WHERE chave='caminho.importacao.arquivos.director.local';
                            """
        )
        insert_aplica_ip2 = text(
            f"""UPDATE public.configuracao SET valor='{novo_ip}\Mercadologic\Importacao', descricao='Indica o caminho onde os arquivos serão exportados do Director para a máquina do Concentrador (caminho de rede).', modificado=true, desativado=NULL WHERE chave='caminho.exportacao.arquivos.director';
                            """
        )
        insert_aplica_ip_pdv_bd = text(
            f"""UPDATE public.propriedadeperfil SET desativado=NULL, modificado=true, idpropriedade=3, idperfilpdv=1, valor='jdbc:postgresql://{novo_ip_limpo}:5432/DBMercadologic' WHERE id=3;
                            """
        )
        insert_aplica_ip_pdv_rede = text(
            f"""UPDATE public.propriedadeperfil SET desativado=NULL, modificado=true, idpropriedade=148, idperfilpdv=1, valor='{novo_ip_limpo}' WHERE id=148;
                            """
        )
        insert_aplica_ip_pdv_bridge = text(
            f"""UPDATE public.propriedadeperfil SET desativado=NULL, modificado=true, idpropriedade=249, idperfilpdv=1, valor='{novo_ip_limpo}' WHERE id=248;
                            """
        )

        session_db2.execute(
            insert_aplica_ip)

        session_db2.execute(
            insert_aplica_ip2)

        session_db2.execute(
            insert_aplica_ip_pdv_bd)

        session_db2.execute(
            insert_aplica_ip_pdv_rede)

        session_db2.execute(
            insert_aplica_ip_pdv_bridge)

        # Confirmar transações
        session_db2.commit()

        # Fechar as sessões
        # session_db1.close()
        session_db2.close()
        # Fechar os engines
        # engine_db1.dispose()
        engine_db2.dispose()
        st.write("IP inserido com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def aplica_nova_id(session_db2, engine_db2, nova_id):
    try:
        ################################
        insert_id_loja = text(
            f"""UPDATE public.configuracao SET valor='{nova_id}', descricao='Código da empresa cadastrado no Director que será utilizado para importar os dados para o Concentrador.', modificado=true, desativado=NULL WHERE chave='codigo.empresa.padrao';
                            """
        )

        session_db2.execute(
            insert_id_loja)

        # Confirmar transações
        session_db2.commit()

        # Fechar as sessões
        # session_db1.close()
        session_db2.close()
        # Fechar os engines
        # engine_db1.dispose()
        engine_db2.dispose()
        st.write("ID inserida com Sucesso")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()


def aplica_csc_cliente(session_db2, engine_db2, csc_cliente):
    try:
        ################################
        insert_csc_loja = text(
            f"""UPDATE public.propriedadeperfil SET desativado=NULL, modificado=true, idpropriedade=119, idperfilpdv=1, valor='{csc_cliente}' WHERE id=119;
                            """
        )
        muda_prod_hom = text(
            f"""UPDATE public.propriedadeperfil SET desativado=NULL, modificado=true, idpropriedade=117, idperfilpdv=1, valor='2' WHERE id=117;
                             """)

        session_db2.execute(
            insert_csc_loja)
        session_db2.execute(
            muda_prod_hom)

        # Confirmar transações
        session_db2.commit()

        # Fechar as sessões
        # session_db1.close()
        session_db2.close()
        # Fechar os engines
        # engine_db1.dispose()
        engine_db2.dispose()
        st.write("CSC inserido com Sucesso e banco configurado para Homologação")
    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
        session_db2.rollback()

####################### FUNÇOES DE ATUALIZAÇAO DE DADOS IMPORTADOS #####################


def visualiza_config_geral_func(session_db2):

    try:
        visualiza_config_geral = text(
            f"""select c.descricao,c.valor from configuracao c
                order by descricao asc
                ;"""
        )
        vizu_config_geral = session_db2.execute(
            visualiza_config_geral).fetchall()
        vizu_config_geral = pd.DataFrame(vizu_config_geral)
        st.dataframe(vizu_config_geral,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_config_papel_func(session_db2):

    try:
        visualiza_config_papel = text(
            f"""select pp.id as id_papel, pp.nome as nome_operacao, u.nomereduzido as nome_user, u.id ,u.login, u.senha , o.nome_reduzido ,o.imprimir,o.asciioperacao, o.visivel_usuario from papeloperacao p
            inner join operacao o on p.idoperacao = o.id
            inner join papel pp on pp.id = p.idpapel
            inner join papelusuario p2 on pp.id = p.idpapel
            inner join usuario u on p2.idusuario = u.id ;"""
        )
        vizu_config_papel = session_db2.execute(
            visualiza_config_papel).fetchall()
        vizu_config_papel = pd.DataFrame(vizu_config_papel)

        col100, col200 = st.columns(2)
        with col100:
            vizu_papel_nome_usuario = vizu_config_papel["nome_user"].unique(
            )
            selectbox_nome_usuario_papel = st.selectbox(
                "Selecione o Usuario", vizu_papel_nome_usuario)
            vizu_papel_nome_usuario_df = vizu_config_papel[vizu_config_papel['nome_user']
                                                           == selectbox_nome_usuario_papel]

        with col200:
            vizu_papel_nome_operacao = vizu_papel_nome_usuario_df['nome_operacao'].unique(
            )
            selectbox_nome_operacao_papel = st.selectbox(
                "Selecione a Operacao", vizu_papel_nome_operacao)
            vizu_papel_nome_operacao_df = vizu_papel_nome_usuario_df[
                vizu_papel_nome_usuario_df["nome_operacao"] == selectbox_nome_operacao_papel]
            vizu_papel_nome_operacao_df['valor'] = vizu_papel_nome_operacao_df['valor'].replace({
                                                                                                True: 'Ativado'})

        st.dataframe(vizu_papel_nome_operacao_df,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_config_papel_central_func(session_db2):

    try:
        visualiza_config_papel_central = text(
            f"""select pc.id, pc.nome from papelconcentrador pc;"""
        )
        vizu_config_papel_central = session_db2.execute(
            visualiza_config_papel_central).fetchall()
        vizu_config_papel_central = pd.DataFrame(vizu_config_papel_central)
        st.dataframe(vizu_config_papel_central,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_config_grupo_propriedades_func(session_db2):

    try:
        visualiza_grupo_propriedades = text(
            f"""select f.id,f.nome as tipo,f.forma_pagamento_sefaz as sefaz,o.nome as operacao , f.exibir_pdv,f.id_forma_pai as Menu_Pai, f.integra_tef from formapagamento f
        inner join operacao o on f.id_operacao = o.id order by f.id asc;"""
        )
        vizu_grupo_propriedade = session_db2.execute(
            visualiza_grupo_propriedades).fetchall()
        vizu_grupo_propriedade = pd.DataFrame(vizu_grupo_propriedade)
        st.dataframe(vizu_grupo_propriedade,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_mot_desc_func(session_db2):

    try:
        visualiza_motiv_desc = text(
            f"""select descricao from motivo_desconto md;"""
        )
        vizu_motivo_desc = session_db2.execute(
            visualiza_motiv_desc).fetchall()
        vizu_motivo_desc = pd.DataFrame(vizu_motivo_desc)
        st.dataframe(vizu_motivo_desc,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_mot_devolucao_func(session_db2):

    try:
        visualiza_motiv_devolucao = text(
            f"""select md.id, md.descricao from motivo_devolucao md;"""
        )
        vizu_motivo_devolucao = session_db2.execute(
            visualiza_motiv_devolucao).fetchall()
        vizu_motivo_devolucao = pd.DataFrame(vizu_motivo_devolucao)
        st.dataframe(vizu_motivo_devolucao,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_mot_cancelamento_func(session_db2):

    try:
        visualiza_motiv_cancelamento = text(
            f"""select mcl.id, mcl.descricao from motivocancelamento mcl;"""
        )
        vizu_motivo_cancelamento = session_db2.execute(
            visualiza_motiv_cancelamento).fetchall()
        vizu_motivo_cancelamento = pd.DataFrame(vizu_motivo_cancelamento)
        st.dataframe(vizu_motivo_cancelamento,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_mot_sangria_func(session_db2):

    try:
        visualiza_motiv_sangria = text(
            f"""select ms.id, ms.descricao, ms.existe_envelope from motivo_sangria ms;""")
        vizu_motivo_sangria = session_db2.execute(
            visualiza_motiv_sangria).fetchall()
        vizu_motivo_sangria = pd.DataFrame(vizu_motivo_sangria)
        st.dataframe(vizu_motivo_sangria,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_mot_suprimento_func(session_db2):

    try:
        visualiza_motiv_suprimento = text(
            f"""select msp.id, msp.descricao from motivo_suprimento msp;"""
        )
        vizu_motivo_suprimento = session_db2.execute(
            visualiza_motiv_suprimento).fetchall()
        vizu_motivo_suprimento = pd.DataFrame(vizu_motivo_suprimento)
        st.dataframe(vizu_motivo_suprimento,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_forms_pag_func(session_db2):

    try:
        visualiza_forms_pag = text(
            f"""select f.id,f.nome as tipo,f.forma_pagamento_sefaz as sefaz,o.nome as operacao , f.exibir_pdv,f.id_forma_pai as Menu_Pai, f.integra_tef from formapagamento f
        inner join operacao o on f.id_operacao = o.id order by f.id asc;"""
        )
        formas_importadas = session_db2.execute(visualiza_forms_pag).fetchall()
        formas_importadas = pd.DataFrame(formas_importadas)
        st.dataframe(formas_importadas,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_prop_perfil_func(session_db2):

    try:
        visualiza_prop_perfil = text(
            f"""select gprd.nome as tipo, pfgr.nome as local, prd.descricao as descrição, prd.valor_padrao as valor, prd.versao as versao  from grupopropriedade gprd
        inner join propriedade prd on gprd.id = prd.idgrupopropriedade
        inner join perfilgrupo pfgr ON gprd.idperfilgrupo = pfgr.id order by gprd.nome asc;"""
        )
        prop_perfil_importado = session_db2.execute(
            visualiza_prop_perfil).fetchall()
        prop_perfil_importado = pd.DataFrame(prop_perfil_importado)

        col100, col200 = st.columns(2)
        with col100:
            prop_perfil_local = prop_perfil_importado['local'].unique()
            selectbox_local_config_perfil = st.selectbox(
                "Selecione Local", prop_perfil_local)
            prop_perfil_importado_local = prop_perfil_importado[prop_perfil_importado["local"]
                                                                == selectbox_local_config_perfil]

        with col200:
            prop_perfil_tipo = prop_perfil_importado_local['tipo'].unique()
            selectbox_tipo_config_perfil = st.selectbox(
                "Selecione Tipo", prop_perfil_tipo)
            prop_perfil_importado_tipo = prop_perfil_importado_local[prop_perfil_importado_local["tipo"]
                                                                     == selectbox_tipo_config_perfil]

        st.dataframe(prop_perfil_importado_tipo,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()


def visualiza_prop_geral_func(session_db2):

    try:
        visualiza_prop_geral = text(
            f"""select descricao,valor_padrao, versao  from propriedade;"""
        )
        prop_geral_importado = session_db2.execute(
            visualiza_prop_geral).fetchall()
        prop_geral_importado = pd.DataFrame(prop_geral_importado)
        st.dataframe(prop_geral_importado,
                     use_container_width=True, hide_index=True)

    except Exception as e:
        if "does not exist" in str(e):
            st.write("Erro: O banco de dados especificado não existe.")
        elif "authentication failed" in str(e):
            st.write(
                "Erro: Falha na autenticação. Por favor, verifique o nome de usuário e senha.")
        elif "utf-8" in str(e):
            st.write("Erro: IP com erro, verifique o ip digitado.")
        else:
            st.write(f"Detalhes do erro: {e}")
    finally:
        # Fechar a sessão DB2
        session_db2.close()
