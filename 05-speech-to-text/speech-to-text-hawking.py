from __future__ import print_function
import time
import boto3
import urllib.request
import json

demo_name = 'speech-to-text-hawking'
bucket_name = 'sgfdevs-demo-2018'

s3 = boto3.client('s3')
filename = demo_name+'.wav'
s3.upload_file(filename, bucket_name, filename, ExtraArgs={'ACL':'public-read'})

transcribe = boto3.client('transcribe')
job_name = demo_name+'-'+str(time.time())
job_uri = "https://s3.amazonaws.com/"+bucket_name+"/"+filename
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='wav',
    LanguageCode='en-US'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
#print(status)

transcript_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
#print(transcript_url)

# Download Transcription Results to JSON File
transcript_file = demo_name+'.json'
urllib.request.urlretrieve(transcript_url, transcript_file)

with open(transcript_file, 'r') as transcript_file:
    transcript_json=transcript_file.read().replace('\n', '')

# Display Transcription
transcript_data = json.loads(transcript_json)
transcript_text = transcript_data['results']['transcripts'][0]['transcript']
print(transcript_text)
