SELECT *

FROM item_pedido AS t1

LEFT JOIN produto AS t2
ON t1.descItem = t2.descitem

WHERE descTipoItem like'%massa%'