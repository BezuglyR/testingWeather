FROM bezuglyr/mytesttask

#RUN git clone https://github.com/BezuglyR/testingWeather.git /usr/src/app/

RUN sudo mkdir /usr/src/app
ADD . /usr/src/app/
WORKDIR /usr/src/app

VOLUME /dev/shm
EXPOSE 4444
EXPOSE 80

RUN sudo apt update
RUN pip3 install --no-cache-dir -r requirements.txt

RUN sudo service elasticsearch start

ENTRYPOINT ["python3", "main.py"]
