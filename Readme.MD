# EPP Trackers

A [tracker](https://ananyabchetia.github.io/EPP_trackers/) that collects and displays the dates on which universities and other institutions were the subject of complaints filed by the Equal Protection Project (EPP).

## Project Overview

This project aggregates and updates a dataset of higher education institutions that the Equal Protection Project has filed civil rights complaints against, including the dates the complaints were filed. The tracker updates automatically every two weeks so readers and researchers can see the most recent filings at a glance.

## Live Demo

Visit the interactive tracker here:
https://ananyabchetia.github.io/EPP_trackers/

## File Structure

.github/workflow/scrape_epp.yml - has the Github Actions workflow which runs src/scraper.py automatically on a two-week schedule

data — cleaned and structured complaint data that updates every two weeks

notebook/epp-scraper.ipynb — This is where I initially developed and tested the scraping logic before moving it into scraper.py. I used the Playwright library to scrape

scraper.py — pulls complaint details from public sources

index.html — displays the tracker live

image — visual elements used for the favicon tag

## How It Works

The scraper collects public complaint entries filed by the Equal Protection Project.

Data is cleaned and structured into a consistent list of universities and complaint dates. The site reads this data and displays:

1. Institution name

2. Date complaint was filed

3. Link to the original complaint source

The tracker refreshes every two weeks to include new filings.

## Automation:

A GitHub Actions workflow (.github/workflows/scrape_epp.yml) runs src/scraper.py automatically on a two-week schedule. The workflow:

1. Sets up a Python environment and installs required packages.

2. Runs scraper.py to collect the latest complaint data.

3. Commits and pushes any updated CSVs back to the repository.

This ensures the tracker always has up-to-date complaint entries without manual intervention.

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

## Goals

Add geographic context to each university by integrating a university API to include city and state information. This will allow users to search by state, rather than only by institution name, improving search flexibility and usability.

## Questions

If you have questions about the logic or how this project was built, feel free to contact me at ananyabchetia@gmail.com.
