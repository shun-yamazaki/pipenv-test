import sys
from src import lambda_function
from moto import mock_s3
import boto3


def test_function():
    assert lambda_function.some_func("1", 2) == "12"
    assert lambda_function.some_func("a", 2) == "a2"


def test_function2():
    assert lambda_function.some_func("1", 2) == "12"
    assert lambda_function.some_func("a", 2) == "a2"


@mock_s3
def test_s3_bucket():
    client = boto3.client('s3')
    bucket_name = "mock-bucket"
    key = "mock-key"
    buckets = lambda_function.get_from_s3(bucket_name, key)
    assert buckets == []
    client.create_bucket(Bucket=bucket_name)
    buckets = lambda_function.get_from_s3(bucket_name, key)
    print(buckets)
    assert buckets == []
