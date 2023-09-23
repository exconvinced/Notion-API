import requests
import json
import os
from dotenv import load_dotenv

# Notion API Reference
# https://developers.notion.com/reference/intro

load_dotenv()
NOTION_INTEGRATION_TOKEN = os.getenv('NOTION_INTEGRATION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')


headers = {
    'Authorization': 'Bearer ' + NOTION_INTEGRATION_TOKEN,
    'Content_Type': 'application/json',
    'Notion-Version': '2022-06-28'
}


def get_pages():
    url = f'https://api.notion.com/v1/databases/{DATABASE_ID}/query'
    payload = {'page_size': 100}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return data['results']


def create_page(requirements):
    title, author, img, url, select, channel, download = requirements
    data = {
        'Name': {'title': [{'text': {'content': title}}]},
        "Author": {"rich_text": [{"type": "text", "text": {"content": author, "link": {"url": channel}}}]},
        "Files & media": {"files": [{"name": title, "type": "external", "external": {"url": img}}]},
        "URL": {"url": url},
        'Category': {'select': {'name': select}},
        # "Author": {"rich_text": [{"text": {"content": author}, "href": channel}]},
        # 'Multi-select': {'multi_select': [{'name': multi_select}]},
        # 'Text': {'rich_text': [{'text': {'content': text}}]},
        # 'Number': {"number": number},
        # 'Select': {'select': {'name': select}},
        # 'Status': {'status': {'name': status}},
    }
    if channel == None:
        data['Author'] = {"rich_text": [{"type": "text", "text": {"content": author}}]}
    if download != None:
        data["Download"] = {"url": download}
    # print(data)
    return data


def upload_page(data: dict):
    create_url = f'https://api.notion.com/v1/pages'
    payload = {'parent': {'database_id': DATABASE_ID}, 'properties': data}
    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res


def delete_page(page_id: str, data: dict):
    url = f'https://api.notion.com/v1/pages/{page_id}'
    payload = {'archived': True}
    res = requests.patch(url, json=payload, headers=headers)
    print(res.status_code)
    return res
