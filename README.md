# Social Network

## Installation:


- Install [docker-compose](https://docs.docker.com/compose/install/)
- Make sure if **port: 8000** is available on your machine.
- Run: `docker-compose up`.
- To apply migrations run `docker-compose exec -T web python manage.py migrate` 
- Finally, go to the url: [http://localhost:8000/api/](http://localhost:8000/api/)

To stop project, run: `docker-compose stop`