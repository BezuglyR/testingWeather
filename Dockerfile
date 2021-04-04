FROM bezuglyr/mytesttask

#RUN git clone https://github.com/BezuglyR/testingWeather.git /usr/src/app/

RUN sudo mkdir /usr/src/app
ADD . /usr/src/app/
WORKDIR /usr/src/app

VOLUME /dev/shm:/dev/shm
EXPOSE 4444:4444
EXPOSE 80:80
EXPOSE 7900:7900

RUN sudo apt update
RUN pip3 install --no-cache-dir -r requirements.txt

#RUN sudo service elasticsearch start

ENTRYPOINT ["sudo", "service", "elasticsearch", "start"]

CMD ["sudo", "python3", "main.py"]
