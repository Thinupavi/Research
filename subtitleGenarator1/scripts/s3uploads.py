# import boto3
# from botocore.client import Config
# import boto
# from boto.s3.key import Key
#
# AWS_ACCESS_KEY_ID = 'AKIAJ5QQLFOLAGZ4HSKQ'
# AWS_SECRET_ACCESS_KEY = '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'
# BUCKET_NAME = 'subgenerator'
#
# s3 = boto3.resource('s3')
#
#
#
# s3.Bucket('subgenerator').put_object(Key='a_python_file.mp4', Body='../webApp/Videos/Sharing your Google data with Apps - New.mp4')
#
#
import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAJ5QQLFOLAGZ4HSKQ'
AWS_SECRET_ACCESS_KEY = 'gAwBQ6H2hO39sg06RgErI+4CWtRorhdbey4JKHw7'

bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "replace this with an actual filename"
print( 'Uploading %s to Amazon S3 bucket %s' % (testfile, bucket_name))

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = '../webApp/Videos/Sharing your Google data with Apps - New.mp4'
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)