from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


# 🔥 Convert rating text → number
def convert_rating(rating_text):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return rating_map.get(rating_text, 0)


def scrape_books():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    base_url = "http://books.toscrape.com/"
    driver.get(base_url)
    time.sleep(2)

    books = driver.find_elements(By.CLASS_NAME, "product_pod")

    data = []

    for book in books:
        try:
            title = book.find_element(By.TAG_NAME, "h3").text

            rating_class = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
            rating_text = rating_class.replace("star-rating", "").strip()
            rating = convert_rating(rating_text)

            link = book.find_element(By.TAG_NAME, "a").get_attribute("href")

            # 🔥 Open detail page
            driver.get(link)
            time.sleep(1)

            try:
                description = driver.find_element(By.ID, "product_description") \
                                   .find_element(By.XPATH, "following-sibling::p").text
            except:
                description = "No description available"

            data.append({
                "title": title,
                "author": "Unknown",
                "description": description,
                "rating": rating,
                "reviews_count": 0,
                "book_url": link
            })

            print(f"Scraped: {title}")

            driver.back()
            time.sleep(1)

        except Exception as e:
            print(f"Error: {e}")
            continue

    driver.quit()
    return data


if __name__ == "__main__":
    books = scrape_books()

    for b in books:
        print(b)