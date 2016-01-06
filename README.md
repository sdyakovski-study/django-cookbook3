Following "Web Development with Django Cookbook" recepes.
I changed the project structure a bit compared to the one suggested in the book:
- Instead of creating the virtualenv in ., I created it in django-cookbook3-env:
   $ virtualenv django-cookbook3-env
   $ source django-cookbook3-env/bin/activate
- So instead of getting bin, include, lib etc. directly in the django-cookbook3 folder, I have in there an django-cookbook3-env folder, and these are inside
- I do not create a project/django_project/myproject
- instead I run 
   (django-cookbook3-env)$ django-admin.py startproject myproject 
  directly in the django-cookbook3 folder, which created in it myproject/myproject
- then mv myproject project
- now I have in django-cookbook3 a folder project which has myproject and manage.py. Added in here this README.md
