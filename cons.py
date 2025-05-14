import os
cookie = {
    "name":"access_token",
    "value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZTQzNGZmZTI1N2Q3NWQ3MTVkNTFjMiIsImlhdCI6MTc0Mzc3MzY0Nn0.1Bqn3ClrYsIIwBG4Z6czs-Kbb4KqYfa6tw4i4s3_4As",
    "domain":"nextjs-typescript.onrender.com",
    "path": "/",
    "httpOnly": True,
    "secure": True,
    "sameSite": "None",
    
}
cookieN = {
    "name":"access_token",
    "value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZjAyZGE1OGM0NGNhNzNlNThiMTE1YyIsImlhdCI6MTc0Mzc5MzU4Mn0.C7dvKxdYjD1AnrSjRE-Bku0QGg0DYzrVf-tYJt09ZSo",
    "domain":"nextjs-typescript.onrender.com",
    "path": "/",
    "httpOnly": True,
    "secure": True,
    "sameSite": "None",
}
url = os.getenv("SELENIUM_HOST")
def check_selenium_host():
    if url:
        print(f"Selenium Host is: {url}")
    else:
        print("SELENIUM_HOST is not set!")