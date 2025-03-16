import os
import sys

"""Add path to helpers/ and steps/"""
sys.path.append(os.path.abspath(__file__))

class WebDriverHelper:
    def __init__(self, driver):
        self.driver = driver