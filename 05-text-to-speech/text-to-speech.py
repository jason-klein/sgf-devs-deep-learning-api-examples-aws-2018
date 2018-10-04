from boto3 import client
polly = client("polly", region_name="us-east-1")

text = 'This is a Text to Speech demonstration for the Springfield Web Developers'

response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna")

# Save to MP3
file = open('text-to-speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
