drop table if exists user;
create table user (
  id integer primary key autoincrement,
  login_name string not null,
  password string not null
);

insert into user (login_name,password) values ("admin","admin");

drop table if exists worker;
create table worker(
  worker_id integer primary key autoincrement,
  login_name char(20) UNIQUE not null,
  password char(50) not null,
  really_name char(20) not null,
  phone char(11) UNIQUE,
  job integer default 0,
  wage_card_number char(30) UNIQUE,
  worker_status integer default 0,
  is_deleted integer check(is_deleted in(0,1)) default 0,
  initiation_time date,
  departure_time date
);

drop table if exists job;
create table job(
	id integer primary key autoincrement,
	job_name char(10) not null,
	job_desc char(100)
);

insert into job (job_name) values('董事长');

drop table if exists worker_status;
create table worker_status(
	id integer primary key autoincrement,
	status_name char(10) not null,
	status_desc char(100)
);

insert into worker_status (status_name) values('在职');
insert into worker_status (status_name) values('离职');