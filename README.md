# Build

1. Docker build:
```
docker build -t nima-cpu . -f Dockerfile.gpu
```




```
python3 -m evaluater.predict -b MobileNet -w ../models/MobileNet/weights_mobilenet_technical_0.11.hdf5 -is ../images/ -pf ../predictictions.json
```