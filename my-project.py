import bs4, requests
from openpyxl import Workbook, load_workbook

# total, tee to green, approach, around the green, putting
sg_urls = ['https://www.pgatour.com/stats/stat.02675.html',
'https://www.pgatour.com/stats/stat.02674.html',
'https://www.pgatour.com/stats/stat.02568.html',
'https://www.pgatour.com/stats/stat.02569.html',
'https://www.pgatour.com/stats/stat.02564.html'
]

wb = Workbook()
wb = load_workbook('pga.xlsx')
sheets = wb.sheetnames
sheet_num = 0

for url in sg_urls:
    data = []
    res = requests.get(url)
    res.raise_for_status()
    urlSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    table = urlSoup.find('table', {'id': 'statsTable'})

    table_head = table.find('thead')
    headers = table_head.find_all('th')
    header_vals = [ele.text.strip() for ele in headers]
    sheet_name = sheets[sheet_num]
    sheet = wb[sheet_name]
    sheet.append(header_vals)

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        sheet.append(cols)
    sheet_num += 1

wb.save('pga.xlsx')
        

    