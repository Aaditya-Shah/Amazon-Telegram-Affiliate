# Amazon Telegram Affiliate Bot 🤖

A Python-based Telegram bot that extracts product information from e-commerce websites (primarily Amazon) and generates affiliate links automatically.

## Features ✨

- 🔍 **Product Information Extraction**: Automatically scrapes product details including:
  - Product title
  - Price
  - Rating
  - Product images
  - ASIN (for Amazon products)

- 🔗 **Automatic Affiliate Link Generation**: Converts regular product URLs into affiliate links with your tag

- 🌐 **Multi-Platform Support**:
  - Full support for Amazon
  - Basic support for other e-commerce platforms

- 💬 **User-Friendly Telegram Interface**: Simple commands and easy-to-use bot interaction

## Prerequisites 📋

- Python 3.7 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- An affiliate tag (e.g., Amazon Associates tag)

## Installation 🚀

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aaditya-Shah/Amazon-Telegram-Affiliate.git
   cd Amazon-Telegram-Affiliate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your credentials:
     ```env
     TELEGRAM_BOT_TOKEN=your_bot_token_here
     AFFILIATE_TAG=your_affiliate_tag_here
     ```

## Getting Your Credentials 🔑

### Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the token provided by BotFather

### Affiliate Tag

#### For Amazon Associates:
1. Sign up at [Amazon Associates](https://affiliate-program.amazon.com/)
2. Once approved, your affiliate tag will be available in your account
3. It usually looks like: `yourname-20`

## Usage 💡

1. **Start the bot**:
   ```bash
   python main.py
   ```

2. **Open Telegram** and search for your bot (using the username you created with BotFather)

3. **Send commands**:
   - `/start` - Welcome message and instructions
   - `/help` - Detailed help information
   - `/about` - Information about the bot

4. **Send product URLs**:
   - Simply paste any Amazon product URL
   - The bot will extract product information and provide an affiliate link

### Example Usage

```
User: https://www.amazon.com/dp/B08N5WRWNW

Bot: 🎯 Product Information

📦 Title: Example Product Name

💰 Price: $29.99

⭐ Rating: 4.5/5

🏪 Platform: Amazon

🔗 Affiliate Link:
https://www.amazon.com/dp/B08N5WRWNW?tag=yourname-20

👆 Click to copy the link!
```

## Project Structure 📁

```
Amazon-Telegram-Affiliate/
├── main.py           # Main application entry point
├── bot.py            # Telegram bot logic and handlers
├── scraper.py        # Web scraping and data extraction
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
├── .gitignore        # Git ignore rules
├── LICENSE           # GPL-3.0 License
└── README.md         # This file
```

## Features in Detail 🔧

### Web Scraping

The bot uses BeautifulSoup4 to extract product information from web pages:
- Handles Amazon product pages with specific selectors
- Provides generic scraping for other e-commerce sites
- Extracts metadata using Open Graph and Twitter Card tags

### Affiliate Link Generation

- Automatically appends your affiliate tag to product URLs
- Preserves existing URL parameters
- Works with Amazon's affiliate link format

### Error Handling

- Graceful error handling for invalid URLs
- Timeout protection for slow websites
- User-friendly error messages

## Dependencies 📦

- `python-telegram-bot` - Telegram Bot API wrapper
- `requests` - HTTP library for making requests
- `beautifulsoup4` - HTML parsing library
- `lxml` - Fast XML/HTML parser
- `python-dotenv` - Environment variable management

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Disclaimer ⚠️

This bot is for educational purposes. Make sure to:
- Comply with the terms of service of the e-commerce platforms you scrape
- Follow the affiliate program rules and guidelines
- Respect robots.txt and rate limiting
- Not use this for malicious purposes

## License 📄

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Support 💬

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Read the documentation carefully

## Roadmap 🗺️

Future enhancements planned:
- [ ] Support for more e-commerce platforms
- [ ] Product price tracking
- [ ] Deal alerts
- [ ] Database integration for tracking conversions
- [ ] Admin panel for statistics
- [ ] Multi-language support

---

Made with ❤️ for affiliate marketers
