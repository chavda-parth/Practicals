create database Student_Info_113
use Student_Info_113

create table Student (
	StuId int,
	Name varchar(100),
	EnrollmentNo varchar(12),
	Division varchar(50),
	Sem int,
	BirthDate datetime,
	Email varchar(100),
	ContactNo varchar(50)
)

insert into Student values
(101, 'Naimish Patel', '090200107051', 'BCX-3', 3, '1992-12-06', 'naimishp49@gmail.com', '8866205253'),
(102, 'Firoz A. S.', '090200107090', 'BCY-3', 3, '1994-05-03', 'Firoz.me@gmail.com', '8885999922'),
(103, 'Krunal Vyas', '090243107101', 'BCZ-5', 5, '1984-03-01', 'Krunal.vyas@gmail.com', '9990888877'),
(104, 'Vijay Patel', '090200107102', 'BCX-5', 5, '1985-02-15', 'Vijay.patel123@gmail.com', '8787878787'),
(105, 'Vimal Trivedi', '090200107103', 'BCY-3', 3, '1988-01-20', 'Maulik123@gmail.com', '8789564512');

select * from Student

--1

select Name from Student where Sem = 3 or Sem = 5

select Name from Student where Sem in (3,5)

--2

select Name, EnrollmentNo from Student where StuId between 103 and 105

--3

select Name, EnrollmentNo, Email from Student where Sem = 5

--4

select top 3 * from Student

--5

select top 30 percent Name, EnrollmentNo from Student where ContactNo like '%7'

--6

select distinct Sem from Student

--7

select * from Student where EnrollmentNo is null

--8

select * from Student where Name not like 'V%'

--9

select * from Student where EmailAddress like '%3@G%' and len(EmailAddress) = 6

--10

select * from Student where Name like 'F_r%'

--11

select * from Student where ContactNo like '%877%'

--12

select Name from Student where Sem = 3 and ContactNo not like '%8%9%'

--13

select * from Student where BirthDate > '1990-01-01'

--14

Update Student
	set Division = 'BCX-5',
		Sem = 5
	where StuId = 102

--15

Update Student
	set Name = 'Firoz Sherasiya'
	where Email = 'Firoz.me@gmail.com' and ContactNo = '8885999922'

--16

alter table Student add City varchar(50)

--17

delete from Student where Division = 'BCX-3'

--18

sp_rename 'Student.Email', 'EmailAddress', 'column'

--19

truncate table Student

--20

select * into Student_New from Student

select * from Student_New