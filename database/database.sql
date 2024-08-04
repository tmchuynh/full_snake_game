SELECT * FROM high_score;

SELECT * FROM user;

INSERT INTO user (username)
VALUES ("Michael"), ("Janet"), ("Natasha");

INSERT INTO high_score (high_score, difficulty, obstacles, obstaclesMove, peacefulMode, user_id)
VALUES (13, "hard", 14, 1, 1, 1),
(24, "medium", 7, 0, 1, 2),
(18, "easy", 4, 0, 0, 3),
(18, "medium", 8, 1, 0, 1),
(13, "Hard", 28, 1, 1, 2),
(38, "easy", 2, 1, 0, 2);

INSERT INTO high_score (high_score, difficulty, obstacles, obstaclesMove, peacefulMode, user_id)
VALUES (43, "easy", 4, 0, 1, 3);

SELECT high_score.*, user.username FROM high_score 
        LEFT JOIN user ON user.id = high_score.user_id
        ORDER BY user.username ASC, high_score.high_score DESC, user.username ASC;