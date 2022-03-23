import json
from nturl2path import url2pathname
import requests

def SEO(website: str):
  url: str ="https://www.semrush.com/on-page-seo-checker/"
  
  find = requests.get(url)
  data = json.loads(find.text)

  site_health = data["Site Health"]
  pages_crawled = data["Pages Crawled"]

  print("Site Health: {}".format(site_health))
  print("Pages Crawled: {}".format(pages_crawled))


if __name__=="__main__":
  SEO("https://www.facebook.com/")