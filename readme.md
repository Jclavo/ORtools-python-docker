Template to run OR-Tools + python 3.8 in a docker container

Steps:

- clone the repository
- docker-compose build
- docker-compose up -d
- docker exec -it my-ortools-python-3.8 /bin/bash (it will open a container terminal)
- python code/LO/google_sample.py (inside container terminal)

create more files and run them.

Happy coding!!