create table core.questions
(
	question_id int,
	title_slug varchar(500),
	difficulty varchar(25),
	question_json jsonb
);

create unique index questions_question_id_uindex
	on core.questions (question_id);

create unique index questions_questionid_uindex
	on core.questions (question_id);

alter table core.questions
	add constraint questions_pk
		primary key (question_id);


create table core.questions
(
	question_id int,
	title_slug varchar(500),
	difficulty varchar(25),
	question_json jsonb
);