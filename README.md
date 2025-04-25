🕷️ Product Data Scraper with Scrapy
This is a powerful and flexible web scraping project built using the Scrapy framework. It automates the extraction of product information from dynamic websites, providing structured data ideal for analysis, price tracking, and more.

🚀 Features
Fast Crawling with Scrapy’s asynchronous architecture

Product Information Extraction:

🏷️ Title

💰 Price

🟢 Stock Status

🧾 Description

🎮 Platform / Category

Export to CSV: Collected data is saved automatically in a clean, ready-to-use .csv format

Easily Customizable: Quickly adjust selectors to target any e-commerce site layout

Error Handling: Robust against missing fields or unreachable pages

📁 Project Structure
bash
Copy
Edit
/your-scrapy-project
│
├── scraper/              # Scrapy spider code
│   ├── spiders/
│   │   └── products_spider.py
│   └── items.py
│   └── pipelines.py
│   └── settings.py
│
├── products_data.csv     # Output file
├── requirements.txt      # Required Python packages
└── README.md             # This file
🔧 How to Run
bash
Copy
Edit
# Install required packages
pip install -r requirements.txt

# Run the spider
scrapy crawl products -o products_data.csv
