--не менее 4 исполнителей,
--не менее 3 жанров,
--не менее 3 альбомов,
--не менее 6 треков,
--не менее 4 сборников.
insert into executors(nickname)
values('ATL'), ('Lenkin Park'), ('EMINEM'), ('Macan'), ('Скриптонит'), ('Три дня дождя'), ('Mnogoznaal');


insert into genre(name_of_genre)
values ('Rap'), ('Rock'), ('Pop');


insert into albums(title, year_of_release)
values ('Радио Апокалипсис', '2021-06-10'), ('Linkerbaan', '2017-10-01'), ('The Eminem Show', '2002-02-02'), ('За всех', '2022-06-09'),
		('Праздник на улице 36', '2017-01-01'), ('Не киряй', '2022-04-03'), ('Гостиница "Космос"', '2018-08-23');

--Треки добавлял вручную, чтобы не искать id
insert into track(title_track, track_duration, id_album)
select 'Разрушитель', 78, id
from albums
where title in ('Радио Апокалипсис');


insert into collections(name_of_collections, year_of_release)
values('Relax', '2023-01-01'), ('Hard rock', '2022-03-09'), ('Training', '2020-10-23'), ('Try again', now());


insert into album_executors(id_album, id_executor)
values((select id from albums where title in ('Радио Апокалипсис')), (select id from executors where nickname in ('ATL'))),
	((select id from albums where title in ('Linkerbaan')), (select id from executors where nickname in ('Lenkin Park'))),
	((select id from albums where title in ('The Eminem Show')), (select id from executors where nickname in ('EMINEM'))),
	((select id from albums where title in ('За всех')), (select id from executors where nickname in ('Macan'))),
	((select id from albums where title in ('Праздник на улице 36')), (select id from executors where nickname in ('Скриптонит'))),
	((select id from albums where title in ('Не киряй')), (select id from executors where nickname in ('Три дня дождя'))),
	((select id from albums where title in ('Гостиница "Космос"')), (select id from executors where nickname in ('Mnogoznaal')));


insert into genre_executor(id_executor, id_genre)
values((select id from executors where nickname in ('ATL')), (select id from genre where name_of_genre in ('Rap'))),
		((select id from executors where nickname in ('Lenkin Park')), (select id from genre where name_of_genre in ('Rock'))),
		((select id from executors where nickname in ('EMINEM')), (select id from genre where name_of_genre in ('Rap'))),
		((select id from executors where nickname in ('Macan')), (select id from genre where name_of_genre in ('Pop'))),
		((select id from executors where nickname in ('Скриптонит')), (select id from genre where name_of_genre in ('Rap'))),
		((select id from executors where nickname in ('Три дня дождя')), (select id from genre where name_of_genre in ('Pop'))),
		((select id from executors where nickname in ('Mnogoznaal')), (select id from genre where name_of_genre in ('Rap')));


insert into cross_collections(id_track, id_collecton)
values(1,1), (8,1), (12,1), (10, 2), (11, 2), (1, 3), (2, 3),
	(5,3), (8,3), (4,4), (13, 4), (11,4), (2,4);
