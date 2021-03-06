import requests

def main():
    send_line_notify('\n*限目授業の開始です\n教室は***です')

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    f = open("./linetoken.txt","r")
    line_notify_token = f.read()
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()