import OdessaApi
import KievApi
import HersonApi
import SeleniumRequestWeather

from elasticsearch import Elasticsearch
import unittest

es = Elasticsearch()

class TestSuite(unittest.TestCase):

    def test_Odessa(self):
        odessaSelenium = es.get(index="odessa", id=1)
        odessaApi = es.get(index="odessaapi", id=4)

        print('Start Testing Odessa')

        odessa = odessaSelenium['_source']
        odessaapi = odessaApi['_source']
        self.assertDictEqual(odessa, odessaapi)

    def test_Kiev(self):
        kievSelenium = es.get(index="kiev", id=2)
        kievApi = es.get(index="kievapi", id=5)

        print('Start Testing Kiev')

        kiev = kievSelenium['_source']
        kievapi = kievApi['_source']
        self.assertDictEqual(kiev, kievapi)

    def test_Herson(self):
        hersonSelenium = es.get(index="herson", id=3)
        hersonApi = es.get(index="hersonapi", id=6)

        print('Start Testing Herson')

        herson = hersonSelenium['_source']
        hersonapi = hersonApi['_source']
        self.assertDictEqual(herson, hersonapi)

if __name__== "__main__":
    unittest.main()

