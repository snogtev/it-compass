<div align='center'>
<img src='logo.svg' alt='IT Compass Logo' width='300'>
</div>

# 🧭 IT Compass

**IT Compass** is a web application designed to calculate ratings of Russian subjects for IT specialists, tailored to their qualification levels and based on objective metrics.

🚧 **Status:** Under active development.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23D71F00.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 📚 Documentation

> Note: All documentation files are written in **Russian**.

* [Project Specification](docs/spec.md)
* [Scoring Methodology](docs/scoring-methodology.md)
* [Glossary](docs/GLOSSARY.md)

## 🗺️ Roadmap

* [x] Define and analyze subject domain
* [x] Design database schema
* [x] Devise scoring methodology
* [x] Set up PostgreSQL via Docker Compose
* [x] Implement database models and constraints with SQLAlchemy
* [ ] Configure database migrations with Alembic
* [ ] Seed reference tables (regions, metrics, grades, and weights)
* [ ] Write a CLI script for database management (`setup`, `clear`, `refresh`)
* [ ] Implement the `/subjects` endpoint with filtering by district and subject
* [ ] Implement the `/subjects/{subject_slug}` endpoint
* [ ] Implement the `/subjects/compare` endpoint for comparing two subjects
* [ ] Implement the `/subjects/rating` endpoint

## 🪪 License

Distributed under the MIT License. See `LICENSE.txt` for more information.
