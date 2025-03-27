
    
    

select
    saleOrderID as unique_field,
    count(*) as n_records

from `hive_metastore`.`saleslt`.`dim_sales`
where saleOrderID is not null
group by saleOrderID
having count(*) > 1


