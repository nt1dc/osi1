export containerID=$(docker ps --format "{{.ID}}")
docker cp io.py $containerID:/home
docker cp threads.py $containerID:/home
docker cp script.sh $containerID:/home
