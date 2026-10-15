<div align='center'>
<img src='logo.svg' alt='IT Compass Logo' width='300'>
</div>

# 🧭 IT Compass

**IT Compass** is a web application designed to calculate ratings of Russian subjects for IT specialists, tailored to their qualification levels and based on objective metrics.

🚧 **Status:** Under active development.

## 🛠️ Tech Stack

### Backend

![Python](https://img.shields.io/badge/language-python-%233670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/framework-fastapi-%23009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/database-sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLModel](https://img.shields.io/badge/orm_%26_validation-sql_model-7e56c2?style=for-the-badge)
![Pandas](https://img.shields.io/badge/data_engineering-Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/data_processing-scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![uv](https://img.shields.io/badge/PACKAGE_MANAGER-uv-%23DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white)

### Frontend

![JavaScript](https://img.shields.io/badge/language-javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/markup-html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/styling-css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white)

## 📊 Data sources

1. **Names of subjects**: Constitution of the Russian Federation, Article 65.
2. **Names of federal districts and their composition**: Decree of the President of the Russian Federation No. 849 of May 13, 2000 "On the Plenipotentiary Representative of the President of the Russian Federation in a Federal District".
3. **IT specialist salaries:** [IT Specialist Salaries across all IT specializations — Habr Career](https://career.habr.com/salaries)

## 🗄️ Database commands

> All commands below must be run from `/backend` directory.

> If you don't have `uv` installed, follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

| Command | Description |
| ------- | ----------- |
| `uv run python -m scripts.db_cli setup` | Create database and table and load data |
| `uv run python -m scripts.db_cli clear` | Clear table data |
| `uv run python -m scripts.db_cli refresh` | Refresh table data |

## 🔌 API Endpoints

Once the backend is running, the interactive Swagger documentation is available at `http://localhost:8000/docs`.

| Method | Endpoint | Description | Query Parameters | Validation & Constraints |
| :----- | :------- | :---------- | :--------------- | :----------------------- |
| `GET` | `/subjects` | Returns a list of subjects filtered by federal district or specific subject, or all subjects of Russia. | • `grade` (Grade, **required**)<br>• `district` (District, optional)<br>• `subject` (Subject, optional) | **Simultaneous filtering is blocked.** Providing both `district` and `subject` at the same time will trigger a validation error. |
| `GET` | `/subjects/compare` | Returns metrics for two specific subjects side-by-side for comparison. | • `grade` (Grade, **required**)<br>• `first_subject` (Subject, **required**)<br>• `second_subject` (Subject, **required**) | **Comparing a subject to itself is blocked.** `first_subject` and `second_subject` must be distinct, otherwise a validation error is thrown. |



## 🗺️ Roadmap

### Backend

- [ ] Define the subject domain
- [ ] Design the database schema
- [ ] Devise the rating calculation methodology
- [ ] Connect SQLite as the storage layer
- [ ] Set up ORM and validation via SQLModel
- [ ] Write a CLI script for database management (`setup`, `clear`, `refresh`)
- [ ] Implement the `/subjects` endpoint with filtering by district and subject
- [ ] Implement the `/subjects/{subject_slug}` endpoint
- [ ] Implement the `/subjects/compare` endpoint for comparing two subjects
- [ ] Implement the `/subjects/rating` endpoint

### Frontend

- [x] Implement interactive map of Russia
- [x] Add a red-to-green color gradient reflecting each subject's score
- [x] Add hover tooltips and click-triggered infoboxes with subject details
- [x] Add zoom and pan with map boundaries
- [ ] Implement career level switching (`Applicant`, `Intern`, `Junior`, `Middle`, `Senior`) with map recoloring
- [ ] Implement the Top 10 subjects list for the selected career level
- [ ] Connect the frontend to the backend (`/subjects/rating`) instead of static data
- [ ] Implement subjects comparison with the winner determined by metrics
- [ ] Implement subjects search with real-time highlighting on the map
- [ ] Add a color legend and "No data" state for subjects without metrics
- [ ] Add loading and error states for data fetching
- [ ] Make the layout responsive for tablets and mobile devices


## 🪪 License

Distributed under the MIT License. See `LICENSE.txt` for more information.
