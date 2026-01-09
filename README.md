# Amazon Product Data Scraper (Python + Playwright)

## 📌 Overview
This project is a scalable Amazon product data scraping bot built using Python and Playwright.
It is designed to extract key product-level data from Amazon product detail (DP) pages
using ASINs as input.

The scraper is fault-tolerant, batch-friendly, and suitable for real-world automation use cases.

---

## 🚀 Features
- ASIN Search validation (detects redirected / replaced ASINs)
- ASIN Reflect check (actual ASIN loaded on page)
- Stock availability detection (exact Amazon phrasing)
- Price extraction (only for in-stock products)
- Star rating extraction (e.g. 4.3 / 5)
- Total ratings / reviews count extraction
- Batch processing for 50–100 ASINs per run
- Automatic skip & recovery on page timeouts
- Excel input & output automation
- Human-like delay to avoid blocking

---

## 🛠️ Tech Stack
- Python 3.10+
- Playwright (Chromium)
- Pandas
- OpenPyXL

---

## 📂 Project Structure
├── main.py # Main runner
├── amazon_page.py # Browser & page handling
├── excel_handler.py # Excel input/output
├── utils.py # Helpers
└── extractors/ # Modular extractors
├── asin.py
├── availability.py
├── price.py
├── ratings.py
└── star_rating.py



---

## ⚙️ How It Works
1. Reads ASINs from Excel input
2. Opens Amazon product pages using Playwright
3. Validates ASIN search & redirection
4. Extracts availability, price, ratings & reviews
5. Handles timeouts gracefully
6. Writes structured output to Excel

---

## ▶️ How to Run

### 1. Clone repository
```bash
git clone https://github.com/your-username/amazon-product-data-scraper.git
cd amazon-product-data-scraper
```


### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4. Run scraper
```bash
python -m src.main
```

📊 Example Output
```bash
ASIN	  Availability	Price	Rating	Total Ratings
B0XXXX	In stock	      199    4.3	         1234
B0YYYY	Not Available
```


## ⚠️ Notes
Run in batches (50–100 ASINs recommended)

Avoid running multiple seller ASINs together

Output Excel must be closed before execution

Scraper uses delays to minimize blocking

## 📈 Use Cases
E-commerce price & availability monitoring

Seller performance analysis

Catalog health checks

Market research automation

Internal reporting dashboards


🔐 Disclaimer
This project is for educational and internal automation purposes.
Users are responsible for complying with Amazon’s terms of service.


---

## 4️⃣ requirements.txt (VERY IMPORTANT)

Create `requirements.txt` with:

playwright
pandas
openpyxl



