# Stealth Web Crawler

This project is a web crawler designed to automatically scrape data from websites while leaving minimal traces. It uses the Scrapy framework to handle crawling, link extraction, and anonymous crawling techniques like random user agents, proxy rotation, and rate limiting.

## Purpose:

### The Stealth Web Crawler is designed for various data gathering purposes, including but not limited to:

•	Data Collection for Machine Learning: Gather large datasets for training and testing machine learning models, particularly for natural language processing (NLP) applications.
•	Market Research: Collect data from competitor websites or various market segments for analysis and reporting.
•	Content Aggregation: Aggregate content from different sources for comparison or to provide a consolidated view of information on a   specific topic.
•	Web Archiving: Preserve snapshots of web pages for research or historical purposes.

### Features

•	Automated Web Crawling: Crawls websites starting from seed URLs and follows links recursively.
•	Link Extraction: Automatically extracts and follows all links from crawled pages.
•	Stealth Techniques:
•	Randomized user-agent strings to mimic real browsers.
•	Delay between requests to avoid overloading websites.
•	Proxy rotation for anonymity and to avoid IP blocking.
•	Data Collection: Collects paragraphs of text from web pages and saves them to a JSON file.
•	Respectful Crawling: Respects rate limits and delay rules to avoid detection.

## Installation:

### Prerequisites

•	Python 3.7 or higher
•	Pip
•	Virtual environment (recommended)

### Steps:

1.	Clone the repository:

        git clone https://github.com/your-username/stealth_crawler.git

  	    cd stealth_crawler


2. Create a virtual environment:

         python -m venv venv

         source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install dependencies:

       pip install -r requirements.txt

4. Install Scrapy and other dependencies:

       pip install scrapy scrapy-user-agents scrapy-rotating-proxies


## Usage:

1.	To start the crawler, navigate to the root directory of the project and run:

         scrapy crawl all_sites

2. To save the scraped data into a JSON file:

       scrapy crawl all_sites -o output.json
  

## Crawler Settings

•	Randomized User-Agent: The crawler uses randomized user-agent strings to simulate different browsers and prevent detection.
•	Request Delay: A delay is added between requests (1-3 seconds) to avoid overloading the target servers.
•	AutoThrottle: The auto-throttle feature is enabled to slow down crawling if the server’s load is detected to be high.
•	Proxy Rotation: The crawler uses rotating proxies to hide the IP address and prevent IP blocking.

### Ethical and Legal Considerations

#### This crawler respects ethical web scraping practices:

•	Respect robots.txt: Always check and respect the robots.txt file of websites.
•	Avoid scraping sensitive data: Do not scrape private or copyrighted content.
•	Use rate-limiting: Avoid sending too many requests in a short period to prevent overloading the server.

#### Customization

•	Starting URLs: To change the initial seed URLs, edit the start_urls list in the all_sites.py spider file.
•	Data to Extract: Modify the parse_item function in all_sites.py to extract different types of content (e.g., images, links, etc.).
•	Proxy Setup: Update the proxy settings in settings.py to use your own proxy service.


    
