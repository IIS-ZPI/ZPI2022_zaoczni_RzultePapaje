create table tabela_A(
id serial,
"No" varchar(20) not null,
"Effective Date" date not null,
"Country" varchar(20),
"Code" varchar(5) not null,
"Mid" numeric(10,6) not null,
unique ("Effective Date","Country","Code")
);

create table tabela_B(
id serial,
"No" varchar(20) not null,
"Effective Date" date not null,
"Country" varchar(40),
"Code" varchar(5) not null,
"Mid" numeric(10,6) not null,
unique("Effective Date","Country","Code")
);

create table tabela_C(
id serial,
"No" varchar(20) not null,
"Trading Date" date not null,
"Effective Date" date not null,
"Country" varchar(40),
"Code" varchar(5) not null,
"Bid" numeric(10,6) not null,
"Ask" numeric(10,6) not null,
unique("Effective Date","Country","Code")
);



create index code_index_a on tabela_a("Effective Date","Code");
create index code_index_b on tabela_b("Effective Date","Code");
create index code_index_c on tabela_c("Effective Date","Code");