--Количество исполнителей в каждом жанре.
--Количество треков, вошедших в альбомы 2019–2020 годов.
--Средняя продолжительность треков по каждому альбому.
--Все исполнители, которые не выпустили альбомы в 2020 году.
--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
select name_of_genre, count(id_executor) from genre join genre_executor on genre.id = genre_executor.id_genre
group by name_of_genre;

select count(*) from albums join track on albums.id = track.id_album
where year_of_release between '2019-01-01' and '2020-12-31';

select title, round(avg(track_duration), 2) from albums join track on albums.id = track.id_album
group by title;

select nickname from executors
where nickname not in (select distinct nickname from album_executors al join albums a on a.id = al.id_album
				join track t on al.id_album = t.id_album
				join executors e on al.id_executor = e.id
where extract(year from year_of_release) = 2020);

select name_of_collections from collections join cross_collections on cross_collections.id_collecton = collections.id
					join track on cross_collections.id_track = track.id
					join album_executors on track.id_album = album_executors.id_album
					join executors on executors.id = album_executors.id_executor
where nickname in ('Скриптонит');
