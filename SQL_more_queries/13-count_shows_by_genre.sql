-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY COUNT(tv_show_genres.show_id) DESC;
