\c scientists_db;
CREATE TABLE IF NOT EXISTS scientists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    birthday DATE,
    description VARCHAR(255),
    area INT
);
INSERT INTO scientists (name, birthday, description, area) 
VALUES 
('Marie Curie', '1867-11-07', 'Pioneer in radioactivity research', 2),
('Albert Einstein', '1879-03-14', 'Developed the theory of relativity', 2)
ON CONFLICT DO NOTHING;


CREATE TABLE IF NOT EXISTS areas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25)
);
INSERT INTO areas (name)
VALUES
('Mathematics'),
('Physics'),
('Biology'),
('Astronomy'),
('Chemistry')
ON CONFLICT DO NOTHING;
