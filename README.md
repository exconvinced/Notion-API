# Notion-API

<!-- Suppose you are interested in personal development, and you watch lots of motivational videos and read psychology and finance books. With the vast wealth of knowledge on the internet, you must somehow keep track of what you've already finished and what you're about to start. Building a [Notion](https://www.notion.so/) workspace for this purpose is an intuitive approach. Better yet, why not automate the workspace? -->

This project demonstrates streamlined interaction between Python and databases in Notion via [Notion API Integration](https://developers.notion.com/reference/intro).

The Python script ([`main.py`](./main.py)) performs two main functions: extract information from web-scraped data (via [`webcrawler.py`](./webcrawler.py)), and write those information on the Notion database through API authentication via simple request headers (via [`notion.py`](./notion.py)):

```py
headers = {
    'Authorization': 'Bearer ' + NOTION_INTEGRATION_TOKEN,
    'Content_Type': 'application/json',
    'Notion-Version': '2022-06-28'
}
```

<center><h4>Preview</h4></center>

<div align="center">
    <a href="">
        <img width="100%" src="./.preview/notion_api-lanczos-480.gif" alt="image"/>
    </a> 
</div>