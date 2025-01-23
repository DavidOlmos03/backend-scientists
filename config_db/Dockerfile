# Use the official postgres image
FROM postgres:15

# Initialize the database
COPY create.sql /docker-entrypoint-initdb.d/01_create.sql
COPY init.sql /docker-entrypoint-initdb.d/02_init.sql