create table core.prices
(
	price_id serial,
	symbol varchar(10) not null,
	exchange varchar(50) not null,
	price_time timestamp,
	price_json jsonb
);

create unique index prices_price_id_uindex
	on core.prices (price_id);

alter table core.prices
	add constraint prices_pk
		primary key (price_id);

alter table core.prices
	add to_symbol varchar(10);

alter table core.prices
	add price_value numeric(16,8);