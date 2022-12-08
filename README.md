### CAS - DBMS Project

#### Project Checklist

##### High Priority

- [x] login page -> verify if owner or kitchen staff
- [ ] if owner -> 3 interfaces
  - [x] add kitchen staff
  - [ ] add canteen items
  - [x] order items
  - [ ] generate bill
- [ ] if staff -> an interface listing all current orders and ability to tick them off
- [ ] frontend for all the above
- [ ] documentation/project report (synopsis, screenshots, er diagram, schema etc.)
- [ ] hosting

##### Low Priority

- [ ] handling cases with empty items
- [ ] summary and stats of orders for owner

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

- Start a postgres database called 'cas' on default port (5432)
- Create `secrets.json` inside cas/ folder

```json
{
  "SECRET_KEY": "",
  "DB_PASSWORD": "",
  "DB_USER": ""
}
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

- If you add install any package during development, add it to requirements.txt by

```bash
pip freeze > requirements.txt
```

- Develop on a different branch (like 'feat/home-page', 'fix/overflow-issue' for different features/bug fixes and make PR to main or a single branch for all development purposes called 'develop' and make PRs to main from there
