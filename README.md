# NICKA
##About:
*[CS401 Mini-Project Capstone]* Program to Register and maintain records of code words, nicknames, reconnaissance nicknames and exercise terms and controls their use within the GCCS-T. The System validates code word, nickname and exercise term usage with assigned agencies, assigned blocks, assigned prefixes and ensures nicknames and exercise terms are not duplicated. 

##Setup:

####Jango 1.8.4 Setup

1. Install dependencies (`$pip install Django==1.8.4` (MySQL-Python==1.2.5, mysql-connector-python==2.0.4)
2. cd /django-NICKA
3. `$python manage.py runserver`

####Database

- [root]/[app]/models.py
```
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
- [Simple form](https://docs.djangoproject.com/en/1.8/intro/tutorial04/)
- [Styling](https://docs.djangoproject.com/en/1.8/intro/tutorial06/)

####Frontend using templates

- admin template belongs in [project]/templates/admin/
- each app template belongs in [project]/[app]/templates/
- create .html file in template folder or use from "/usr/local/lib/python2.7/site-packages/django/contrib/admin/templates/"
- add template path to project in [project]/settings.py
```
TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
        ],},},]
```

####URLs
- [url filtering](https://docs.djangoproject.com/en/1.8/intro/tutorial03/)
- adding views to [app]/views.py
	```
	from django.http import HttpResponse
	def index_page(request):
    	return HttpResponse("Hello, world")
	```
- create [app]/urls.py
	```
		from django.conf.urls import url
		from . import views

		urlpatterns = [
			url(r'^$', views.index, name='index_page'),
		]
	```
- edit [project]/urls.py
	```
	from django.conf.urls import include, url
	from django.contrib import admin

	urlpatterns = [
	    url(r'^[app]/', include('[app].urls')),
	    url(r'^admin/', include(admin.site.urls)),
	]
	```
- now when visiting [host]:8000/[app] will display "Hello, world" from the index page in views.py

####Users

- [Admin](https://docs.djangoproject.com/en/1.8/intro/tutorial02/):
	- `$python manage.py createsuperuser`
 	- localhost:8000/admin/
	- codenames/admin.py
	```
		from django.contrib import admin
		from .models import Name
		class NameAdmin(admin.ModelAdmin):
			fields = ['nickname','date', ...]
		admin.site.register(Name, NameAdmin)
	```

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
