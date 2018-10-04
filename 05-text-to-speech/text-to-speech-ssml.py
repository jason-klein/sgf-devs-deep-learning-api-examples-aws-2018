from boto3 import client
polly = client("polly", region_name="us-east-1")

# SSML Tag Reference
# https://docs.aws.amazon.com/polly/latest/dg/ssml.html
# Demonstrate SSML speaking rate and breath
text = '<speak><prosody rate="fast">Imagine seven million people all wanting to live together.</prosody> Yeah,<amazon:breath/> New York must be the friendliest place on earth.</speak>'

voice = "Russell" # Australian English Male

response = polly.synthesize_speech(
        Text=text,
        TextType="ssml",
        OutputFormat="mp3",
        VoiceId=voice)

# Save to MP3
file = open('text-to-speech-ssml.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

