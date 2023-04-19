import requests  #URL 요청을 보내는 모듈 
import json #클라이언트 서버가 통신하는 규율, 규격


def send_slack_message():
    bot_url = 'https://hooks.slack.com/services/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'
    payload = {
        'text': '여기에 메시지를 입력하시면 됩니다.'
    }
    requests.post(
        bot_url,
        data=json.dumps(payload),
        headers={'content-Type': 'application/json'}
    )
    
    print(response)


send_slack_message()







# def hello(event, context):
#     slack_hooks_url = "https://hooks.slack.com/services/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"

#     payload = {"text":"Hello, World!"}
#     headers = {'Content-type': 'application/json'}
#     response = requests.post(slack_hooks_url, data=json.dumps(payload), headers=headers)
#     print(response)