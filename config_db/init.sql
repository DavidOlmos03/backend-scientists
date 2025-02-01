\c scientists_db;
CREATE TABLE IF NOT EXISTS areas (
    id INT PRIMARY KEY,
    name VARCHAR(25) UNIQUE
);
INSERT INTO areas (id, name)
VALUES
(1, 'Mathematics'),
(2, 'Physics'),
(3, 'Biology'),
(4, 'Astronomy'),
(5, 'Chemistry'),
(6, 'Engineering')
ON CONFLICT DO NOTHING;


CREATE TABLE IF NOT EXISTS scientists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    birthday DATE,
    description VARCHAR(255),
    area INT,
    CONSTRAINT FK_areas FOREIGN KEY (area) REFERENCES areas(id)
);
INSERT INTO scientists (name, birthday, description, area) 
VALUES 
('Marie Curie', '1867-11-07', 'Pioneer in radioactivity research', 2),
('Albert Einstein', '1879-03-14', 'Developed the theory of relativity', 2),
('Charles Darwin', '1809-02-12', 'Proposed the theory of evolution by natural selection', 3),
('Nikola Tesla', '1856-07-10', 'Contributions to the design of modern AC electricity supply systems', 6),
('Ada Lovelace', '1815-12-10', 'First computer programmer', 6),
('Galileo Galilei', '1564-02-15', 'Father of modern observational astronomy', 4),
('Stephen Hawking', '1942-01-08', 'Theoretical physicist known for black hole radiation', 2),
('Rosalind Franklin', '1920-07-25', 'Contributions to the understanding of DNA structure', 3),
('Alan Turing', '1912-06-23', 'Father of theoretical computer science and artificial intelligence', 6)
ON CONFLICT DO NOTHING;


