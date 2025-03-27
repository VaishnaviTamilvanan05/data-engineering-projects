
    
    

select
    SalesOrderID as unique_field,
    count(*) as n_records

from `hive_metastore`.`saleslt`.`dim_sales`
where SalesOrderID is not null
group by SalesOrderID
having count(*) > 1


