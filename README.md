# S3 Flask Example

![Block diagram of expected architecture](diagram.png?raw=true "Block Diagram")

- The application sends a POST request to `<Submission IP Address>/begin` with the following content:
```
{
   "banner": "<Student Banner ID>",
   "ip": "<EC2 IP Address>"
}
```

- A request to `/begin` with the `data` keyword, containing a text which has to be stored in S3.
```
{
   "data": "<A string to store in S3>"
}
```

- The expected output:
```
{
   "s3uri": "<Public URL of the S3 file created>"
}
```

## Installation:
- Install dependencies: `pip3 install -r requirements.txt`
- Create a new file `.env` with the environmental variables mentioned in `.env.example`
- Run Flask Application on Port 80: `python3.9 app.py

## Quick Deployment (AWS EC2)
**Note:** For development and testing purpose only
- Create an EC2 instance (AWS Linux 2) and SSH into the machine: `ssh -i ec2-licensing-keypair.pem ec2-user@<ec2-public-ip-address>`
- Install git: `sudo yum install git -y`
- Clone the repository: `git clone https://github.com/addu390/s3-flask-example.git`

### Install and Install Python 3.9:
- Pre-requisites: `sudo yum install gcc openssl-devel bzip2-devel libffi-devel`
- Download Python 3.9:
	- `cd /opt`
	- `sudo wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz`
	- `sudo tar xzf Python-3.9.6.tgz`
	- `cd Python-3.9.6`
	- `sudo ./configure --enable-optimizations`
	- `sudo make altinstall`
	- `sudo rm -f /opt/Python-3.9.6.tgz`
	- `python3 -V` or `python3.9 -V`

### Install Dependencies:
- Create Virtual Environment: `python3.9 -m venv env`
- Activate: `source env/bin/activate`
- Install Dependencies: `sudo python3 -m pip install -r requirements.txt`

### Run the application
- `sudo python3 app.py --host=0.0.0.0 --port=80`

### For production use, consider the following tutorials:
- [Dockerizing Django Application — Gunicorn and Nginx](https://blog.devgenius.io/dockerizing-django-application-gunicorn-and-nginx-5a74b250198f)
- [Deploying Django Application on AWS EC2 and Docker](https://medium.com/dev-genius/deploying-django-application-on-aws-ec2-and-docker-10a1f7c29573)
- [Deploying Django Application on AWS Fargate in 8 minutes](https://medium.com/faun/deploying-django-application-on-aws-fargate-in-8-minutes-f04373880e0a)


