FROM bezuglyr/mytesttask

#RUN git clone https://github.com/BezuglyR/testingWeather.git /usr/src/app/

RUN mkdir /usr/src/app
ADD . /usr/src/app/
WORKDIR /usr/src/app

VOLUME /dev/shm
EXPOSE 4444
EXPOSE 80

RUN apt update
RUN pip install --no-cache-dir -r requirements.txt

RUN service elasticsearch start

ENTRYPOINT ["python", "main.py"]
