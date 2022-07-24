# PySouthParkDownloader
This repository contains a script in Python 3.9 to download from southparkstudios.com.

You can use it as a standalone script or use the docker image already built on [Dockerhub](https://hub.docker.com/r/beruto/pysouthparkdownloader).

## Usage standalone script
1. Run `pip3 install -r requirements.txt`
2. Run `python3 main.py linkAsArgument` where linkAsArgument is the HTTPS url.

### Example standalone script
`python3 main.py https://www.southparkstudios.com/episodes/fi4nmu/south-park-mexican-joker-season-23-ep-1`

## Usage with Docker
You can either pull the image beruto/pysouthparkdownloader using `docker pull beruto/pysouthparkdownloader:latest` or build it yourself using the `Dockerfile`.

### Example Docker
`docker run -v "$(pwd)":/south_park beruto/pysouthparkdownloader https://www.southparkstudios.com/episodes/jiru42/south-park-basic-cable-season-23-ep-9`

## Disclaimer
Tested on:
- Raspberry Pi 4 - 8GB on Raspbian
- Macbook Pro Intel with Docker and script (dev laptop)

Untested script in Windows, Docker should work, mounting point should be adapted on Windows path-style.