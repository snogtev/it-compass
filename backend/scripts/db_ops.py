import argparse

from app.database import create_db_and_tables
from scripts.data_normalization import create_salary_scores
from scripts.load_data import import_data

parser = argparse.ArgumentParser(description='Project database management utility')
subparsers = parser.add_subparsers(dest='command')

subparsers.add_parser('setup', help='Create database and load data')

args = parser.parse_args()

if args.command == 'setup':
    create_db_and_tables()
    import_data()
    create_salary_scores()