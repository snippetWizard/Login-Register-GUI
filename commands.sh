#!/bin/bash

# Function to install required libraries
install_libraries() {
    python -m pip install alembic sqlalchemy
}

# Function to create migrations
create_migrations() {
    read -p "Enter a message for the migration: " migration_message
    alembic revision --autogenerate -m "$migration_message"
}

# Function to apply migrations
apply_migrations() {
    alembic upgrade head
}

# Function to display help
display_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -i, --install    Install required libraries"
    echo "  -c, --create     Create migrations"
    echo "  -a, --apply      Apply migrations"
    echo "  -h, --help       Display this help message"
    exit 0
}

# Main script
while [ "$#" -gt 0 ]; do
    case "$1" in
        -i|--install)
            install_libraries
            shift
            ;;
        -c|--create)
            create_migrations
            shift
            ;;
        -a|--apply)
            apply_migrations
            shift
            ;;
        -h|--help)
            display_help
            ;;
        *)
            echo "Unknown option: $1"
            display_help
            ;;
    esac
done
