create table albums(
					id SERIAL primary key,
					title VARCHAR(50) UNIQUE,
					year_of_release DATE check (year_of_release >= '1900-01-01'));

create table executors(
						id SERIAL primary key,
						nickname VARCHAR(30) UNIQUE);

CREATE TABLE album_executors (
    id SERIAL PRIMARY KEY,
    id_album INTEGER,
    id_executor INTEGER,
    FOREIGN KEY (id_album) REFERENCES albums (id) ON DELETE SET NULL,
    FOREIGN KEY (id_executor) REFERENCES executors (id) ON DELETE SET NULL
);

create table genre(
					id SERIAL primary key,
					name_of_genre VARCHAR(50) UNIQUE);

create table genre_executor(
							id SERIAL primary key,
							id_executor integer,
							id_genre integer,
							foreign key (id_executor) references executors (id) on delete set null,
							foreign key (id_genre) references genre (id) on delete set null);

create table track(
					id SERIAL primary key,
					title_track VARCHAR(50),
					track_duration integer,
					id_album integer,
					foreign key (id_album) references albums (id) on delete set null);

create table collections(
						id SERIAL primary key,
						name_of_collections VARCHAR(50),
						year_of_release DATE check (year_of_release >= '1900-01-01'));

create table cross_collections(
								id SERIAL primary key,
								id_track integer,
								id_collecton integer,
								foreign key (id_track) references track (id),
								foreign key (id_collecton) references collections (id));