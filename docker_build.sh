if [ -z ${PYTHON_VERSION+x} ]; then PYTHON_VERSION=3.7; fi

PYTHON_VERSION=$PYTHON_VERSION docker-compose build
