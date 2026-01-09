from src.amazon_page import AmazonPage
from src.excel_handler import read_cocoblu_asins, write_output
from src.utils import today
from src.extractors.asin import extract_asin_info
from src.extractors.price import extract_price
from src.extractors.availability import extract_availability
import time
from src.extractors.ratings import extract_total_ratings
from src.extractors.star_rating import extract_star_rating

def run_cocoblu_bot():
    asins = read_cocoblu_asins()
    rows = []

    amazon = AmazonPage(headless=False)

    for asin in asins:
        print(f"Opening ASIN: {asin}")

        row = {
            "Date": today(),
            "ASIN": asin,
            "Ratings": "",
            "Total Ratings": "",
            "Availability": "",
            "Price": "",
            "Seller Name": "",
            "ASIN Search": "NO",
            "ASIN Reflect": ""
        }

        opened = amazon.open_product(asin)
        print("Page opened:", opened)

        if opened:
            print(">>> CALLING extract_asin_info() <<<")
            asin_search, asin_reflect = extract_asin_info(amazon.page, asin)
            print("Extractor returned:", asin_search, asin_reflect)

            row["ASIN Search"] = asin_search
            row["ASIN Reflect"] = asin_reflect

            if asin_search == "YES":
                availability = extract_availability(amazon.page)
                row["Availability"] = availability

                if "stock" in availability.lower() and "unavailable" not in availability.lower():
                    price = extract_price(amazon.page)
                    print("Price extracted:", price)
                    row["Price"] = price
                else:
                    row["Price"] = ""

                # ✅ TOTAL RATINGS
                total_ratings = extract_total_ratings(amazon.page)
                print("Total ratings extracted:", total_ratings)
                row["Total Ratings"] = total_ratings
                
                # ⭐ STAR RATING
                star_rating = extract_star_rating(amazon.page)
                print("Star rating extracted:", star_rating)
                row["Ratings"] = star_rating

                row["Seller Name"] = ""

            else:
                row["Availability"] = "Not Available"
                row["Price"] = ""
                row["Total Ratings"] = ""
                row["Ratings"] = ""
                row["Seller Name"] = ""

        else:
            print("Page did not open")
            row["Availability"] = "Not Available"
            row["Price"] = ""
            row["Total Ratings"] = ""
            row["Ratings"] = ""
            row["Seller Name"] = ""


        rows.append(row)
        print("Row appended\n")

        # ⏳ Delay to avoid Amazon blocking
        time.sleep(2)

    amazon.close()
    write_output(rows, "ccb-1ii")

if __name__ == "__main__":
    run_cocoblu_bot()
