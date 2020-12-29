shopping-lists
==============

Manage simple shopping lists with a web app written in django

Screenshots
============
Index page :

![ScreenShot](https://raw.github.com/shaftmx/shopping-lists/master/screenshots/index.png)

Shopping list page:

![ScreenShot](https://raw.github.com/shaftmx/shopping-lists/master/screenshots/list.png)

Short shopping list page (only missing items) :

![ScreenShot](https://raw.github.com/shaftmx/shopping-lists/master/screenshots/short_list.png)

Recipe page :

![ScreenShot](https://raw.github.com/shaftmx/shopping-lists/master/screenshots/recipe.png)


# Install

Simply run the docker image with those parameters

```yaml
    image: shaftmx/shopping-lists
    ports:
      - "8000:80"
    environment:
      DB_NAME: netwiki_shop
      DB_HOST: db
      DB_USER: root
      DB_PASSWORD: root
```

For the first setup you can force manually the creation of a user going into the container and running

```bash
python /shoppingList/manage.py createsuperuser
```

# Legacy migration

Your container should run with this following cconfiguration using sleep 3600 as command

```yaml
    image: shaftmx/shopping-lists
    command: sleep 3600
    environment:
      DB_NAME: shop
      DB_HOST: db
      DB_USER: root
      DB_PASSWORD: root
```

Then connect in the container and do the following steps

```bash
sudo docker exec -it shopping-lists_web_1 bash
python /legacy_migration.py -d
# A json file should be created under /tmp/...
# drop and recreate the database to flush it
# If it's easier for you, you can install mysql client in the container and do it from there
apt-get update && apt-get install -y default-mysql-client
# Small dump just in case
mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASSWORD --databases $DB_NAME --skip-extended-insert > /tmp/dump.sql
mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e "drop database $DB_NAME;"
mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e "create database $DB_NAME;"
```
Init the new db

```bash
/entrypoint & # This script will actually call python /shoppingList/manage.py migrate
# Create an initial user
python /shoppingList/manage.py createsuperuser
```

Load the datas in it

```bash
python /legacy_migration.py -l
```

Then is should be working. You can now test it live then if everything is ok run your container as usual.


# Some notes to run local dev tests

Run local env

```bash
docker-compose up --build
```

Run local db shell
```bash
sudo docker exec -it shopping-lists_web_1 python shoppingList/manage.py dbshell
```

Creating/running db migration

```bash
python manage.py makemigrations
python manage.py migrate
```
