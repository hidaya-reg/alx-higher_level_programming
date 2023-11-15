--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre, count(sg.show_id) AS number_of_shows 
FROM tv_genres g
RIGHT JOIN tv_show_genres sg
ON sg.genre_id = g.id 
GROUP BY sg.genre_id
ORDER BY 2 DESC;
