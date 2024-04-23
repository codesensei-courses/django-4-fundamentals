# Django Fundamentals
Demo code for the course "Django Fundamentals" on [Pluralsight](https://www.pluralsight.com).

There's a commit for each module in the course, as well as a tag:


- [After Module 2: Starting a Django Project](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/project-start)
- [After Module 3: Creating a Simple Web Page](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/m3-create-a-simple-page)
- [After Module 4: Setting Up a Data Model](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/m4-data-model;m4-data-model)
- [After Module 5: Combining Model, View and Template](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/m5-mtv)
- [After Module 6: URLs and Link Building](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/m6-urls)
- [After Module 7: Templates, Styling and Static Content](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/m7-templates-styling)
- [After Module 8: Adding User Interaction with ModelForms](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/m8-forms)
- [After Module 9: Editing Meetings and Authentication](https://github.com/codesensei-courses/django-4-fundamentals/releases/tag/m9-authentication)
# Setup instructions

## 1. Clone this repository

Check out any specific commit you like.

## 2. Create and activate a virtual environment

How to do this depends on your system; depending on your IDE this may not be necessary.

If you don't know how to do this: see my course [Development Environments and Package Management in Python 3](https://www.pluralsight.com/courses/python-3-development-environments-package-management)

## 3. Install dependencies

Inside the project, run `python -m pip install -r requirements.txt`.

## 4. Move into the meeting_planner folder

You want to be in the folder where the file `manage.py` is.

To get there, You probably need to run `cd meeting_planner`.

But watch out: there are two of those and you want to be in the
*outer* meeting_planner folder. If you end up 1 level too deep, run
`cd ..` to move up 1 level.

## 5. Run the project

The command for this is `python manage.py runserver`.

You can now view the project at http://localhost:8000

If this does not work, you are probably not in the correct folder.

# 6. Admin password

The username/password for the admin interface is:
user: test
password: test

Or you can of course create your own using the command `python manage.py createsuperuser`.

