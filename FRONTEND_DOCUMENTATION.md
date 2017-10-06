## FRONTEND DOCUMENTATION

## FRAMEWORK
* Angular node JS

## WHAT THE SITE WILL LOOK LIKE
The following images are what our site is planned to look like.

![Login_page](/Users/student/Desktop/NYUAD Alumni Website Project/login.png)


![Search_page](/Users/student/Desktop/NYUAD Alumni Website Project/search.png)

![]


## RUNNING A COMMAND
* All commands should be run from within the container. There a two ways to do that:

1) If the container is already up and running, just `exec` into it:
`docker exec -it nyuadalumniwebsite_web_1 bash`, then you can run your command from the new shell.

2) If the container is not yet running you can use something like:
`docker-compose run web python manage.py test` to run the tests from within the container.

## CONTRIBUTION GUIDELINES
* Create a branch from the master and submit a pull request.

* Once the PR is reviewed it can be merged to master.
