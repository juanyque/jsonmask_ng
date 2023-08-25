PYTHON_VERSIONS='3.7 3.8 3.9 3.10 3.11'

for PYTHON_VERSION in $PYTHON_VERSIONS
do
  echo "******* Building Python $PYTHON_VERSION *******"
  PYTHON_VERSION=$PYTHON_VERSION docker-compose -f docker-compose_test.yml -p jsonmask-ng-test-${PYTHON_VERSION/./-} build &
  echo ""
done

wait $(jobs -rp)

for PYTHON_VERSION in $PYTHON_VERSIONS
do
  echo ""
  echo ""
  echo "******* Testing on Python $PYTHON_VERSION *******"
  echo ""
  PYTHON_VERSION=$PYTHON_VERSION docker-compose -f docker-compose_test.yml -p jsonmask-ng-test-${PYTHON_VERSION/./-} run --rm app
  echo ""
  docker rmi $(docker images "jsonmask-ng-test-${PYTHON_VERSION/./-}-app" -a -q)
  echo ""
done
