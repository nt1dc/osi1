export containerID=$(docker ps --format "{{.ID}}")
docker cp $containerID:/home/io .
docker cp $containerID:/home/threads.txt .
