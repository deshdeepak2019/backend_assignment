# Animal Details

Animal Data CRUD API documentation! This set of APIs allows you to perform basic CRUD operations on animal data, including storing, retrieving, modifying, and deleting information such as name, type (Herbivore or Carnivore), sound, and additional details.

## Installation :

- If pip is not in your system
  ```
  $ sudo apt-get install python-pip
  ```
- Then install virtualenv
  ```
  $ pip install virtualenv
  ```
- Create Virtual Environment
  ```
  python3 -m venv .venv
  ```
- Activate venv
  ```
    source .venv/bin/activate
  ```

1. Clone the repository and proceed to the directory containing the manage.py file.

```
git clone https://github.com/deshdeepak2019/backend_assignment/
```

```
cd backend_assignment
```

2. Install the requirements

```
pip install -r requirements.txt
```

3. Run the development server

```
python manage.py runserver
```

4. Open this URL to view all APIs

```
http://127.0.0.1:8000/
```

5. Open admin dashboard-
     a. Create a new superuser
         ```
         python3 manage.py createsuperuser
         ```
    b. Open this URL to view admin dashboard
       ```
        http://127.0.0.1:8000/admin/
       ```

## NOTE:-

1. I am using SWAGGER UI for visualize and interact with the API's resources

    <img width="957" alt="Screenshot 2024-01-06 195502" src="https://github.com/deshdeepak2019/backend_assignment/assets/97728256/0c0633d2-a9ec-4bda-be29-6c796c5dfcce">

    

2. Using DRF for viewsets and REST API.
3. Default SQLite DB is used.
4. Token Based Authentication is used.
5. Only Super Users can delete data.

## APIs:-

# Accounts API - LOGIN, LOGOUT, REGISTER
1. Login - http://127.0.0.1:8000/accounts/login/
2. Logout- http://127.0.0.1:8000/accounts/logout/
3. Register- http://127.0.0.1:8000/accounts/register/

# Animal API- GET, POST, PUT, PATCH, DELETE

1. http://127.0.0.1:8000/animal/  - Get all animals,POST new animal.
2. http://127.0.0.1:8000/animal/id/ -  Get Delete and Modify single instance
   
