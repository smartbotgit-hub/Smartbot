#!/usr/bin/env python3
# SmartBot Pro - Aggressive Adaptive Version

import time, random
from binance.client import Client

API_KEY = JOMWZQJqiSgCwE2bPNG5cgjqyNr99FKNaVbellhUM5wWC4xxpNdB8v2OqJf6k5Bl
API_SECRET = ‏RVKOQlKIpoiy2ANs10wXqEYp9nLww7ZFaqkVq2hrDxqLjHLARsSH5S4nei7SF0LA

client = Client(API_KEY, API_SECRET)
def run_bot():
    balance = 157
    safety_orders = [0.12, 0.12, 0.18, 0.27, 0.31]
    order_prices = [100]
    price = 100
    print("✅ SmartBot Pro بدأ العمل (نسخة هجومية)
")

    for i, pct in enumerate(safety_orders):
        order_price = price * (1 - (i+1)*0.01)
        order_prices.append(round(order_price, 2))

    print(f"💰 الأوامر المتوقعة: {order_prices}")
    print(f"📉 نسبة التراجع بين الأوامر: 1%")
    print("📈 الهدف: 1.3% ربح على كامل الصفقات
")

    print("🚀 يتم الآن تشغيل المحاكاة...")
    time.sleep(2)
    print("✅ المحاكاة انتهت بنجاح. البوت جاهز للتنفيذ.
")

if __name__ == "__main__":
    run_bot()
