
## grab all rows in table ##
select *
from alerts

## example 1 ##
select case
	when exists (select ATOMIC_STATUS
				 from alerts
				 where atomic_status = 'FAILED') then 1
	else 2
end

## exzmple 2 ##
select batchid,
case
	when (batchid <= 100) then'gold'
	when (batchid <= 300) then'silver'
	when (batchid <= 400) then'bronze'
	else 'cheapskate'
end as customer_class
from alerts

## example 3 ##
select atomic_status,
case atomic_status 
	when 'COMPLETED' then 'COMPLETED'
	when 'STARTED' then 'STARTED'
	when 'INITIALISING' then 'INITIALISING'
	when 'FAILED' then 'FAILED'
	else 'UNKNOWN'
end as current_atomic_status
from alerts


### single column in case ###
select landing_status,
case landing_status 
	when 'COMPLETED' then 'COMPLETED'
	when 'STARTED' then 'STARTED'
	when 'INITIALISING' then 'INITIALISING'
	when 'FAILED' then 'FAILED'
	else 'UNKNOWN'
end as current_landing_status
from alerts


### multiple columns in case ###
select
case 
	when atomic_status like 'FAILED' then 'FAILED'
	when landing_status like 'FAILED' then 'FAILED'
	else 'JOB STILL RUNNING'
end matching_status
from alerts

