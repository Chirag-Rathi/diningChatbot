from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
import json
import requests

host = 'url'
region = 'us-east-1'

index = 'restauants'

res = requests.delete(host+'/'+index,  auth=('username', 'password'))
