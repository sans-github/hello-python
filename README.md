# Resources
[Learning Pandas for Data Analysis? Start Here by Rob Mulla](https://www.youtube.com/watch?v=DkjCaAMBGWM)

# Set up
1. Create a virutal env: `python3 -m venv .venv`

2. Activate the virutal environment: `source .venv/bin/activate`

3. Install project dependencies: 

    3.1 From requirements.txt `pip install -r requirements.txt`
    
    3.2 Or individually
    ```
    pip install pandas
    ```


# UV reference
* Create/update the env from toml file `UV sync`

* List of installed dependencies with `uv pip list`

* Write installed Python packages to requirements.txt: `UV pip freeze > requirements.txt`

* `uv tool run ruff check --fix .` Fix formatting. 

# Exit
To deactivate the env - `deactivate`