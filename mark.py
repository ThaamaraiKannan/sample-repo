print("dummy")
import boto3
s3 = boto3.client("s3")

def createBucket(BucketName, region='ap-south-1'):
    s3.create_bucket(
         Bucket=BucketName,
         CreateBucketConfiguration= {
             'LocationConstraint': region
         }
         
         
    )
    print("Bucket created successfully")
    return

def putBucketAcl(BucketName):
    response = s3.put_public_access_block(
        Bucket = BucketName,
        PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    },
    )
    print("Bucket is Publicly accessable....")
    return


def bucketOwnership(BucketName):
    response = s3.put_bucket_ownership_controls(
    Bucket=BucketName,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
    )
    print("changed Owner ship successfully")
    return

def putObject(BucketName, objectUrl, indexName):
    with open(objectUrl, "rb") as data:
        s3.put_object(
            ACL = 'public-read',
            Bucket = BucketName,
            Body = data,
            Key = indexName,
            ContentType = "text/html"
        )
    return

def staticWebsiteHost(BucketName, indexName):
    s3.put_bucket_website(
    Bucket=BucketName,
    WebsiteConfiguration={
        'IndexDocument': {
            'Suffix': indexName
        }
    })
    print("Bucket changed to Static Website")
    return

def deleteBucket(BucketName):
    s3.delete_bucket(Bucket = BucketName)
    return


def listBuckets():
    reponse = s3.list_buckets()
    return reponse["Buckets"]

def emptyBucket(BucketName):
    listObject = s3.list_objects_v2(Bucket = BucketName)
    print("Objects Deleting....")
    for data in listObject["Contents"]:
        s3.delete_object(
            Bucket = BucketName,
            Key = data["Key"]
        )
    print("Bucket is empty Now!")
    return
print("dummy")
