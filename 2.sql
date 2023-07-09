--Название и продолжительность самого длительного трека.
--Название треков, продолжительность которых не менее 3,5 минут.
--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
--Исполнители, чьё имя состоит из одного слова.
--Название треков, которые содержат слово «мой» или «my».
select title_track from track where track_duration = (select max(track_duration) from track);
select title_track from track where track_duration >= 3.5*60;
select name_of_collections from collections where year_of_release between '2018-01-01' and '2020-12-31';
select nickname from executors where nickname not like ('% %');
select title_track from track where string_to_array(lower(title_track), ' ') && ARRAY['my'];
