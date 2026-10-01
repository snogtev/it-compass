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

## 🗄️ Database commands

**Note:** All commands below must be run from `/backend` directory.

| Command | Description |
| ------- | ----------- |
| uv run python -m scripts.db_cli setup | Create database and table and load data |
| uv run python -m scripts.db_cli clear | Clear table data |
| uv run python -m scripts.db_cli refres | Refresh table data |

## 🗺️ Roadmap

- **Interactive Map:** A map of Russia featuring a color gradient (from red to green) and informational infoboxes triggered upon clicking a subjects.
- **Profile Selection:** Career level switching (`Applicant`, `Intern`, `Junior`, `Middle`, `Senior`) with dynamic metric weight recalculation tailored to specific priorities.
- **Top 10 Subjects:** A ranked list of the best subjects in the Russian Federation for the selected profile, showing position, name, and total score.
- **Subjects Comparison:** Detailed side-by-side comparison of two subjects with an automatically determined winner based on individual metrics.
- **Subjects Search:** A search input field with real-time highlighting of the selected subjects on the map.

## 🪪 License

Distributed under the MIT License. See `LICENSE.txt` for more information.