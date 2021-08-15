import typing
import boto3
from boto3_type_annotations.s3 import Client
from dotenv import load_dotenv
import vars
import botocore.exceptions

load_dotenv()
s3: Client = boto3.client('s3')


class AWSFeeder:
    def list(self, prefix: str = None, after: str = '', limit: int = 2 ** 30, count: int = 0):
        res = s3.list_objects_v2(Bucket=vars.S3_BUCKET, Prefix=prefix,
                                 StartAfter=after, MaxKeys=limit, Delimiter='/')
        dirs = list([p['Prefix'] for p in res['CommonPrefixes']])
        keys = list([item['Key'] for item in res['Contents']])
        if res['IsTruncated'] and count + len(keys) < limit:
            new_keys, new_dirs = self.list(prefix=prefix, after=res['NextContinuationToken'], limit=limit,
                                           count=count + len(keys))
            return keys.extend(new_keys), dirs.extend(new_dirs)
        return keys, dirs

    def scan_prefix(self, prefix: str, key_processor: typing.Callable, on_next: typing.Callable,
                    on_error: typing.Callable):
        keys, _ = self.list(prefix=prefix)
        filenames = []
        for key in keys:
            keyfrag = key_processor(key)
            if keyfrag:
                filename = vars.concat(vars.CACHE, keyfrag)
                print('downloading to ', filename)
                try:
                    s3.download_file(Bucket=vars.S3_BUCKET, Key=key, Filename=filename)
                    filenames.append(filename)
                except Exception as e:
                    on_error(e)
                on_next(filename)
        return filenames

    def upload(self, key: str, filename: str):
        pass
