\c scientists_db;
CREATE TABLE IF NOT EXISTS scientists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    birthday DATE,
    description VARCHAR(255),
    area VARCHAR(50)
);
INSERT INTO scientists (name, birthday, description, area) 
VALUES 
('Marie Curie', '1867-11-07', 'Pioneer in radioactivity research', 'Physics'),
('Albert Einstein', '1879-03-14', 'Developed the theory of relativity', 'Physics')
ON CONFLICT DO NOTHING;
