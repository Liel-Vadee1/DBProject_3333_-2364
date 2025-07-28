# Database configuration
import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'DBProject_L'),
    'user': os.getenv('DB_USER', 'Lielv'),
    'password': os.getenv('DB_PASSWORD', 'lielvadee3055')
}


# Application configuration
APP_CONFIG = {
    'title': 'Maternity Ward Management System',
    'geometry': '1000x800',
    'bg_color': '#f0f8ff',
    'primary_color': '#4a90e2',
    'secondary_color': '#7bb3f0',
    'success_color': '#28a745',
    'error_color': '#dc3545',
    'warning_color': '#ffc107'
}