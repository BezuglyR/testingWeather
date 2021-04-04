FROM bezuglyr/mytesttask

RUN git clone https://github.com/BezuglyR/testingWeather.git /usr/src/app/

WORKDIR /usr/src/app/

RUN apt update && apt install -y python3-pip \
pip install --no-cache-dir -r requirements.txt

RUN service elasticsearch start

ENTRYPOINT ["python", "main.py"]