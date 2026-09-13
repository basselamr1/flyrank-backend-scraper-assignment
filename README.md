# Books to Scrape — Scraping Target Classification

## Overview

This project is a web-scraping exercise targeting **Books to Scrape**, a fictional bookstore website specifically designed as a sandbox for practicing web scraping.

The target is hosted at:

`https://books.toscrape.com/`

The parent ToScrape website describes Books to Scrape as a fictional bookstore that is intended to be scraped and as a safe environment for beginners learning web scraping. The target website also identifies itself as a demo website for web-scraping purposes.

## Target Classification

### Target

**Books to Scrape**

`https://books.toscrape.com/`

### Why this target?

Books to Scrape is explicitly designed as a web-scraping sandbox. It provides a fictional catalog, pagination, and structured book information specifically for scraping practice.

This makes it an appropriate target for an internship scraping exercise without targeting a production website or collecting real commercial data.

### Scope

The scraper will access **only the first 3 catalogue pages**.

With 20 books displayed per page, the maximum scope is approximately **60 book listings**.

The scraper will not continue beyond these three pages.

### Data to collect

For each book, the scraper will collect only publicly displayed catalogue information relevant to the exercise:

* Book title
* Price
* Availability
* Product URL
* Rating

No user accounts, personal information, authentication data, or private information will be collected.

### Robots.txt

The following URL was requested once:

`https://books.toscrape.com/robots.txt`

**Result:** `404 Not Found`

Therefore:

> **no robots file found**

A missing `robots.txt` file is not treated as permission to scrape other websites. In this case, the target is appropriate because Books to Scrape is explicitly provided as a scraping sandbox.

### Why this scope is appropriate

The target is specifically intended for scraping practice, and limiting the exercise to the first three catalogue pages keeps the request volume small and controlled while providing enough data to demonstrate pagination and structured data extraction.

## Responsible Scraping Rule

**I will not reuse this code on another site without checking its rules and terms first.**

## Current Stage

**Stage 0 — Classify scraping target**

The target has been checked and classified before implementing the scraper.
