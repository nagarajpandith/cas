### CAS - DBMS Project

#### Local setup

- Create virtualenv

```bash
  python -m venv env
  env\Scripts\activate
```

- Install all the requirements

```bash
  pip install -r requirements.txt
```

- Install django-tailwind

```bash
python -m pip install django-tailwind
```

- Start a postgres database called 'cas' on default port (5432)
- Create `.env` in root folder and add the following

```env
SECRET_KEY=
DB_PASSWORD=
DB_USER=
```

- Make migrations

```bash
    python manage.py makemigrations
    python manage.py migrate
```

- Create a super user.

```bash
    python manage.py createsuperuser
```

- Running server

```bash
python manage.py runserver
python manage.py tailwind start
```

#### Development Notes

- Modify npm bin path (only if you're using Windows). Currently it is set to `NPM_BIN_PATH = '/usr/local/bin/npm'` for Mac & Linux based systems. If you're using Windows, you need to change it to `NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"` in settings.py of cas project. Do not stage settings.py while pushing to repo.

- If you add install any package during development, add it to requirements.txt by

```bash
pip freeze > requirements.txt
```

- Develop on a different branch (like 'feat/home-page', 'fix/overflow-issue' for different features/bug fixes and make PR to main or a single branch for all development purposes called 'develop' and make PRs to main from there

#### Attributions

[Restaurant icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/restaurant)
