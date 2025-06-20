-- List all genres not linked to the show `Dexter` in the database `hbtn_0d_tvshows`.
SELECT tv_genres.name FROM tv_genres
WHERE NOT EXISTS
(
	SELECT 1 FROM tv_show_genres
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_show_genres.genre_id = tv_genres.id
	AND tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
