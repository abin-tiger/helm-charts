# -*- coding: utf-8 -*-

from locust import HttpUser, task
import s3fs
import json

default_headers = {'Content-Type': 'application/json'}
fs = s3fs.S3FileSystem()

payload = json.load(fs.open('test-bucket-mleteam/abin/curl_es_qa.txt', 'r'))

class WebsiteUser(HttpUser):

    @task
    def get_item_calculation(self):
        self.client.post("/ms-api/item-calc", headers=default_headers,  json=payload)
