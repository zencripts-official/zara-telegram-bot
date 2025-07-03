# 🤖 Zara AI – Gemini-Powered Telegram Bot

## Features
- Gemini AI replies
- Memory per user using SQLite
- Telegram integration
- `/start` and `/forget` commands

## Setup

### 1. Clone the project
```bash
git clone https://github.com/yourusername/zara-telegram-bot.git
cd zara-telegram-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your keys
Copy `.env.example` to `.env` and add your `BOT_TOKEN` and `GEMINI_API_KEY`.

### 4. Run locally
```bash
python main.py
```

### 5. Deploy on Render
- Connect GitHub repo
- Add Environment Variables:
  - `BOT_TOKEN`
  - `GEMINI_API_KEY`
- Start command: `python main.py`
