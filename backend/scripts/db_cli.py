import argparse

from app.database import create_db_and_tables
from app.db_ops import clear_table, load_data
from scripts.data_normalization import create_salary_scores

parser = argparse.ArgumentParser(description='Project database management utility')
subparsers = parser.add_subparsers(dest='command')

subparsers.add_parser('setup', help='Create database and table and load data')
subparsers.add_parser('clear', help='Clear table data')
subparsers.add_parser('refresh', help='Refresh table data')

args = parser.parse_args()

if args.command == 'setup':
    create_db_and_tables()
    load_data()
    create_salary_scores()
elif args.command == 'clear':
    clear_table()
elif args.command == 'refresh':
    clear_table()
    load_data()
    create_salary_scores()