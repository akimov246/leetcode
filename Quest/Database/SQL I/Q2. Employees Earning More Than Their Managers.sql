select
    employee.name as employee
from employee
join employee as manager
on employee.managerid = manager.id
where employee.salary > manager.salary;