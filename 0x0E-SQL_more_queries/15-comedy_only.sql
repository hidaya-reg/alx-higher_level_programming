-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres sg
ON s.id = sg.show_id
LEFT JOIN tv_genres g
ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY 1 ASC;
