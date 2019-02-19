# Item Catalog

Project Item Catalog - Udacity Full Stack Nanodegree course
A Restaurant Menu app was built, where users can add, edit, and delete restaurants and menu items in the restaurants.

### Project Overview
> To Develop an application that provides a list of restaurants within a variety of menus as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own restaurants and menus and implements a JSON endpoint that serves the same information as displayed in the HTML endpoints for an arbitrary menu in the restaurant.

### Why This Project?
> Modern web applications perform a variety of functions and provide amazing features and utilities to their users; but deep down, it’s really all just creating, reading, updating and deleting data. In this project, you’ll combine your knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to your users.

### What Will I Learn?
  * Develop a RESTful web application using the Python framework Flask.
  * Implementing third-party OAuth authentication.
  * Implementing CRUD (create, read, update and delete) operations.
  
### How to Run?

#### PreRequisites
  * [Python ~2.7](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  
#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Find the Item_Catalog zip file.
  3. Extract the zip file and place Item_Catalog folder in your Vagrant directory.

#### Launch Project
  1. Launch the Vagrant VM using command:

  ```
  $ Vagrant up 
  ```

  2. Run Vagrant

  ```
  $ Vagrant ssh
  ```

  3. Change directory to `/vagrant/Item_Catalog/`

  ```
  $ cd /vagrant/Item_Catalog
  ```

  4. Initialize the database

  ```
  $ python database_setup.py
  ```

  5. Populate the database with some initial data

  ```
  $ Python menus.py
  ```

  6. Launch application

  ```
  $ Python project.py
  ```# catalog
