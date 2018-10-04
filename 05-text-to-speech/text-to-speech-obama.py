from boto3 import client
polly = client("polly", region_name="us-east-1")

# 2010 State of the Union
# https://www.nytimes.com/2010/01/28/us/politics/28obama.text.html
transcript_file = 'text-to-speech-obama.txt'
with open(transcript_file, 'r') as transcript_file:
    text=transcript_file.read()

# SSML Tag Reference
# https://docs.aws.amazon.com/polly/latest/dg/ssml.html
# https://docs.aws.amazon.com/polly/latest/dg/supported-ssml.html
# Automatically Add Pauses for Breathing
text = '<speak><amazon:auto-breaths>'+text+'</amazon:auto-breaths></speak>'
# Replace new paragraphs and hyphens with medium breaks
text = text.replace('\n','<break/>')
text = text.replace('--','<break/>')
text = text.replace('-–','<break/>')
text = text.replace('–-','<break/>')
# Preview text
print(text)

voice = 'Matthew' # US English Male
#voice = 'Justin' # US English Male (Young)
#voice = 'Joey' # US English Male

response = polly.synthesize_speech(
        Text=text,
        TextType="ssml",
        OutputFormat="mp3",
        VoiceId=voice)

# Save to MP3
file = open('text-to-speech-obama.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

