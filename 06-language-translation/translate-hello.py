import boto3

text='Hello, World'
source='en' # English
#target='de' # German
target='es' # Spanish

translate = boto3.client(service_name='translate', region_name='us-east-1')
result = translate.translate_text(Text=text, 
            SourceLanguageCode=source, TargetLanguageCode=target)
print('SourceText: ' + text)
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

