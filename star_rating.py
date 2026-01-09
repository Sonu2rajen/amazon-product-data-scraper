import re

def extract_star_rating(page):
    """
    Extract star rating (e.g. 4.3) from Amazon DP page.
    Returns string like '4.3' or empty string if not found.
    """

    selectors = [
        "span.a-icon-alt",                 # Most common
        "i.a-icon-star span.a-icon-alt"    # Fallback
    ]

    for selector in selectors:
        try:
            loc = page.locator(selector)
            if loc.count():
                text = loc.first.inner_text().lower()
                # Example: "4.3 out of 5 stars"
                match = re.search(r"(\d+(\.\d+)?)\s+out of\s+5", text)
                if match:
                    return match.group(1)
        except:
            pass

    return ""
