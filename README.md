# Online Library

A simple online platform for storing, browsing, reading, and managing PDF/EPUB books built with Django.

---

## Features

- User registration and authentication  
- Upload books in PDF or EPUB formats  
- Browse books with filters by author and genre  
- Download books  
- CRUD operations on books with object-level permissions (only the uploader can edit/delete)  
- Statistics stored in Redis (e.g., download counts)  
- PostgreSQL as the database backend  
- Dockerized environment with Redis and PostgreSQL  
- Code style checks with Black via GitHub Actions CI  

---

## Technologies

- Python 3.11  
- Django 5.2  
- PostgreSQL  
- Redis  
- Docker & Docker Compose  
- GitHub Actions  

---

## Setup and Installation

### Requirements

- Docker  
- Docker Compose  

### Clone the repository

```bash
git clone https://github.com/antshkvr/online-library.git
cd online-library
```

### Environment Variables

- Create a .env file in the root directory and add the following (adjust values as needed):
```bash
POSTGRES_DB=library_db
POSTGRES_USER=library_user
POSTGRES_PASSWORD=your_postgres_password

REDIS_HOST=redis
REDIS_PORT=6379

DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True
```

### Docker Compose

- Build and start the containers:
```bash
docker-compose up --build
```

### Database migrations

- In a separate terminal, create and run migrations:
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Usage
- Open http://localhost:8000/books/ to browse books

- Register an account or log in to add/edit/delete books

- Use filters on the book list page to filter by genre or author

- Upload new books via the "Add book" page

- Download books by clicking the download link on book detail pages

### Code style check
- The project uses **Black** for code formatting. The GitHub Actions workflow will check this automatically on push and pull requests. You can also run it locally:
```bash
docker-compose exec web black .
```