import boto3

demo_name = 'translate-obama'

# 2010 State of the Union
# https://www.nytimes.com/2010/01/28/us/politics/28obama.text.html
transcript_filename = demo_name+'.txt'
with open(transcript_filename, 'r') as transcript_file:
    transcript_text=transcript_file.read()

source='en' # English
#target='de' # German
target='es' # Spanish

translate = boto3.client(service_name='translate', region_name='us-east-1')
result = translate.translate_text(Text=transcript_text, 
            SourceLanguageCode=source, TargetLanguageCode=target)
translated_text = result.get('TranslatedText')
print('SourceText: ' + transcript_text)
print('TranslatedText: ' + translated_text)
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

output_filename = demo_name+'-'+target+'.txt'
with open(output_filename, 'w') as text_file:
    print("{}".format(translated_text), file=text_file)

