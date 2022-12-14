### Canteen Automation System (CAS) - DBMS Project

<p align="center">
  <a href=""><img src="https://res.cloudinary.com/dpfpk49oa/image/upload/v1670989811/restaurant_rplypn.png" alt="Logo" height=200 width=200 /></a>
</p>

<p align="center">
The objective of this project is to develop a system that automates the process of ordering and managing food in a canteen. The system is built using the Django web framework and the Tailwind CSS framework for the frontend design. This will provide a convenient and efficient solution for both Admin and Canteen staff, allowing admin to easily place orders and track their status, and allowing canteen staff to manage the orders efficiently.
</p>
     
<p align="center">
<a href="https://cas.up.railway.app/">Live Project Link</a> 
 </p>
     
<p align="center">
<a href="https://www.python.org/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="g' title="Made with Python" />
     </p>
     
#### Tech used

<img src="https://www.svgrepo.com/show/353657/django-icon.svg" height="50px">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://www.svgrepo.com/show/374118/tailwind.svg" height="50px">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://www.svgrepo.com/show/354200/postgresql.svg" height="50px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://railway.app/brand/logo-light.svg" height="50px">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

#### Features

1. Staff registration and login
2. Menu management
3. Order management
4. Bill generation
5. Summary of Transactions

#### Schema Diagram

<img width="661" alt="Screenshot 2022-12-14 at 9 41 22 AM" src="https://user-images.githubusercontent.com/83623339/207504032-25d8788b-b57e-4c50-9e12-6ff6960eabce.png">

#### ER Diagram

<img width="638" alt="Screenshot 2022-12-14 at 9 41 38 AM" src="https://user-images.githubusercontent.com/83623339/207504061-3276dd05-7609-4dd4-8c0e-ad8f7f50244e.png">

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
DATABASE_URL=
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

#### Screenshots

1. Login Page
   ![image14](https://user-images.githubusercontent.com/83623339/207505386-de5c78c1-23b8-4dc9-bec3-70731a642d5d.jpg)

2. Adding Canteen Items
   ![image13](https://user-images.githubusercontent.com/83623339/207505403-3296ad48-ec45-4258-9f67-7bdce5f1ff54.jpg)
3. Registering Kitchen Staff
   ![image12](https://user-images.githubusercontent.com/83623339/207505427-b97e46ad-a0cc-408c-bc5b-326b8718c1e4.jpg)
4. Order Canteen Items
   ![image10](https://user-images.githubusercontent.com/83623339/207506466-16a38d49-0ffa-4766-9769-582fd7876e1f.jpg)

5. Home Page
   ![image9](https://user-images.githubusercontent.com/83623339/207506769-5cba2375-e2cb-47bc-9f21-0aab37806137.jpg)

6. View, Update, Delete Order items
   ![image7](https://user-images.githubusercontent.com/83623339/207506818-da1c1bdd-1227-444d-ad6d-638061223889.jpg)

7. View and Complete orders
   ![image6](https://user-images.githubusercontent.com/83623339/207506835-c67482b6-2dcf-412f-aaa0-f8b77b6b69ef.jpg)

8. Generated Bill Invoice
   ![image5](https://user-images.githubusercontent.com/83623339/207506873-db576c30-0f40-4921-8c0d-158ebddd66e3.png)

9. Summary
   ![image4](https://user-images.githubusercontent.com/83623339/207506917-ae7c8e96-b5a6-4aa4-9501-98990ed1c3ad.jpg)

10. Secure Billing workflow
    ![image2](https://user-images.githubusercontent.com/83623339/207506936-64a424e5-cdef-4372-874f-5f806986135f.jpg)

### Team Members

| <img src = "https://avatars.githubusercontent.com/u/83623339?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/91735807?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/120498628?v=4" width="50px"> |
| :-----------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
|              [Nagaraj Pandith](https://github.com/nagarajpandith/)              | [Nidheesha T](<https://github.com/NidheeshaT/](https://github.com/rudra246)>) |                 [Rudradeep Roy](https://github.com/KishorBalgi/)                 |

#### Attributions

- [Restaurant icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/restaurant)
- [Django + Postgres Deployment guide](https://devpress.csdn.net/postgresql/62f4d8b8c6770329307fa54e.html)
