select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select SalesOrderID
from `hive_metastore`.`saleslt`.`dim_sales`
where SalesOrderID is null



      
    ) dbt_internal_test