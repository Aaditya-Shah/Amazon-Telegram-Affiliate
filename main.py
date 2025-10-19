"""
Amazon Telegram Affiliate Bot
Main application entry point
"""

import os
from dotenv import load_dotenv
from bot import AffiliateBot


def main():
    """Main function to run the bot"""
    # Load environment variables
    load_dotenv()
    
    # Get configuration from environment variables
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    affiliate_tag = os.getenv('AFFILIATE_TAG')
    
    # Validate configuration
    if not telegram_token:
        print("❌ Error: TELEGRAM_BOT_TOKEN not found in environment variables")
        print("Please create a .env file with your bot token")
        print("See .env.example for reference")
        return
    
    if not affiliate_tag:
        print("❌ Error: AFFILIATE_TAG not found in environment variables")
        print("Please add your affiliate tag to the .env file")
        print("See .env.example for reference")
        return
    
    # Create and run the bot
    try:
        bot = AffiliateBot(telegram_token, affiliate_tag)
        bot.run()
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error running bot: {str(e)}")


if __name__ == "__main__":
    main()
