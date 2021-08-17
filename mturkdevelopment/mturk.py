import boto3

from rootkey import keyid, secretkey


if __name__ == '__main__':
    client = boto3.client('mturk', endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com',
                          region_name='us-east-1', aws_access_key_id=keyid, aws_secret_access_key=secretkey)
