import boto3


# region 関数たち
def some_func(str1, num1):
    """
    引数を文字列として結合する
    :param str1: 文字列
    :type str1: str
    :param num1: 数値
    :type num1: int
    :return: 結合した文字列
    :rtype: str
    """
    return str1 + str(num1)


def get_from_s3(bucket_name, key):
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()['Buckets']
    return buckets


# endregion

def lambda_handler(event, context):
    print('Hello world.')
    test1 = some_func("a", 10)
    # test2 = some_func("a", "a")
    # test3 = some_func(10, 10)
