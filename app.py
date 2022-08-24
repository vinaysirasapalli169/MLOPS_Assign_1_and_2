
from flask import Flask
import os, uuid
from flask import jsonify
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

app = Flask(__name__)
@app.route('/')
def hello_world():
    name = '1'
    print(name)
    res = []
    
    connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccount4123;AccountKey=0+CBE9QTYMdwqlLA4nDYb2B2wgL8MS8rL0B+3S9/KhawJQTFQhjs/Ug0sOnHlAtrSKVenjxh+PTQ+AStbNpWAQ==;EndpointSuffix=core.windows.net"
    print(connect_str)
    blob_service_client = ContainerClient.from_connection_string(connect_str,container_name="data")
    blob_list = blob_service_client.list_blobs()
    print(blob_service_client)
    print(blob_list)
    for blob in blob_list:
        temp = str(blob.name)
        folder,file = temp.split('/')
        print(folder,name)
        if folder  ==  name:
            res.append(file)
    return jsonify(res)

app.run(host ='0.0.0.0', port = 5000, debug = True) 