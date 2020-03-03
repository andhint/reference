# Reference

## Virtual Envs using venv

1) Creating 

`python3 -m venv [env name]` 
`python3 -m venv venv`

2) Activating

`source [env name]/bin/activate`
`source venv/bin/activate`

3) Deactivating

`deactivate`

4) Removing

`rm -R [env name]`
`rm -R venv`

Good practice to make environment named `venv` within each project directory

For creating requirements.txt
`pip freeze > requirements.txt`

To install dependencies from requirements.txt
`pip install -r requirements.txt`