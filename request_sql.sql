create table albums(
					id SERIAL primary key,
					title VARCHAR(50),
					year_of_release DATE);
create table executors(
						id SERIAL primary key,
						nickname VARCHAR(50));
create table album_executors(
							id SERIAL primary key,
							foreign key (id_album) references albums (id) on delete set null,
							foreign key (id_executor) references executors (id) on delete set null);
create table genre(
					id SERIAL primary key,
					name_of_genre VARCHAR(50));
create table genre_executor(
							id SERIAL primary key,
							foreign key (id_executor) references executors (id) on delete set null,
							foreign key (id_genre) references genre (id) on delete set null);
create table track(
					id SERIAL primary key,
					title_track VARCHAR(50),
					track_duration time,
					foreign key (id_album) references albums (id) on delete set null);
create table collections(
						id SERIAL primary key,
						name_of_collections VARCHAR(50),
						year_of_release DATE);
create table cross_collections(
								id SERIAL primary key,
								foreign key (id_track) references track (id),
								foreign key (id_collecton) references collections (id);