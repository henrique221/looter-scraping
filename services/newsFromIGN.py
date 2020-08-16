from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from utils import response, dateFormatter


def searchNews(parameter):
    urlIGN = "https://br.ign.com/se/?model=article%2Cvideo&order_by=-date&q=" + parameter
    page = requests.get(urlIGN)
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.get_text()
    text.encode('utf-8')

    headNewsIGN = soup.find_all(class_='m')

    list = []
    
    for i in range(0, len(headNewsIGN)):

        list.append(
            {
            'title': headNewsIGN[i].parent.h3.text,
            'link': str(headNewsIGN[i].parent.h3.a.get('href')),
            'text': str(headNewsIGN[i].parent.p.text)
            }
        )
    return list
