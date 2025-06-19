<<<<<<< HEAD
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2KNg-QOU)
# Django_View-Templates

## install requirement project's packages

```commandline
pip install -r requirements.txt
```

## Run project

Go to the folder with manage.py file, run library
```commandline
python manage.py migrate 
```

```commandline
python manage.py runserver
```

## Run tests

There are no tests.

Everything is at your discretion and the feeling of beauty :)

**_As a result of this sprint ( except fot the code in  repository) you should have a short video (2-10min) that shows functionality of the app._**

## Tasks

Create the appropriate views and templates for:

**Do not use django forms, use only HTML forms!**

(if necessary, you can modify the models)

auth
* Provide the ability to register the user as a librarian or as an ordinary user (guest)
* Provide the ability to log in (guest)
* Provide the ability to Log out (authorized user)

books  (admin/user)

* show information about all books (admin/user)
* provide an opportunity to view a specific book (admin/user);
* provide the ability to filter books by various criteria (author, title, etc.) (admin/user);
* show all books provided to a specific user (by id) (admin);

users  (admin)

* show information about all users (admin/user)
* provide an opportunity to view a specific user (admin/user)

orders  (admin)

* show information about all orders (admin)
* show information about all my orders (user)
* provide an opportunity to create an order (user)
* provide an opportunity to close the order  (admin)

authors  (admin)

* show information about all authors (admin)
* provide an opportunity to create a new author  (admin)
* provide the ability to remove the author if he is not attached to any book (admin)
=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZzvGImr-)

Сopy the project from the previous sprint.

Create an admin panel for your projects.

In the admin panel:

* create a user with administrator rights
* create an additional user
* register all models listed in the models.py file
* configure the display of lists by adding additional model fields
* add list filters to make it easier to find information by book id, book title, book author
* create a layout with a detailed presentation for books and authors
* form a visual distribution of information about books so that there is a separate section with data that do not
  change (title, author, year of publication) and that change (date of issue of the book)

As a result of this sprint (except for the code in the repository) you should get a short video (2-10 minutes) showing
the functionality of the program.
>>>>>>> origin/main
