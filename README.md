### S3 Flask Example

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

### Installation:
- Install dependencies: `pip3 install -r requirements.txt`
- Run Flask Application on Port 80: `flask run --host=0.0.0.0 --port=8080`


