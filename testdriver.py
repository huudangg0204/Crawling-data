import requests
from bs4 import BeautifulSoup
import re

url = 'https://web.archive.org/web/20220324004745/https://www.worldometers.info/coronavirus/#countries'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm bảng với id 'main_table_countries_today'
table = soup.find('table', id='main_table_countries_today')

# Lấy hàng tiêu đề để xác định cột
header_row = table.find('thead').find_all('tr')[0]  # Lấy từ <thead> để chắc chắn đúng
columns = [cell.text.strip() for cell in header_row.find_all('th')]

# In danh sách cột để kiểm tra vị trí
print("Danh sách cột:", columns)

index = 3  # Chỉ số cột cho "New Cases" (có thể thay đổi tùy theo cấu trúc bảng)

# Trích xuất dữ liệu cho mỗi quốc gia
data = []
rows = table.find('tbody').find_all('tr')

# Loại bỏ 6 dòng tổng ở cuối
country_rows = rows[:-6] if len(rows) > 6 else rows

for row in country_rows:
    cells = row.find_all('td')
    if len(cells) > index:
        country = cells[1].text.strip()  # Kiểm tra lại vị trí
        new_cases_text = cells[index].text.strip()

        # Xử lý dữ liệu: xóa ký tự "+" và dấu phẩy
        new_cases_text = re.sub(r'[\+,]', '', new_cases_text)
        new_cases = int(new_cases_text) if new_cases_text.isdigit() else 0

print(data)
