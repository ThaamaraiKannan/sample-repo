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