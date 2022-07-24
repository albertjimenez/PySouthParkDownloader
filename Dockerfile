FROM python:3.9.13-alpine3.15
# install ffmpeg
RUN apk add ffmpeg
RUN apk add build-base
WORKDIR south_park
COPY main.py requirements.txt ./
ADD post_processor ./post_processor
ADD util_functions ./util_functions
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python3", "main.py"]