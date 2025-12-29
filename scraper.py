import asyncio
import requests
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import os

# Get the folder where scraper.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Make sure the data folder exists inside the repo
os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://equalprotect.org/case/")
        
        # Click "Load More" until all content is loaded
        while True:
            try:
                load_more = page.locator("#cpt-load-more")
                await load_more.wait_for(state="visible", timeout=5000)
                await load_more.click()
                await asyncio.sleep(1)
            except:
                print("All content loaded!")
                break
        
        full_html = await page.content()
        await browser.close()
    
    # Parse main page HTML
    soup = BeautifulSoup(full_html, "html.parser")
    links = soup.find_all("a", class_="text-xl font-semibold black-st hover:blue-st")
    
    case_data = []
    
    for link in links:
        href = link.get("href")
        full_text = link.get_text(strip=True)
        
        if "v." in full_text:
            university_name = full_text.split("v.")[-1].strip()
        else:
            university_name = full_text
        
        # Request the individual case page to get the date
        response = requests.get(href)
        soup_doc = BeautifulSoup(response.text, "html.parser")
        try:
            date = soup_doc.find_all("p", class_="pb-[25px] text-black-st")[1].get_text(strip=True)
        except IndexError:
            date = "N/A"
        
        case_data.append({
            "Complaint": university_name,
            "Link": href,
            "Date of Complaint": date
        })
    
    df = pd.DataFrame(case_data)
    df.to_csv(os.path.join(BASE_DIR, "data", "complaints.csv"), index=False)
    print("Scraping complete! CSV saved to data/complaints.csv")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
