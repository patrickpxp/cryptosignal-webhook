#!/bin/sh
curl -s -X POST https://api.telegram.org/botYOUR_TOKEN/sendMessage -d text="yourMessage" -d chat_id=YOUR_CHAT_ID
