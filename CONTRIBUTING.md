# Contributing to this project

Welcome to Pluto! We appreciate and welcome contribution on our project, your contribution enhances our app and increase it's efficiency.

## Setup the Project locally

1. Fork this repository into your Github account.
2. Clone the forked repository in your local system.
3. Create a virtual environment *(if needed)*.
4. Run `pip3 install -r requirements.txt` (or) `poetry install` to install all dependencies for the backend.
5. Navigate to the `Pluto-Frontend` directory using `cd Pluto-Frontend`.
6. Then run `npm install` (or) `yarn install` to install all dependencies for the frontend.
7. Now navigate to `Pluto` directory using `cd Pluto`.
8. Then run `python3 manage.py makemigrations` to make migrations in the database and `python3 manage.py migrate` to migrate the changes.
9. Now open two terminals for running the backend and frontend simultaneously due to the fact that both backend and frontend should be running at the same time in order for the web app to work.
10. In the first terminal, navigate to `Pluto` directory using `cd Pluto` and run `python3 manage.py runserver` to run the django backend server.
11. Then in the second terminal, navigate to `Pluto-Frontend` directory using `cd Pluto-Frontend` and run `npm run dev`.
13. Finally, you can now view the web app by visiting `127.0.0.1:8000` *(which is the common local url in most cases)* in your browser.

    Thanks for setting up our project locally and now, you can start contributing! If you ran into any problems, feel free to open a new issue using the Bug fix issue template!

## Guide on Contributing to this Project

1. You can always find issues tagged "good first issue", those issues can be done easily by the new contributors.
2. After finding an issue to work on, first off check if there is any assignees already.
3. Then read the description of the issue and almost every comment on the issue which could  be helpful to work on.
4. Finally *(if there are any assignees already)* ping/CC them in the issue comments to ask and discuss about their current progress and knowledge on the issue which will be extremely helpful for your work.
5. By now, you may have already setup the project locally and if not [check this out!](#setup-the-project-locally).
6. While working on the project, be sure that in case you create or edit a model in [`models.py`](./Pluto/Pluto_Backend/models.py) you also have to update the [`schema.py`](./Pluto/Pluto_Backend/schema.py) to enable the frontend to fetch the model you created or edited. you can find [the docs](https://docs.graphene-python.org/projects/django/en/latest/schema/) of `graphene-django` helpful. 
7. You also have to update or create *(if applicable)* the test cases in [`tests.py`](./Pluto/Pluto_Backend/tests.py) when you create or edit a model in [`models.py`](./Pluto/Pluto_Backend/models.py).
8. After finishing the changes, you have just to checkout to beta branch and commit the changes and push the changes to your forked repository.
9. Checkout/Switch to the beta branch by running `git checkout -b beta` as we recommend making changes in the beta branch and later propose the changes to the main branch. 

> [!WARNING]
> If you committed your changes to the main branch then your changes will not be accepted!

10. Then add and commit your changes and push it to your forked repository
11. After pushing the changes to your forked repository, create a pull request from your forked repository to the main repository and be sure to also mention the issue using `#` (i.e. `#15`) in the pull request's name itself. 
12. Your pull request will automatically be reviewed and merged into the main repository *(if it didn't run into any problems or any poor implementation)*
13. If you found any bug, then create a new issue with the Bug Fix issue template and anyone who found that this issue can be fixed will get assigned to this issue and fix this issue or maybe you can also try fixing it by yourself if you think you can fix the issue by your own or with the help of others. 

    Thank you for your contributions to this project, we appreciate it very much!

## Code of Conduct 
We appreciate if all the contributions to follow the [`CODE_OF_CONDUCT`](./CODE_OF_CONDUCT.md) to help us build a better community!

> [!NOTE]
> If you like the repository and our work then why not star our repository to show support!

<br>
Once again we thank everyone who have contributed to this project by far and we also appreciate the ones who will contribute to this project in the future!
