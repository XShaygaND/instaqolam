# Instaqolam
[![GitHub](https://img.shields.io/github/license/XShaygaND/instaqolam)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![GitHub last commit](https://img.shields.io/github/last-commit/XShaygaND/instaqolam)](https://github.com/XShaygaND/instaqolam)
[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/XShaygaND/instaqolam)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.1-green)](https://djangoproject.com)

Instaqolam is a weblog in which you have the ability to view, create, edit and delete posts and you also have the ability to like and comment on posts.

##
This project is my first project and many features are yet to be added, But further development is paused for now Since I need to work on other important projects.

## Running the project
Install required packages

	pip install -r requirements.txt

Clone project to your computer

	git clone https://github.com/XShaygaND/instaqolam.git

Create migrations

	python manage.py makemigrations members posts

Migrate project

	python manage.py migrate
		
Run the server on your localhost

	python manage.py runserver