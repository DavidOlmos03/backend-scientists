#!/bin/bash
set -e

echo "Esperando a que la base de datos esté lista..."
while ! pg_isready -h postgres_container -p 5432 -U ${DB_USER}; do
  sleep 1
done

echo "Base de datos lista, ejecutando tests..."
exec "$@"
