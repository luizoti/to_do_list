# postgres deps

sudo apt-get install libpq-dev python3-dev

# alembic create migration

alembic revision --autogenerate -m "squash"

# alembic run migrate:

alembic upgrade head