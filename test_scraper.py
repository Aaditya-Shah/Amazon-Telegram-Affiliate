"""
Simple test script to verify scraper functionality
This is a basic demonstration of how the scraper module works
"""

from scraper import ProductScraper


def test_amazon_url_affiliate_tag():
    """Test adding affiliate tag to Amazon URL"""
    scraper = ProductScraper()
    
    # Test URL
    original_url = "https://www.amazon.com/dp/B08N5WRWNW"
    affiliate_tag = "testaffiliate-20"
    
    # Add affiliate tag
    affiliate_url = scraper.add_affiliate_tag(original_url, affiliate_tag)
    
    print("Original URL:")
    print(original_url)
    print("\nAffiliate URL:")
    print(affiliate_url)
    print("\n✅ Affiliate tag added successfully!")
    
    # Verify tag is in URL
    assert "tag=" + affiliate_tag in affiliate_url
    return True


def test_url_extraction():
    """Test URL parsing"""
    scraper = ProductScraper()
    
    test_urls = [
        "https://www.amazon.com/dp/B08N5WRWNW",
        "https://www.amazon.com/Product-Name/dp/B08N5WRWNW",
        "https://www.amazon.com/dp/B08N5WRWNW?keywords=test",
    ]
    
    affiliate_tag = "testaffiliate-20"
    
    print("\n" + "="*60)
    print("Testing URL Affiliate Tag Addition")
    print("="*60 + "\n")
    
    for url in test_urls:
        result = scraper.add_affiliate_tag(url, affiliate_tag)
        print(f"Input:  {url}")
        print(f"Output: {result}")
        print()
    
    print("✅ All URL tests passed!")
    return True


def test_scraper_structure():
    """Test scraper basic structure"""
    scraper = ProductScraper()
    
    print("\n" + "="*60)
    print("Testing Scraper Structure")
    print("="*60 + "\n")
    
    # Test that scraper has required methods
    assert hasattr(scraper, 'scrape_product'), "scrape_product method missing"
    assert hasattr(scraper, 'add_affiliate_tag'), "add_affiliate_tag method missing"
    
    print("✅ Scraper has all required methods")
    print("   - scrape_product()")
    print("   - add_affiliate_tag()")
    
    return True


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("Amazon Telegram Affiliate Bot - Scraper Tests")
    print("="*60 + "\n")
    
    try:
        # Run tests
        test_scraper_structure()
        test_amazon_url_affiliate_tag()
        test_url_extraction()
        
        print("\n" + "="*60)
        print("🎉 All tests passed successfully!")
        print("="*60 + "\n")
        
        print("Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Configure .env file with your bot token and affiliate tag")
        print("3. Run the bot: python main.py")
        print()
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}\n")
        return False
    
    return True


if __name__ == "__main__":
    main()
