# mylingua GPU API

## general info

to start server:
```bash
python runserver.py
```

Note that only one IP is allowed to make API calls. To change this, edit `PYTHONANYWHERE_IP` in `.env`.

## Endpoints

### /ner
example usage:
```python
import requests

url = 'http://[SERVER_IP]:[SERVER_PUBLIC_PORT]/ner'
data = {
    "1": "第一篇文章的文本",
    "2": "第二篇文章的文本",
    "3": "第三篇文章的文本"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("NER Tags:", response.json())
else:
    print("Error:", response.text)
```
should return:
```bash
>>> NER Tags: {'1': {'第一': 'ORDINAL'}, '2': {'第二': 'ORDINAL'}, '3': {'第三': 'ORDINAL'}}
```