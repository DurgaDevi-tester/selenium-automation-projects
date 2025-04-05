# Wikipedia Search Automation

This project automates a Wikipedia search using **Selenium WebDriver with Python**. It searches for a specific term, extracts the page title and the first paragraph, and saves the result to a text file.

## 📌 What it does

- Opens [Wikipedia](https://www.wikipedia.org/)
- Searches for the term: `"Python (programming language)"`
- Extracts:
  - Page title
  - First paragraph (ignores any class-based formatting)
- Saves the content into a file called: `wikipedia_search_result.txt`

## 🛠️ Technologies Used

- Python
- Selenium
- Firefox WebDriver (GeckoDriver)

## 🖥️ How it works

1. Uses Selenium to launch Firefox and open Wikipedia.
2. Enters the search term into the search box and submits.
3. Waits briefly for the page to load.
4. Extracts the page title using its HTML ID.
5. Extracts the first paragraph using an XPath that avoids paragraph tags with classes.
6. Writes the result into a `.txt` file.

## 📂 Output Example

```
Page Title: Python (programming language)

First Paragraph:
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
```
