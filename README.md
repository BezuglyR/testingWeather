# testingWeather

This is testing task project.

using Python, write script, that:


1. Collect by Selenium with UI data from any weather forecast site. 3 cities on 3 day forecast and write it in elasticsearch.
2. Collect forecast on the next 3 days with 3 cities using API on another weather forecast site and also write in elasticsearch.
3. Read collected data from elasticsearсh and compare between 1 step and 2-nd.
For searching data from step 1 use xpath (write by your own, without generators)

To run this test you will need to download, install and run elasticsearch using this guide:
https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html 

In the future I will pack this test into docker with all requirements
