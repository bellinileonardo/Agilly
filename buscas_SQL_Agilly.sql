select * from propriedadeperfil p where idperfilpdv = '1'

select * from modalidade_frete mf 

select f.id,f.nome as tipo,f.forma_pagamento_sefaz as sefaz,o.nome as operacao , f.exibir_pdv,f.id_forma_pai as Menu_Pai, f.integra_tef from formapagamento f 
inner join operacao o on f.id_operacao = o.id order by f.id asc

select descricao from motivo_desconto md 

select md.id, md.descricao from motivo_devolucao md 

select mcl.id, mcl.descricao from motivocancelamento mcl 

select ms.id, ms.descricao, ms.existe_envelope from motivo_sangria ms 

select msp.id, msp.descricao from motivo_suprimento msp 

select pc.id, pc.nome from papelconcentrador pc 

select  * from grupopropriedade gprd 
inner join propriedade prd on gprd.id = prd.idgrupopropriedade 
inner join perfilgrupo pfgr ON gprd.idperfilgrupo = pfgr.id 


select gprd.nome as tipo, pfgr.nome as local, prd.descricao as descrição, prd.versao as versao, prd.valor_padrao as valor  from grupopropriedade gprd
        inner join propriedade prd on gprd.id = prd.idgrupopropriedade
        inner join perfilgrupo pfgr ON gprd.idperfilgrupo = pfgr.id order by gprd.nome asc;


select * from perfilgrupo p 

select * from propriedade

select * from grupopropriedade g 

select * from retorno_sefaz rs 

select c.descricao,c.valor from configuracao c 
order by descricao asc

select p.nome, p.perc_desc_max_final_cupom as desc_cupom, p.perc_desc_max_item as desc_item from papel p



select * from versao



select modalidade_desconto, sum(cupom_total_liquido) as Liquido, sum(desconto_total) as Desconto from vw_relatorio_desconto vrd 
where id_modalidade_promocional = 4
and cupom_cancelado = false 
and cupom_data_abertura between '2024-06-01' and '2024-06-30'
group by modalidade_desconto 



select  * from papel p
inner join papelusuario p2 on p.id = p2.idpapel 

select * from papelconcentrador p 

select  * from papelconcentradortela p 

select * from papelconcentradorusuario p 

select pp.id as id_papel, pp.nome as nome_operacao, u.nomereduzido as nome_user, u.id ,u.login, u.senha , o.nome_reduzido ,o.imprimir,o.asciioperacao, o.visivel_usuario from papeloperacao p 
inner join operacao o on p.idoperacao = o.id 
inner join papel pp on pp.id = p.idpapel 
inner join papelusuario p2 on pp.id = p.idpapel 
inner join usuario u on p2.idusuario = u.id 

select * from operacao o 

select  * from papelusuario p #


select
icf.id,
cf.datafechamento,
i.id as cod_item,
i.nome,
i.desc_categoria ,
cfe.cupom_fiscal,
cfe.url_qrcode,
cfe.numero as nfce,
cfe.serie,
icf.quantidade,
icf.preco ,
icf.desconto,
icf.totaldesconto ,
icf.totalliquido 
from cupom_fiscal_eletronico cfe 
inner join cupomfiscal cf 
on cfe.chave_eletronica = cf.chave
inner join itemcupomfiscal icf
on icf.idcupomfiscal = cfe.cupom_fiscal
inner join item i 
on icf.iditem = i.id  
WHERE cf.datafechamento between current_date -60 and now() 
AND icf.cancelado = 'False'
AND cf.cancelado = 'False'
AND cf.fechado = 'True'
AND cf.totalizado = 'True'
