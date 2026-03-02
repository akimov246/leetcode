select employees.employee_id
from employees
full join employees as managers
on employees.manager_id = managers.employee_id
where public.employees.salary < 30000
and
employees.manager_id not in (select employees.employee_id from employees)
order by employee_id;