import requests

url = 'https://www.oag.state.md.us/Press/index.htm'

response = request.get(url)
html = response.content
print html