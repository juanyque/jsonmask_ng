docker-compose -f docker-compose_test-all.yml build

# docker-compose -f docker-compose_test-all.yml up
docker-compose -f docker-compose_test-all.yml run --rm app_3.7 make test-all
docker-compose -f docker-compose_test-all.yml run --rm app_3.8 make test-all
docker-compose -f docker-compose_test-all.yml run --rm app_3.9 make test-all
docker-compose -f docker-compose_test-all.yml run --rm app_3.10 make test-all
docker-compose -f docker-compose_test-all.yml run --rm app_3.11 make test-all
