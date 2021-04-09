FROM selenium/standalone-chrome

#RUN git clone https://github.com/BezuglyR/testingWeather.git /usr/src/app/

RUN sudo mkdir /usr/src/app
ADD . /usr/src/app/
WORKDIR /usr/src/app

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
RUN sudo apt-get install apt-transport-https
RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
RUN sudo apt-get update && sudo apt-get install elasticsearch

VOLUME /dev/shm:/dev/shm
ENV discovery.type=single-node
EXPOSE 4444:4444
EXPOSE 7900:7900
EXPOSE 9200:9200
EXPOSE 9300:9300

RUN sudo pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT sudo sysctl -w vm.max_map_count=262144 sudo service elasticsearch start && sudo python3 main.py
