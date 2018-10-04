from __future__ import print_function
import time
import boto3
import urllib.request
import json

demo_name = 'image-analysis-1' # Soda Bottles
#demo_name = 'image-analysis-2' # Speaker Presentation
#demo_name = 'image-analysis-3' # Audience in Pub
#demo_name = 'image-analysis-4' # People Working on Laptop
#demo_name = 'image-analysis-5' # People Working at Wood Table
demo_name = 'image-analysis-6' # Speaker Presentation with Audience
#demo_name = 'image-analysis-7' # Man and Bear

bucket_name = 'sgfdevs-demo-2018'

s3 = boto3.client('s3')
filename = demo_name+'.jpg'
s3.upload_file(filename, bucket_name, filename, ExtraArgs={'ACL':'public-read'})

client = boto3.client("rekognition")
response = client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':filename}})

print('Detected labels for ' + filename)    
for label in response['Labels']:
    print (label['Name'] + ' : ' + str(label['Confidence']))

response = client.detect_faces(Image={'S3Object':{'Bucket':bucket_name,'Name':filename}}, Attributes=['ALL'])

print('Detected faces for ' + filename)
for face in response['FaceDetails']:
    print(face)
