## NYUAD ALUMNI WEBSITE

## SET UP
* Install Docker and Docker-Compose

## RUN THE PROJECT
* From the project root run	`docker-compose up` and the site will be up and running on `http://localhost:8000/`

## RUNNING A COMMAND
* All commands should be run from within the container. There a two ways to do that:

1) If the container is already up and running, just `exec` into it:
`docker exec -it nyuadalumniwebsite_web_1 bash`, then you can run your command from the new shell. 

2) If the container is not yet running you can use something like:
`docker-compose run web python manage.py test` to run the tests from within the container.

## CONTRIBUTION GUIDELINES
* Create a branch from the master and submit a pull request.

* Once the PR is reviewed it can be merged to master.