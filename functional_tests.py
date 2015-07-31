# -*- coding: utf-8 -*-
"""
From TDD with Python Chapter 1
Created on Fri Jul 31 11:48:53 2015

@author: amaloney
"""

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
