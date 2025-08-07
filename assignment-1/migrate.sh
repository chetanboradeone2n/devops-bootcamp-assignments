#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found"
    exit 1
fi

# Load environment variables
export $(cat .env)

# Debug output
echo "DB_HOST: $DB_HOST"
echo "DB_USER: $DB_USER"
echo "DB_NAME: $DB_NAME"

# Check if required variables are set
if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_NAME" ] || [ -z "$DB_PASSWORD" ]; then
    echo "Error: Environment variables DB_HOST, DB_USER, DB_NAME, and DB_PASSWORD must be set"
    exit 1
fi

# Create database if it doesn't exist
echo "Creating database if it doesn't exist..."
psql -h "$DB_HOST" -U "$DB_USER" -d postgres -c "CREATE DATABASE $DB_NAME;" 2>/dev/null || echo "Database $DB_NAME already exists"

# Apply migration
echo "Applying migration to create students table..."
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -f migrations/001_create_students_table.sql || { echo "Migration failed"; exit 1; }

echo "Migration completed successfully."
