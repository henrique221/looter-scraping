from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from app import app
from utils import response, dateFormatter
from services import newsFromIGN

@app.route('/api/news/', methods=['GET'])
def news():
    try:
        parameter =  request.args.get('parameter', 'game')
        resultIGN = newsFromIGN.searchNews(parameter)

        list = {"news": []}

        for i in range(0, len(resultIGN)):
            print(resultIGN[i])
            list["news"].append(resultIGN[i])

        return response.response(list)
        

    except Exception as e:
        return str(e)
