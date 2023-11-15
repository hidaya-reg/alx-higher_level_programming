--  list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE name
NOT IN (SELECT g.name
	FROM tv_genres g
	RIGHT JOIN tv_show_genres sg
	ON g.id = sg.genre_id
	RIGHT JOIN tv_shows s
	ON sg.show_id = s.id
	WHERE s.title = 'Dexter')
ORDER BY 1 ASC;
