# Contributing to Amazon Telegram Affiliate Bot

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs 🐛

If you find a bug, please open an issue with:
- A clear title and description
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)
- Any relevant logs or screenshots

### Suggesting Enhancements 💡

We welcome suggestions! Please open an issue with:
- A clear description of the enhancement
- Why this would be useful
- Any implementation ideas you have

### Pull Requests 🔧

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages: `git commit -m "Add feature: description"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Amazon-Telegram-Affiliate.git
   cd Amazon-Telegram-Affiliate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file for testing:
   ```bash
   cp .env.example .env
   # Add your test bot token and affiliate tag
   ```

## Code Style Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Comment complex logic

### Example:

```python
def add_affiliate_tag(self, url, affiliate_tag):
    """
    Add affiliate tag to product URL
    
    Args:
        url (str): Original product URL
        affiliate_tag (str): Affiliate tag to add
        
    Returns:
        str: URL with affiliate tag
    """
    # Implementation here
    pass
```

## Testing

Before submitting a PR:

1. Run the test script:
   ```bash
   python test_scraper.py
   ```

2. Test manually with your bot
3. Check for syntax errors:
   ```bash
   python -m py_compile *.py
   ```

## Areas for Contribution

### High Priority
- [ ] Support for more e-commerce platforms (eBay, Walmart, etc.)
- [ ] Error handling improvements
- [ ] Rate limiting for web scraping
- [ ] Unit tests with pytest

### Medium Priority
- [ ] Price tracking feature
- [ ] Deal alerts
- [ ] Database integration
- [ ] Admin statistics dashboard

### Low Priority
- [ ] Multi-language support
- [ ] Custom message templates
- [ ] Analytics integration

## Commit Message Guidelines

- Use present tense: "Add feature" not "Added feature"
- Be descriptive but concise
- Reference issues when relevant: "Fix #123"

Examples:
- ✅ `Add support for eBay product scraping`
- ✅ `Fix price extraction for Amazon.co.uk`
- ✅ `Update README with installation instructions`
- ❌ `fixed stuff`
- ❌ `changes`

## Code Review Process

1. At least one maintainer will review your PR
2. Address any feedback or requested changes
3. Once approved, a maintainer will merge your PR

## Questions?

Feel free to:
- Open an issue for discussion
- Ask questions in PR comments
- Check existing issues/PRs for context

## License

By contributing, you agree that your contributions will be licensed under the GPL-3.0 License.

---

Thank you for contributing! 🎉
