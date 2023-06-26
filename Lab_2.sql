create database Employee_Info_113
use Employee_Info_113

--1

select * from Employee where EName like 'm__h%'

--2

select power(3,5) as 'output'

--3

select getdate() - 20

--4

select EName from Employee where EName like 'j%n%'

--5

select substring('SQL Programming', 2, 8)

--6

select EName from Employee where City like '___ney'

--7

select convert(varchar(50), 15)

--8

alter table Employee add Department varchar(20)

--9

Update Employee 
	set Department = 'Marketing'
	where City = 'London'

--10

select * from Employee where EName like '%n' or EName like '%y'

--11

select ceiling(63.1), (63.8), (-63.2)

--12

select * from Employee where JoiningDate is null

--13

select UPPER(EName), lower(City) from Employee

--14

alter table Employee
alter column Ename char(30)