# FastAPI with Redis job queue

## Run

```bash
cd myproj_app
docker build -t myproj:latest .
docker-compose -f docker-compose.yml up --scale myproj_worker=1
```

## Post task

```bash
curl -v -X POST -H "Content-Type: application/json" -d '{"owner":"foo","description":"bar"}' http://localhost:5057/groups/group1
```

## Scale workers

```bash
docker-compose -f docker-compose.yml up --scale myproj_worker=4 --detach
```