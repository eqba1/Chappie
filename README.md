# Chappie: To Do List with Django and Ajax
My web project from the University of Kurdistan: Internet Engineering. 📋 Simple to-do list where you can add new tasks, or delete them if they are no longer important.


## Want to learn how to build this?

Check out the [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).

## Want to use this project?

> Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8800](http://localhost:8800). The "app" folder is mounted into the container and your code changes apply automatically.

> Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

## To-Do
- [] Better user interface for homepage
- [] Add done mark in UI after task done
- [] Add filter module 
- [] Add Search module
- [] Add user regestration
- [] Add Multi language Support

## Licence
GPLv3
