import typing
import boto3
from boto3_type_annotations.s3 import Client
from dotenv import load_dotenv
import vars
import botocore.exceptions

load_dotenv()
s3: Client = boto3.client('s3')


def concat(*args) -> str:
    return '/'.join(args)


class AWSFeeder:
    def list(self, prefix: str = None, after: str = None, limit: int = None, count: int = 0):
        res = s3.list_objects_v2(Bucket=vars.S3_BUCKET, Prefix=concat(vars.S3_PATH, prefix), StartAfter=after,
                                 MaxKeys=limit, Delimiter='/')
        ret = list([item['Key'] for item in res['Contents']])
        if res['IsTruncated'] and count + len(ret) < limit:
            return ret.extend(
                self.list(prefix=prefix, after=res['NextContinuationToken'], limit=limit, count=count + len(ret)))
        return ret

    def scan_prefix(self, prefix: str, on_next: typing.Callable, on_error: typing.Callable):
        keys = self.list(prefix=concat(vars.S3_PATH, prefix))
        filenames = []
        for key in keys:
            filename = concat(vars.CACHE, key)
            try:
                s3.download_file(Bucket=vars.S3_BUCKET,
                                 Key=concat(vars.S3_PATH, prefix, key),
                                 Filename=filename)
                filenames.append(filename)
            except Exception as e:
                on_error(e)
            on_next(filename)
        return filenames
