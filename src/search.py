import boto3

# Create an S3 client
s3 = boto3.client('s3')

def search_s3_bucket(bucket, item, page_size=100, start_after=None):
  # Set the pagination parameters
  params = {
    'Bucket': bucket,
    'MaxKeys': page_size,
  }
  if start_after:
    params['StartAfter'] = start_after

  # Get a list of objects in the bucket, using the pagination parameters
  objects = s3.list_objects_v2(**params)

  # Search through the objects for the item
  for obj in objects['Contents']:
    if obj['Key'] == item:
      # Return the object if it is found
      return obj

  # If the item was not found and there are more pages of results,
  # call the search function again to search the next page of results
  if objects['IsTruncated']:
    return search_s3_bucket(bucket, item, page_size, objects['NextContinuationToken'])

  # Return None if the item is not found
  return None
