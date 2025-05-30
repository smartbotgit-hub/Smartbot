#!/bin/bash
# SmartBot Pro Install Script

echo "🚀 بدء تثبيت البوت..."
apt update && apt install -y python3
echo "✅ تثبيت Python تم"

echo "📁 إنشاء مجلد smartbot"
mkdir -p /root/smartbot
cp smartbot.py /root/smartbot/

echo "✅ تم التثبيت بنجاح. لتشغيل البوت:"
echo "cd /root/smartbot && python3 smartbot.py"
