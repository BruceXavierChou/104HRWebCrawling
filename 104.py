import requests
from bs4 import BeautifulSoup
import csv

# 要搜尋的關鍵字和頁數
keyword = "Python軟體工程師"
pages = 3  # 指定要爬取的頁數

# 建立CSV檔案並寫入標題列
csv_file = open("104_jobs.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["公司名稱", "職缺", "工作內容"])

# 迴圈爬取多個頁面的資料
for page in range(1, pages + 1):
    url = f"https://www.104.com.tw/jobs/search/?ro=0&keyword={keyword}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 找出所有職缺列表項目
    job_items = soup.find_all("article", class_="b-block--top-bord job-list-item b-clearfix js-job-item")

    # 逐一處理每個職缺
    for item in job_items:
        company_name_elem = item.find("li", class_="b-list-inline__ad-icon").find_next("li")
        job_title_elem = item.find("a", class_="js-job-link")
        job_content_elem = item.find("p", class_="job-list-item__info b-clearfix b-content")

        if company_name_elem:
            company_name = company_name_elem.text.strip()
        else:
            company_name = "N/A"

        if job_title_elem:
            job_title = job_title_elem.text.strip()
        else:
            job_title = "N/A"

        if job_content_elem:
            job_content = job_content_elem.text.strip()
        else:
            job_content = "N/A"

        # 寫入CSV檔案
        csv_writer.writerow([company_name, job_title, job_content])

# 關閉CSV檔案
csv_file.close()

print("資料已成功寫入104_jobs.csv檔案。")
