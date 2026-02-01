# Lottery Project

### Functional Requirments & Assumptions

- [ ] A lottery event will be created automatically each day at midnight
    - do it by celery beat schedule
- [ ] Can create users with different roles: admin, participant
- [ ] Admin users can create/update/delete lottery events manually
    - practice router based url and modelviewsets here
- [ ] Admin users can view all lottery events list and participants count
- [ ] Admin users can view all participants for a specific lottery event
- [ ] Admin users can export all data of a specific lottery event in CSV, json, etc formats
    - practice different type of renders here
- [ ] Users can register for lottery events as participants.
- [ ] Lottery participants will be able to buy as many lottery ballots as possible which is not closed yet.
- [ ] Each day at midnight the lottery event will be closed and a random lottery-winning ballot will be selected from
  all the participants.
- [ ] All users will be able to check the winning ballot for any specific date.

### Additional

```
● The winner will be notified via email.
● Users have to pay per lottery ballot submission.
```


## Instructions to run the application

Go to the project root folder **lottery** and run the command

```
docker-compose up --build
```


The app will run on **0.0.0.0:8081**


-------------

### To get the full description of the project please have a look at the **readme-doc.pdf**.



## Development: Pre-commit hooks
To enable automatic code quality checks locally before each commit:

1. Install pre-commit (once):
   - pip install pre-commit
2. Install the git hooks in this repo (once):
   - pre-commit install
3. Run on all files (optional, to check/fix current tree):
   - pre-commit run --all-files

The configured hooks will run ruff, black, flake8, and basic file hygiene checks.
