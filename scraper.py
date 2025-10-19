"""
Product Scraper Module
Extracts product information from URLs
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import re


class ProductScraper:
    """Scraper for extracting product information from e-commerce websites"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def scrape_product(self, url):
        """
        Extract product information from URL
        
        Args:
            url (str): Product URL
            
        Returns:
            dict: Product information including title, price, image, etc.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Detect the website type
            domain = urlparse(url).netloc.lower()
            
            if 'amazon' in domain:
                return self._scrape_amazon(soup, url)
            else:
                # Generic scraper for other sites
                return self._scrape_generic(soup, url)
                
        except Exception as e:
            return {
                'error': f'Failed to scrape product: {str(e)}',
                'url': url
            }
    
    def _scrape_amazon(self, soup, url):
        """Extract product info from Amazon"""
        product_data = {
            'url': url,
            'platform': 'Amazon'
        }
        
        # Extract title
        title_elem = soup.find('span', {'id': 'productTitle'})
        if title_elem:
            product_data['title'] = title_elem.text.strip()
        
        # Extract price
        price_elem = (
            soup.find('span', {'class': 'a-price-whole'}) or
            soup.find('span', {'class': 'a-offscreen'})
        )
        if price_elem:
            product_data['price'] = price_elem.text.strip()
        
        # Extract image
        image_elem = soup.find('img', {'id': 'landingImage'})
        if not image_elem:
            image_elem = soup.find('img', {'class': 'a-dynamic-image'})
        if image_elem and 'src' in image_elem.attrs:
            product_data['image'] = image_elem['src']
        
        # Extract rating
        rating_elem = soup.find('span', {'class': 'a-icon-alt'})
        if rating_elem:
            rating_text = rating_elem.text.strip()
            match = re.search(r'(\d+\.?\d*)\s*out of', rating_text)
            if match:
                product_data['rating'] = match.group(1)
        
        # Extract ASIN
        asin_match = re.search(r'/dp/([A-Z0-9]{10})', url)
        if asin_match:
            product_data['asin'] = asin_match.group(1)
        
        return product_data
    
    def _scrape_generic(self, soup, url):
        """Generic scraper for other e-commerce sites"""
        product_data = {
            'url': url,
            'platform': 'Generic'
        }
        
        # Try to find title using common meta tags
        title = (
            soup.find('meta', {'property': 'og:title'}) or
            soup.find('meta', {'name': 'twitter:title'}) or
            soup.find('h1')
        )
        if title:
            if title.name == 'meta':
                product_data['title'] = title.get('content', '').strip()
            else:
                product_data['title'] = title.text.strip()
        
        # Try to find price using common patterns
        price_elem = soup.find('span', {'class': re.compile(r'price', re.I)})
        if price_elem:
            product_data['price'] = price_elem.text.strip()
        
        # Try to find image
        image = (
            soup.find('meta', {'property': 'og:image'}) or
            soup.find('meta', {'name': 'twitter:image'})
        )
        if image:
            product_data['image'] = image.get('content', '')
        
        return product_data
    
    def add_affiliate_tag(self, url, affiliate_tag):
        """
        Add affiliate tag to product URL
        
        Args:
            url (str): Original product URL
            affiliate_tag (str): Affiliate tag to add
            
        Returns:
            str: URL with affiliate tag
        """
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        
        # For Amazon URLs
        if 'amazon' in parsed_url.netloc.lower():
            query_params['tag'] = [affiliate_tag]
            
            # Clean up the URL
            new_query = urlencode(query_params, doseq=True)
            affiliate_url = urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))
            return affiliate_url
        
        # For other platforms, just append as query parameter
        query_params['ref'] = [affiliate_tag]
        new_query = urlencode(query_params, doseq=True)
        affiliate_url = urlunparse((
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            new_query,
            parsed_url.fragment
        ))
        return affiliate_url
