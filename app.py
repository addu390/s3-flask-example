from flask import Flask, request
import requests
import boto3
import os
from dotenv import load_dotenv, find_dotenv
import uuid

load_dotenv(find_dotenv())

app = Flask(__name__)


@app.route("/storedata", methods=['POST'])
def store():
    data = request.get_json(force=True)
    content = data.get("data")
    print(content)
    s3_url = upload(content)
    result = {
        "s3uri": s3_url
    }
    return result, 200


@app.route("/begin", methods=['POST'])
def begin():
    data = request.get_json(force=True)
    banner_id = data.get("banner")
    ip_address = data.get("ip")

    result = {
        "banner": banner_id,
        "ip": ip_address
    }
    request_url = 'http://{}/begin'.format(os.getenv('DAL_IP_ADDRESS'))
    response = requests.post(request_url, json=result)
    print('response from server:', response.text)
    if response.ok:
        return response.json(), 200
    else:
        return response.json(), 400


def upload(content):
    try:
        session = boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        s3 = session.resource('s3')

        bucket = os.environ.get("AWS_BUCKET_NAME")
        input_file = str(uuid.uuid4()) + ".txt"

        s3_object = s3.Object(bucket, input_file)
        result = s3_object.put(Body=content)

    except Exception as e:
        print("Error: ", e)
        return e

    location = 'http://{}.s3.amazonaws.com/'.format(bucket)
    return "{}{}".format(location, input_file)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
