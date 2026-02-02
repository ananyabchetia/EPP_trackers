# EPP Trackers

A [tracker](https://ananyabchetia.github.io/EPP_trackers/) that collects and displays the dates on which universities and other institutions were the subject of complaints filed by the Equal Protection Project (EPP).

## Project Overview

This project aggregates and updates a dataset of higher education institutions that the Equal Protection Project has filed civil rights complaints against, including the dates the complaints were filed. The tracker updates automatically every two weeks so readers and researchers can see the most recent filings at a glance.

The Equal Protection Project is a legal initiative that has filed complaints with government civil rights offices against colleges and universities alleging discrimination in scholarship or program eligibility based on race, nationality, or other protected classes.

## Live Demo

Visit the interactive tracker here:
https://ananyabchetia.github.io/EPP_trackers/

## File Structure

Data folder — cleaned and structured complaint data that updates every two weeks.

Jupyter notebook (EPP scrape.ipynb) — for scraping and preprocessing complaint data

Python scraper (scraper.py) — pulls complaint details from public sources

Static site (index.html) — displays the tracker live

Images and assets — visual elements used on the tracker site

## How It Works

The scraper collects public complaint entries filed by the Equal Protection Project.

Data is cleaned and structured into a consistent list of universities and complaint dates. The site reads this data and displays:

    a. Institution name

    b. Date complaint was filed

    c. Link to the original complaint source

The tracker refreshes every two weeks to include new filings.

## Tech Stack

Python (scraping and data processing)

Jupyter Notebook

HTML / JavaScript (for UI display)

GitHub Pages (for hosting the live tracker)

## Purpose of the tracker

This tracker helps journalists, researchers and the public monitor legally significant actions taken by a conservative nonprofit against educational institutions. It makes transparent when and where EPP complaints were filed. My hope is this tool is valuable for reporting and research.

## How to Explore

1. Open the live site listed above.

2. Click View All Complaints to see the full list.

3. Use the dates and complaint links to dive deeper into primary sources.

## Development

To run or modify the scraper locally:

Clone the repository

git clone https://github.com/ananyabchetia/EPP_trackers.git

### Install dependencies (e.g., pandas, requests)

Run the scraper or notebook to update data

(Note: The live demo is hosted via GitHub Pages and updates automatically; running locally isn’t required to view the tracker.)

## Goals

Add geographic context to each university by integrating a university API to include city and state information. This will allow users to search by state, rather than only by institution name, improving search flexibility and usability.

## Questions

If you have questions about the logic or how this project was built, feel free to contact me at ananyabchetia@gmail.com.
