if [ -z ${PYTHON_VERSION+x} ]; then PYTHON_VERSION=3.7; fi

echo ""
echo ""
echo "******* Starting shell on Python $PYTHON_VERSION *******"
echo ""
PYTHON_VERSION=$PYTHON_VERSION docker-compose -p jsonmask-ng-dev-${PYTHON_VERSION/./-} run --rm app
