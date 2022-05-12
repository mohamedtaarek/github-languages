# Trending Repositories 

### Getting started
---
- Install a package manager and environment management system "Conda is the recommended one"

  > https://docs.conda.io/en/latest/miniconda.html

- Create a conda environment that lives in the same directory and install python:3.6

  ```bash
  conda create --prefix ./venv python=3.9
  ```

  > for more information check : https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

- Activate the conda environment

  ```bash
   conda activate ./venv
  ```
- Install packages and dependencies

  ```bash
    pip install -r requirements.txt
  ```

- add your local variables in the ".env.json" file as:
  ```json
    {
        "DEBUG": true,
        "ALLOWED_HOSTS": ["*"],
        "DJANGO_SECRET_KEY": "**************",
        "BASE_DIR": "Directory path"
    }
  
  ```


### Run Server
```bash
 python manage.py runserver
```
### View
---
- send get request to 127.0.0.1:8000/trending-repos/ 

### purpose
---
The API aims to classify the latest 100 trending repositories on [Github](www.github.com) according to languages used.

### Response
--- 
The API returns an object containing list of keys which are programming languages used in those trending repositories and each key has a value of  and object containing count and list repositories as following:
```json
    {
        "Java": {
            "count": 3,
            "repositories": [
                *** LIST OF REPOSITORIES ***
            ]
        },
        "Python": {
            "count": 18,
            "repositories": [
                *** LIST OF REPOSITORIES ***
            ]
        }
    }
```