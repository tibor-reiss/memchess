# Memsource chess homework

This is a simple REST program calculating the number of unique valid positions
on a nxn chessboard with n chess pieces.

## Installation
```bash
$ python -m venv ve_memsource
$ source ve_memsource/bin/activate
$ pip install memsource
```

## Usage
### Starting the program
```bash
$ flask run
```

### Running requests
```bash
$ curl -X POST -H 'Content-Type: application/json' -d '{"n": 2, "chessPiece": "rook"}' http://127.0.0.1:5000/chess
```
```bash
$ curl -X GET "http://127.0.0.1:5000/result?id=rook_2"
```

### Running the tests
```bash
$ pytest
```
