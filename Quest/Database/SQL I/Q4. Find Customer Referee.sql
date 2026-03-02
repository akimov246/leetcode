select customer.name
from customer
left join customer as referee
on customer.referee_id = referee.id
where customer.referee_id != 2 or customer.referee_id is null;