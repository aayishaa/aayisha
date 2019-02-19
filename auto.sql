Create database office;
use office;
create table Employee(ID int AUTO_INCREMENT,NAME varchar(20),AGE int,primary key(ID));
insert into Employee(NAME,AGE)values('aayisha',18);
insert into Employee(NAME,AGE)values('fahima',18);
insert into Employee(NAME,AGE)values('fahira',18);
insert into Employee(NAME,AGE)values('afroze',18);
select*from Employee;
