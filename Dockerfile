FROM bezuglyr/mytesttask

#RUN git clone https://github.com/BezuglyR/testingWeather.git /usr/src/app/

RUN sudo mkdir /usr/src/app
ADD . /usr/src/app/
WORKDIR /usr/src/app

VOLUME /dev/shm:/dev/shm
EXPOSE 4444:4444
EXPOSE 7900:7900
EXPOSE 9200:9200

RUN sudo apt update
RUN sudo pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT sudo sysctl -w vm.max_map_count=262144 && sudo service elasticsearch start && sudo python3 main.py
