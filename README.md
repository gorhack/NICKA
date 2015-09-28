# NICKA
##About:
*[CS401 Mini-Project Capstone]* Program to Register and maintain records of code words, nicknames, reconnaissance nicknames and exercise terms and controls their use within the GCCS-T. The System validates code word, nickname and exercise term usage with assigned agencies, assigned blocks, assigned prefixes and ensures nicknames and exercise terms are not duplicated. 

##Setup:

####Jango Setup

1. Install dependencies (`$pip install Django==1.8.4` (MySQL-Python==1.2.5, mysql-connector-python==2.0.4)
2. cd /django-NICKA
3. `$python manage.py runserver`

####Database

- [root]/[appname]/models.py
- ```
class Operation(models.Model):
	code_word = models.CharField(max_length=200)
	location = models.ForeignKey(Location)
	agency = models.ForeignKey(Agency)
	user = models.ForeignKey(User)
	op_num = models.IntegerField()
	clearance = models.CharField(max_length=30)
	def __str__(self):
		return self.code_word
```
- Exploring the shell:
	- `$python manage.py shell`
	- `>from codenames.models import * `
	
####Frontend
- [simple form](https://docs.djangoproject.com/en/1.8/intro/tutorial04/)
- [Styling](https://docs.djangoproject.com/en/1.8/intro/tutorial06/)

####Frontend using templates

- create .html template in [root]/templates/
- add template path to project in [project_name]/settings.py

- [url filtering](https://docs.djangoproject.com/en/1.8/intro/tutorial03/)


####Users

- [Admin](https://docs.djangoproject.com/en/1.8/intro/tutorial02/):
	- `$python manage.py createsuperuser`
 	- localhost:8000/admin/
	- codenames/admin.py
		- ```
		from django.contrib import admin
		from .models import Name
		class NameAdmin(admin.ModelAdmin):
			fields = ['nickname','date', ...]
		admin.site.register(Name, NameAdmin)
		```
- 

####Testing

- [Tests](https://docs.djangoproject.com/en/1.8/intro/tutorial05/)

####Jango project creation

- `$django-admin.py startproject NICKA`
- Edit NICKA/settings.py for database settings
- `$./manage.py migrate`
- `$python manage.py startapp codenames`
- create models for database in codenames/models.py
- add `codenames` to INSTALLED_APPS in NICKA/settings.py
- `$python manage.py makemigrations codenames`
	- run when making changes to models, run sqlmigrate to view sql
- `$python manage.py sqlmigrate codenames 0001`
	- creates the model tables in db 