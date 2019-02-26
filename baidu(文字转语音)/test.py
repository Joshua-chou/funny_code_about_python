from aip import AipSpeech

APP_ID = '11437325'
API_KEY = 'gmH3vbXQKSk0L2sNDO76umr9'
SECRET_KEY = 'lsOZ74qYIlwFbc6G27zIOHMGNnZBzXKC '

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result  = client.synthesis('沙雕老狗','zh', 1,{
    'spd' : "5",
    'pit' : "5",
    'vol':"5",
    'per':"0",
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    print('a')
    with open('auido.mp3', 'wb') as f:
        f.write(result)