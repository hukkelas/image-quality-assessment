# Build

1. Docker build:
```
docker build -t nima-gpu . -f Dockerfile.gpu
```

2. Start docker container (NOTE: CHANGE DEVICE!)
```
docker run  -v $PWD/:/workspace  -it --rm --gpus "device=1" --name haakohu/nima --ipc=host -u 1174424 -v /work/haakohu:/work/haakohu  nima-gpu bash
```


3. When  in docker container:
```
cd src/
python3 -m evaluater.predict -is /work/haakohu/datasets/fdh_v3/images/ -pf /work/haakohu/datasets/fdh_v3/nima_predictions.json
```