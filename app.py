from flask import Flask, request
import requests
import boto3
import os

app = Flask(__name__)


@app.route("/storedata", methods=['POST'])
def definition():
    data = request.get_json(force=True)
    content = data.get("data")
    s3_url = upload(content)
    result = {
        "s3uri": s3_url
    }
    return result, 200


@app.route("/begin", methods=['POST'])
def definition():
    data = request.get_json(force=True)
    banner_id = data.get("banner")
    ip_address = data.get("ip")

    result = {
        "banner": banner_id,
        "ip": ip_address
    }
    response = requests.post('http://<ip-address>/begin', json=result)
    print('response from server:', response.text)
    if response.ok:
        return response.json(), 200
    else:
        return response.json(), 400


def upload(content):
    try:
        s3 = boto3.client("s3", region_name='ca-central-1', aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

        bucket = os.getenv("AWS_BUCKET_NAME")
        input_file = 'input.txt'

        s3.Object(bucket, input_file).put(Body=content)

    except Exception as e:
        print("Error: ", e)
        return e

    location = 'http://{}.s3.amazonaws.com/'.format(bucket)
    return "{}{}".format(location, input_file)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
