#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: run.py
# @Created:   2018-04-17 02:22:09  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-17 02:26:22  Simon Seo (simon.seo@nyu.edu)
import os
from app import app

app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
