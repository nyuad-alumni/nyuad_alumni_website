# NYUAD ALUMNI WEBSITE



## SET UP
* Install Docker and Docker-Compose

## STARTING WITH GITHUB
If this is the first time you are using Github, you should set up your two-factor authentication. You can do this in the `settings > security` section of your Github account. You have to download a mobile app called Authy from the App Store. Everything will work without the 2FA but we strongly recommend you to do it.

You have to clone the git repository to have access to and be able to commit to the repository. To do this, go to the nyuad_alumni_website repository, and click the 'Clone or download' button at the top right. Copy the url to your clipboard. After you do this, go to your command line, and type `git clone (what you copied)`. Now, you should be set up with the repository on your local machine.

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
