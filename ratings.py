import re

def extract_total_ratings(page):
    """
    Extract total number of ratings / reviews from Amazon DP page.
    Returns digits only (string) or empty string if not found.
    """

    selectors = [
        "#acrCustomerReviewText",   # Most common
        "span[data-hook='total-review-count']"
    ]

    for selector in selectors:
        try:
            loc = page.locator(selector)
            if loc.count():
                text = loc.first.inner_text().lower()

                # Extract digits only
                numbers = re.findall(r"\d+", text.replace(",", ""))
                if numbers:
                    return numbers[0]
        except:
            pass

    return ""
