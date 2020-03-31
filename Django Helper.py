import os
import sys

base_html_format = """{% load static %}
<!DOCTYPE html>
<html lang='en'>
	<head>
		<meta charset='UTF-8'>
		<meta name='viewport' content='width=device-width, initial-scale=1'>
		<link rel='stylesheet' type='text/css' href="{% static 'css/bootstrap.min.css' %}">
		<title>{{title}}</title>
		<link rel="stylesheet" type='text/css' href="{% static 'css/user_styles.css' %}">
	</head>
	<body>
		<div class='container'>
		{% block content %}
			<!-- Code will be here -->
		{% endblock %}
		</div>
		<script src="{% static 'js/jquery.js' %}"></script>
		<script src="{% static 'js/bootstrap.min.js' %}"></script>
	</body>
</html>	
"""


index_html_format = """{% extends 'base.html' %}
 
 {% block content %}
 <p>This is default code</p>
 {% endblock %}
"""
urls_py_format = """from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('home', views.home, name='home'),
]

"""

views_py_format = """from django.shortcuts import render, redirect

def home(request):
	title = 'Home'
	template_name = 'index.html'
	return render(request, template_name, {'title':title})

#END
"""

#OPERATION FOR CREATING PROJECTS
project_name = input('Enter Django project name: ')
#making project creation command
command = 'django-admin startproject ' + project_name
try:
	os.system('cmd /c ' + command)
except:
	pass
#change to project directory
project_path = os.getcwd() + '\\' + project_name
os.chdir(project_path)
#then promp user for app name
app_name = input('Enter app name: ')
command = 'python manage.py startapp ' + app_name
try:
	os.system('cmd /c ' + command)
except:
	pass
#making a template folder
os.system('cmd /c "mkdir templates"')
template_path = project_path + '\\templates'
os.chdir(template_path)
#creating base.html file
file = open('base.html', 'w+')
file.write(base_html_format)
file.close()
#creating index.html file
file = open('index.html', 'w+')
file.write(index_html_format)
file.close()
#creating urls.py in application directory
app_path = project_path + '\\' + app_name
os.chdir(app_path)
file = open('urls.py', 'w+')
file.write(urls_py_format)
file.close()
file = open('views.py', 'w+')
file.write(views_py_format)
file.close()

#prompt user should it runserver or not
os.chdir(project_path)
run_server = False
user_proposal = input('Do you want to run the server?[Yes/No]\n= ')
if user_proposal == 'yes' or user_proposal == 'YES' or user_proposal == 'Yes':
	run_server = True
else:
	run_server = False
if run_server:
	command = 'python manage.py runserver'
	try:
		os.system('cmd /c ' + command)
	except:
		pass