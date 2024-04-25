# sneakhub-be
SneakHub backend service

After you pull this code repo to your local, follow the below steps to run the server:

create a virtual environment with "venv" module as a script.

`$ python -m venv .env`

activate the virtual environment.

`$ .env\Scripts\activate`

install all packages/libraries following the file "requirements.txt".

`$ pip install -r requirements.txt`
build the docker compose.

`$ docker compose build`
run server by command.
`$ docker compose up`

_you can check you app via the link http://localhost:80

stop the docker compose and remove it

`$ docker compose down`

deactivate the virtual environment.

`$ deactivate`
