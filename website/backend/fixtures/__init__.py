
# python3 backend/manage.py dumpdata user --indent 2 --format json --exclude auth.permission --exclude contenttypes > backend/user/fixtures/init_fixtures.json
# python3 backend/manage.py dumpdata photo_album --indent 2 --format json --exclude auth.permission --exclude contenttypes > backend/photo_album/fixtures/init_fixtures.json


# python3 backend/manage.py loaddata backend/user/fixtures/init_fixtures.json
# python3 backend/manage.py loaddata backend/photo_album/fixtures/init_fixtures.json
