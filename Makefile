# Setup for the project
# setup_project:
# 	pip install virtualenv
# 	mkdir -p ~/.environtments
# 	virtualenv -p python3 ~/.environtments/django-py3

# setup_environment:
# 	source ~/.environtments/django-py3/usr/local/bin/activate
# 	pip install -r requirements.txt

run_server:
	python manage.py runserver

load_init_data:
	python manage.py migrate
	python manage.py init_menu_permission
	python manage.py init_user_permission

run_demo:
	make load_init_data
	make run_server

run_ut:
	coverage erase
	coverage run manage.py test
	coverage report

