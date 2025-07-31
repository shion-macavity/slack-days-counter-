import os
from datetime import datetime
from slack_sdk import WebClient

# Slack Bot TokenをGitHub Secretsから取得
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = "#general"  # 投稿先チャンネル名

client = WebClient(token=SLACK_BOT_TOKEN)

start_date = datetime(2024, 12, 1)  # 開始日を変更
days = (datetime.now() - start_date).days

message = f"2024年12月1日から{days}日目です！"
client.chat_postMessage(channel=CHANNEL_ID, text=message)
print("送信完了")
