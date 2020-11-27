# Memsource chess homework

This is a simple REST program calculating the number of unique valid positions
on a nxn chessboard with n chess pieces.

## Installation
```bash
$ python3 -m venv <your_virtual_environment>
$ source <your_virual_environment>/bin/activate
$ python3 -m pip install https://github.com/tibor-reiss/memchess/raw/master/dist/memchess-1.0.0-py3-none-any.whl
$ export FLASK_APP=src
```

## Usage
### Starting the program
```bash
$ flask run
```

### Running requests
```bash
$ curl -X POST -H 'Content-Type: application/json' -d '{"n": 8, "chessPiece": "queen"}' http://127.0.0.1:5000/chess
```
```bash
$ curl -X GET "http://127.0.0.1:5000/result?id=queen_8"
```
The sqlite3 file will be located in <your_virtual_environment>/var/src-instance/memsource.db

### Running the tests
```bash
$ pytest
```
