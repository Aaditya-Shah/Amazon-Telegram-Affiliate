# Quick Start Guide 🚀

This guide will help you get the Amazon Telegram Affiliate Bot up and running in minutes.

## Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- python-telegram-bot (for Telegram API)
- requests (for HTTP requests)
- beautifulsoup4 (for web scraping)
- lxml (for parsing HTML)
- python-dotenv (for environment variables)

## Step 2: Get Your Telegram Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` to BotFather
3. Choose a name for your bot (e.g., "My Affiliate Bot")
4. Choose a username for your bot (must end with 'bot', e.g., "myaffiliatebot")
5. BotFather will give you a token that looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`
6. Copy this token - you'll need it in the next step

## Step 3: Get Your Affiliate Tag

### For Amazon Associates:
1. Visit [Amazon Associates](https://affiliate-program.amazon.com/)
2. Sign up for an account (if you don't have one)
3. Once approved, find your tracking ID/tag in your account
4. It typically looks like: `yourname-20` or `yourstore-21`

### For Other Platforms:
- Check your affiliate program dashboard for your unique affiliate ID/tag

## Step 4: Configure the Bot

1. Create a `.env` file in the project directory:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your credentials:
   ```env
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
   AFFILIATE_TAG=yourname-20
   ```

   Replace:
   - `123456789:ABCdefGHIjklMNOpqrsTUVwxyz` with your actual bot token
   - `yourname-20` with your actual affiliate tag

## Step 5: Test the Installation

Run the test script to verify everything is set up correctly:

```bash
python test_scraper.py
```

You should see output showing all tests passing ✅

## Step 6: Start the Bot

```bash
python main.py
```

You should see:
```
🤖 Bot is starting...
✅ Affiliate tag: yourname-20
🚀 Bot is running! Press Ctrl+C to stop.
```

## Step 7: Use Your Bot

1. Open Telegram
2. Search for your bot using the username you created
3. Start a chat and send `/start`
4. Try sending an Amazon product URL, for example:
   ```
   https://www.amazon.com/dp/B08N5WRWNW
   ```

5. The bot will respond with:
   - Product title
   - Price
   - Rating
   - An affiliate link with your tag

## Troubleshooting 🔧

### "TELEGRAM_BOT_TOKEN not found"
- Make sure you created a `.env` file (not `.env.example`)
- Check that the token is correctly copied without extra spaces

### "Module not found" errors
- Run: `pip install -r requirements.txt` again
- Make sure you're using Python 3.7 or higher

### Bot doesn't respond
- Check that the bot token is correct
- Make sure the bot is running (you should see "Bot is running!" message)
- Try sending `/start` to wake up the bot

### Affiliate link not working
- Verify your affiliate tag is correct
- Check that you're using a valid product URL
- Make sure the URL starts with `http://` or `https://`

## Advanced Usage 📚

### Running in Background (Linux/Mac)

```bash
nohup python main.py > bot.log 2>&1 &
```

This will run the bot in the background and log output to `bot.log`.

### Running as a Service (Linux with systemd)

Create a service file at `/etc/systemd/system/telegram-affiliate-bot.service`:

```ini
[Unit]
Description=Telegram Affiliate Bot
After=network.target

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/Amazon-Telegram-Affiliate
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable telegram-affiliate-bot
sudo systemctl start telegram-affiliate-bot
```

## Next Steps 🎯

- Share your bot with friends who might be interested
- Monitor your affiliate earnings
- Customize the bot messages in `bot.py`
- Add support for more e-commerce platforms in `scraper.py`

## Need Help? 💬

- Check the main [README.md](README.md) for more detailed information
- Review the code comments in the source files
- Open an issue on GitHub if you encounter problems

Happy affiliate marketing! 🎉
