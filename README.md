# simple-backend

## How to run

```
export FLASK_APP=simple_backend
python -m flask run # flask run
```

## To make server externally visible

```
python -m flask run --host=0.0.0.0 # why is it ever 0.0.0.0?
```

## To make it dynamic refreshing like some spring package

```
flask run --extra-files dir1/file1:dir2/file2:dir3/ # export FLASK_RUN_EXTRA_FILES=dir1/file1:dir2/file2:dir3/
```

## To make it ignore some files

> __Warning: it uses `fnmatch`__

```
flask run --exclude-patterns foo*:bar? # export FLASK_RUN_EXCLUDE_PATTERNS=foo*:bar?
```

## Flask app config in .env

### Priorites of .\*env\*

1. `command line` -- any variables
2. `.env` -- private variables __!don't commit this file__
3. `.flaskenv` -- public variables