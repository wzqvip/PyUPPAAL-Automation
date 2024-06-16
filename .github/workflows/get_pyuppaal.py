import requests

# URL to the form.php script
url = 'https://www2.it.uu.se/research/group/darts/uppaal/download/form.php'

# Headers as seen in the Charles proxy tool
headers = {
    'Host': 'www2.it.uu.se',
    'Connection': 'keep-alive',
    'Content-Length': '176',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www2.it.uu.se',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www2.it.uu.se/research/group/darts/uppaal/download/registration.php?id=0&subid=17',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'PHPSESSID=11eIhn7o9hehdf50sjfeuqqm83; sc_is_visitor_unique=rx641662.1718505897.103E5367DBAF4F54D0389C3E2D89579A.2.2.2.2.2.2.2.2.2.2.2.2'
}

# Data payload, if required (you may need to adjust this based on the actual form data)
payload = {
    'Name': 'Ziqi Wang',
    'JobTitle': 'Student',
    'Company': 'ShanghaiTech University',
    'Street': '',
    'City': '',
    'Country': '',
    'Postcode': '',
    'Email': 'tacoin@foxmail.com',
    'Homepage': '',
    'Telephone': '',
    'Fax': '',
    'Agreement': 'on',
    'id': '0',
    'subid': '17'
}

# Perform a POST request to form.php
response = requests.post(url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a file
    with open('downloaded_file', 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully.')
else:
    print(f'Failed to download file. Status code: {response.status_code}')
