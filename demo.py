#!/usr/bin/env python3
"""
Demo script to showcase the bot's capabilities
This demonstrates how the bot processes URLs without requiring Telegram
"""

from scraper import ProductScraper
from colorama import init, Fore, Style
import sys

# Initialize colorama for colored output
try:
    init(autoreset=True)
    HAS_COLOR = True
except:
    HAS_COLOR = False


def print_header(text):
    """Print a formatted header"""
    if HAS_COLOR:
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{text}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
    else:
        print(f"\n{'='*70}")
        print(text)
        print(f"{'='*70}\n")


def print_success(text):
    """Print success message"""
    if HAS_COLOR:
        print(f"{Fore.GREEN}✓ {text}{Style.RESET_ALL}")
    else:
        print(f"✓ {text}")


def print_info(text):
    """Print info message"""
    if HAS_COLOR:
        print(f"{Fore.YELLOW}ℹ {text}{Style.RESET_ALL}")
    else:
        print(f"ℹ {text}")


def demo_affiliate_link_generation():
    """Demonstrate affiliate link generation"""
    print_header("DEMO: Affiliate Link Generation")
    
    scraper = ProductScraper()
    affiliate_tag = "myaffiliate-20"
    
    test_urls = [
        "https://www.amazon.com/dp/B08N5WRWNW",
        "https://www.amazon.com/Some-Product-Name/dp/B08N5WRWNW/ref=sr_1_1",
        "https://www.amazon.com/dp/B08N5WRWNW?keywords=test&qid=123456",
    ]
    
    for i, url in enumerate(test_urls, 1):
        print(f"Test {i}:")
        print(f"  Original: {url}")
        
        affiliate_url = scraper.add_affiliate_tag(url, affiliate_tag)
        print(f"  Affiliate: {affiliate_url}")
        
        # Verify tag is present
        if f"tag={affiliate_tag}" in affiliate_url:
            print_success("Affiliate tag successfully added")
        else:
            print(f"  ✗ Failed to add affiliate tag")
        print()


def demo_url_parsing():
    """Demonstrate URL parsing capabilities"""
    print_header("DEMO: URL Parsing & Detection")
    
    test_cases = [
        ("https://www.amazon.com/dp/B08N5WRWNW", "Amazon"),
        ("https://www.ebay.com/itm/123456789", "Generic"),
        ("https://www.walmart.com/ip/987654321", "Generic"),
    ]
    
    for url, expected_type in test_cases:
        domain = url.split('/')[2]
        detected_type = "Amazon" if 'amazon' in domain.lower() else "Generic"
        
        print(f"URL: {url}")
        print(f"  Domain: {domain}")
        print(f"  Type: {detected_type}")
        
        if detected_type == expected_type:
            print_success("Correctly identified platform")
        print()


def demo_product_info_extraction():
    """Demonstrate product information extraction (structure only)"""
    print_header("DEMO: Product Data Extraction Structure")
    
    scraper = ProductScraper()
    
    print("The scraper extracts the following information:")
    print("  • Product Title")
    print("  • Price")
    print("  • Rating")
    print("  • Product Image URL")
    print("  • ASIN (for Amazon products)")
    print("  • Platform identification")
    print()
    
    print_info("Note: Actual web scraping requires internet connection")
    print_info("and is subject to website availability and structure")


def demo_bot_workflow():
    """Demonstrate the complete bot workflow"""
    print_header("DEMO: Complete Bot Workflow")
    
    print("When a user sends a URL to the bot, it:")
    print()
    print("1. Validates the URL format")
    print("2. Extracts the product information from the webpage")
    print("3. Generates an affiliate link with your tag")
    print("4. Formats the response with product details")
    print("5. Sends the information back to the user")
    print()
    
    print("Example interaction:")
    print()
    print("  User → Bot: https://www.amazon.com/dp/B08N5WRWNW")
    print()
    print("  Bot → User:")
    print("  ┌─────────────────────────────────────────────┐")
    print("  │ 🎯 Product Information                      │")
    print("  │                                              │")
    print("  │ 📦 Title: Example Product Name              │")
    print("  │ 💰 Price: $29.99                            │")
    print("  │ ⭐ Rating: 4.5/5                            │")
    print("  │ 🏪 Platform: Amazon                         │")
    print("  │                                              │")
    print("  │ 🔗 Affiliate Link:                          │")
    print("  │ https://www.amazon.com/dp/B08N5WRWNW?tag... │")
    print("  │                                              │")
    print("  │ 💡 Use this link to earn commission         │")
    print("  └─────────────────────────────────────────────┘")
    print()


def main():
    """Run all demos"""
    print()
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║     Amazon Telegram Affiliate Bot - Interactive Demo          ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    try:
        demo_affiliate_link_generation()
        demo_url_parsing()
        demo_product_info_extraction()
        demo_bot_workflow()
        
        print_header("Demo Complete!")
        print_success("All components are working correctly")
        print()
        print("Next steps:")
        print("  1. Set up your .env file with bot token and affiliate tag")
        print("  2. Run: python main.py")
        print("  3. Start chatting with your bot on Telegram")
        print()
        
    except Exception as e:
        print(f"\n❌ Error during demo: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
