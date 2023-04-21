# To Start the virtualenv in your env
sudo apt-get update
sudo apt-get install python3-virtualenv
virtualenv venv
source venv/bin/activate

# Start redis
docker pull redis
docker run --name redis-lab -p 6379:6379 -d redis
docker exec -it redis-lab bash
redis-cli

# Start worker
celery -A proj worker -l INFO 