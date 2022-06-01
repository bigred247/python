## count number of times completed exists in column atomic_status using SUM ###
select
sum(
case atomic_status  
	when 'COMPLETED' then 1 else 0
end 
) as rating_COMP,
sum(
case atomic_status  
	when 'FAILED' then 1 else 0
end 
) as rating_FAIL
from alerts