import os
import pandas as pd
import csv 
import sys

path = "../output/"
csv_list = os.listdir(path)

"""
for csv_elem in csv_list:
   df = pd.read_csv(os.path.join(path, csv_elem))
   df = df[:1]
   df = list(df)
   print(df[0]) # Date
   print(df[1]) # Category
   print(df[2]) # Publisher
   print(df[3]) # Title
   print(df[4]) # Article 
   print(df[5]) # url
"""

def make_title_and_article():
   _dict = {'title': [], 'article': []}
   for i, csv_elem in enumerate(csv_list):
      print(f"** working on {i+1}/{len(csv_list)}")
      df = pd.read_csv(os.path.join(path, csv_elem), names = ['date', 'category', 'publisher', 'title', 'article', 'url'])
      title = df['title']
      article = df['article']
      _dict['title'] += list(title)
      _dict['article'] += list(article)
      if (len(_dict['title']) != len(_dict['article'])):
         print(f"length of title: {len(_dict['title'])} and length of article: {len(_dict['article'])}")
         sys.exit(-1)      
   _df = pd.DataFrame(_dict)
   _df.to_csv('title_and_article.csv')

def print_sample():
   df = pd.read_csv('./title_and_article.csv')
   print(len(df['title']))
   print(len(df['article']))

   sample_title = df['title'][:10]
   sample_article = df['article'][:10]

   for _title, _article in zip(sample_title, sample_article):
      print(f"title: {_title}\narticle: {_article[:100]}")
      print("="*20)

if __name__ == "__main__":
   print_sample()
