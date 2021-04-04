FROM bezuglyr/mytesttask

RUN git clone https://github.com/BezuglyR/testingWeather.git /usr/src/app/
#RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/



#RUN pip install --no-cache-dir -r requirements.txt


#ENTRYPOINT ["python", "main.py"]