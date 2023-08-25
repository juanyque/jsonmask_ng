[![Build Status](https://img.shields.io/travis/juanyque/jsonmask_ng/master.svg)](https://travis-ci.org/juanyque/jsonmask_ng) [![Coverage Status](https://img.shields.io/coveralls/juanyque/jsonmask_ng/master.svg)](https://coveralls.io/r/juanyque/jsonmask_ng) [![PyPI Version](https://img.shields.io/pypi/v/jsonmask_ng.svg)](https://pypi.org/project/jsonmask_ng)

# Overview

Implements [Google Partial Response](https://developers.google.com/discovery/v1/performance#partial-response) / [`json-mask`](https://github.com/nemtsov/json-mask) in Python.

jsonmask_ng is a fork of [jsonmask](https://github.com/zapier/jsonmask) from Zapier that seems discontinued.

## Requirements

- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11

## Installation

Install jsonmask_ng with pip:

```sh
$ pip install jsonmask_ng
```

or directly from the source code:

```sh
$ git clone https://github.com/juanyque/jsonmask_ng.git
$ cd jsonmask_ng
$ python setup.py install
```

# Usage

After installation, the package can imported:

```sh
$ python
>>> import jsonmask_ng
>>> jsonmask_ng.__version__
```

To prune dictionaries:

```py
>>> import jsonmask_ng
>>> mask = jsonmask_ng.parse_fields('a,b(c,d)')
>>> jsonmask_ng.apply_json_mask(
    {
        'a': {
            'nested_within_a': True,
        },
        'b': {
            'c': True,
            'd': {'Will get included?': 'Yes'},
            'e': 'Tough luck here',
        },
        'c': 'Definitely hopeless',
    },
    mask,
)
```

Output:

```py
{
    'a': {
        'nested_within_a': True,
    },
    'b': {
        'c': True,
        'd': {'Will get included?': 'Yes'},
    },
}
```

## Contribute

To setup an appropriate dev environment:

- With docker environment available
- run: `./docker_start.sh``

- run tests `make test`

- Clean (test, cache, ...) `make clean`

- Clean (test, cache, ... including virtualenv) `make clean-all` (you will need a `make all` after this)

- Build dist package: `make build`

- Set PyPI credentials: `poetry config pypi-token.pypi pypi-xxxxxTOKENXxxx` (find token in `~/.pypirc` file or create a new one on https://pypi.org/manage/account/token/)

- Build dist package: `make upload`

### Util commands:

- To fix poetry.lock with minimal changes: `poetry lock --no-update`
- To fix poetry.lock updating package versions: `poetry lock` (this could don't work)
- After `poetry lock...` probably you will need to do `make all` to update packages on virtualenv
