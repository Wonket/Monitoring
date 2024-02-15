name: Send Telegram Message

on:
   schedule:
   - cron: '5 * */10 * *'
   workflow_dispatch:
    inputs:
      branch:
        description: 'Branch to run the workflow on'
        required: true
        default: 'main'

jobs:
  send-message:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install Dependencies
        run: |
          pip install requests

      - name: Send Telegram Message
        run: |
          TELEGRAM_BOT_TOKEN=$YOUR_TELEGRAM_BOT_TOKEN
          CHAT_ID=$YOUR_CHAT_ID
          MESSAGE="Hello from GitHub Actions on branch ${{ github.event.inputs.branch }}!"

          curl -s -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage \
            -d chat_id=$CHAT_ID \
            -d text="$MESSAGE"
        env:
          YOUR_TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          YOUR_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
