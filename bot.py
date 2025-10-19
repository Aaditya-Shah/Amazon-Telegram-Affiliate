"""
Telegram Bot Module
Handles all Telegram bot interactions
"""

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from scraper import ProductScraper
import os
import re


class AffiliateBot:
    """Telegram bot for affiliate link generation"""
    
    def __init__(self, token, affiliate_tag):
        """
        Initialize the bot
        
        Args:
            token (str): Telegram bot token
            affiliate_tag (str): Affiliate tag for links
        """
        self.token = token
        self.affiliate_tag = affiliate_tag
        self.scraper = ProductScraper()
        self.application = None
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        welcome_message = """
🤖 *Welcome to Amazon Affiliate Bot!*

I can help you create affiliate links and extract product information from e-commerce websites.

*How to use:*
📌 Simply send me a product URL (Amazon or other e-commerce sites)
📌 I'll extract product details and provide an affiliate link

*Commands:*
/start - Show this welcome message
/help - Get help information
/about - Learn more about this bot

Just paste any product URL to get started! 🛍️
        """
        await update.message.reply_text(
            welcome_message,
            parse_mode='Markdown'
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_message = """
📖 *Help & Instructions*

*Supported Platforms:*
• Amazon (primary support)
• Other e-commerce sites (basic support)

*How to use:*
1️⃣ Copy a product URL from any e-commerce site
2️⃣ Send it to me
3️⃣ Get product details and affiliate link

*Example:*
Send: `https://www.amazon.com/dp/B08N5WRWNW`
Get: Product info + affiliate link

*Tips:*
✅ Make sure the URL is valid
✅ URL should start with http:// or https://
✅ Works best with Amazon links

Need more help? Contact the bot admin.
        """
        await update.message.reply_text(
            help_message,
            parse_mode='Markdown'
        )
    
    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /about command"""
        about_message = """
ℹ️ *About This Bot*

This is an automated affiliate marketing bot that:
• Extracts product information from URLs
• Generates affiliate links automatically
• Provides product details instantly

*Technology:*
Built with Python using:
• python-telegram-bot
• BeautifulSoup4
• Requests

*License:* GPL-3.0
*GitHub:* Aaditya-Shah/Amazon-Telegram-Affiliate

Made with ❤️ for affiliate marketers
        """
        await update.message.reply_text(
            about_message,
            parse_mode='Markdown'
        )
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming messages (URLs)"""
        user_message = update.message.text.strip()
        
        # Check if message contains a URL
        url_pattern = r'https?://[^\s]+'
        urls = re.findall(url_pattern, user_message)
        
        if not urls:
            await update.message.reply_text(
                "❌ Please send a valid product URL.\n\n"
                "Example: https://www.amazon.com/dp/B08N5WRWNW\n\n"
                "Use /help for more information."
            )
            return
        
        # Process the first URL found
        url = urls[0]
        
        # Send processing message
        processing_msg = await update.message.reply_text(
            "🔍 Processing your link...\nExtracting product information..."
        )
        
        try:
            # Scrape product information
            product_data = self.scraper.scrape_product(url)
            
            if 'error' in product_data:
                await processing_msg.edit_text(
                    f"❌ {product_data['error']}\n\n"
                    "Please check the URL and try again."
                )
                return
            
            # Generate affiliate link
            affiliate_link = self.scraper.add_affiliate_tag(url, self.affiliate_tag)
            
            # Format response message
            response = self._format_product_response(product_data, affiliate_link)
            
            # Send response
            await processing_msg.edit_text(
                response,
                parse_mode='Markdown',
                disable_web_page_preview=False
            )
            
        except Exception as e:
            await processing_msg.edit_text(
                f"❌ An error occurred: {str(e)}\n\n"
                "Please try again or use a different URL."
            )
    
    def _format_product_response(self, product_data, affiliate_link):
        """Format product data into a nice message"""
        response = "🎯 *Product Information*\n\n"
        
        if 'title' in product_data:
            # Truncate title if too long
            title = product_data['title']
            if len(title) > 100:
                title = title[:97] + '...'
            response += f"📦 *Title:* {title}\n\n"
        
        if 'price' in product_data:
            response += f"💰 *Price:* {product_data['price']}\n\n"
        
        if 'rating' in product_data:
            response += f"⭐ *Rating:* {product_data['rating']}/5\n\n"
        
        if 'platform' in product_data:
            response += f"🏪 *Platform:* {product_data['platform']}\n\n"
        
        response += "🔗 *Affiliate Link:*\n"
        response += f"`{affiliate_link}`\n\n"
        response += "👆 Click to copy the link!\n\n"
        response += "💡 _Use this link to earn affiliate commission_"
        
        return response
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        print(f'Update {update} caused error {context.error}')
    
    def run(self):
        """Start the bot"""
        # Create application
        self.application = Application.builder().token(self.token).build()
        
        # Add command handlers
        self.application.add_handler(CommandHandler('start', self.start_command))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(CommandHandler('about', self.about_command))
        
        # Add message handler for URLs
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
        )
        
        # Add error handler
        self.application.add_error_handler(self.error_handler)
        
        # Start the bot
        print("🤖 Bot is starting...")
        print(f"✅ Affiliate tag: {self.affiliate_tag}")
        print("🚀 Bot is running! Press Ctrl+C to stop.")
        
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
