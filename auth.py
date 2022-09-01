import pytumblr
import os

def login():
  try:
    client = pytumblr.TumblrRestClient(
      os.getenv('OAUTH_CONSUMER_KEY'),
      os.getenv('OAUTH_CONSUMER_SECRET'),
      os.getenv('OAUTH_TOKEN'),
      os.getenv('OAUTH_SECRET'),
    )
  except:
    print("Exception thrown during authentication.")

  return client
