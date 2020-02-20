import requests
import urllib3
import json
import os

# https://lilt.com/docs/api
class Lilt_API:
    lilt_base_url = "https://lilt.com/2/"
    lilt_api_key = ""

    def __init__(self, lilt_api_key):
        self.lilt_api_key = lilt_api_key

    def get_endpoint(self, endpoint):
        return "{}{}?key={}".format(self.lilt_base_url, endpoint, self.lilt_api_key) 

    def create_project(self, project_name, mem_id):
        body = {"name": project_name, "memory_id": mem_id}
        headers = {"Content-Type": "application/json"}
        res = requests.post(
            self.get_endpoint("projects"), headers=headers, json=body, verify=False
        )
        if res.status_code == 200:
            return res.json()["id"]
        else:
            print(res)
            return -1

    def get_memory(self, mem_id):
        payload = {"id": mem_id}
        res = requests.get(self.get_endpoint("memories"), params=payload, verify=False)
        if res.status_code == 200:
            return res.json()  # ["trglang"]
        else:
            print(res)
            return -1

    def create_memory(self, name, src, trg):
        body = [("name", name), ("srclang", src), ("trglang", trg)]
        res = requests.post(self.get_endpoint("memories"), data=body, verify=False)
        if res.status_code == 200:
            # HTTP status code 200 means the request was successful.
            return res.json()["id"]
        else:
            print(res)
            return -1

    def upload_document(self, filename, projid, pretranslate="null", auto_accept=False):
        name = os.path.basename(filename)

        jsonData = {"name": name, "project_id": projid, "pretranslate":pretranslate, "auto_accept":auto_accept}
        headers = {
            "LILT-API": json.dumps(jsonData),
            "Content-Type": "application/octet-stream",
        }
        with open(filename, "r") as fp:
            rawdata = fp.read()
        rawdata = rawdata.encode("utf-8")
        try:
            res = requests.post(
                self.get_endpoint("/documents/files"),
                data=rawdata,
                headers=headers,
                verify=False,
            )
        except Exception as e:
            print(e)
        if res.status_code != 200:
            return -1
        # No error continue on your marry way
        return res.json()["id"]

    def assignDocument(self, email, docId, is_translator=True, is_reviewer=False):
        headers = {"Content-Type": "application/json"}
        body = {
            "id": docId,
            "email": email,
            "is_translator": is_translator,
            "is_reviewer": is_reviewer,
        }  # TODO update booleans
        res = requests.put(
            self.get_endpoint("/documents/share"),
            headers=headers,
            data=json.dumps(body),
        )
        if res.status_code == 200:
            # HTTP status code 200 means the request was successful.
            return res.json()["id"]
        else:
            print(res.json())
            return -1

    def pretranslate_documents(self, docID):
        jsonData = {"id": [docID]}  # can take a list of document IDs
        res = requests.post(
            self.get_endpoint("/documents/pretranslate"), json=jsonData, verify=False
        )
        if res.status_code == 202:
            # HTTP status code 200 means the request was successful.
            return res.json()
        else:
            print(res.json())
            return -1

    def get_document_status(self, docID):
        payload = {"id": docID}
        res = requests.get(self.get_endpoint("documents"), params=payload, verify=False)
        if res.status_code == 200:
            return res.json()
        else:
            print(res.json())
            return -1
