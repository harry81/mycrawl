import time
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NaverShoppingSpider(scrapy.Spider):
    name = "naver_shopping"

    allowed_domains = ["shopping.naver.com"]

    def start_requests(self):
        url = "https://shopping.naver.com/home"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        driver = response.meta['driver']

        # 검색어 입력
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class, '_searchInput_search_text_')]"))
        )
        search_input.send_keys("노트북")

        # 엔터키 입력
        search_input.send_keys(Keys.ENTER)


        # 페이지 로딩 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'basicList_list_basis__')]"))
        )

        # 스크롤 다운 (더 많은 결과 로딩)
        for _ in range(0, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)

        # 상품 정보 추출
        products = driver.find_elements(By.XPATH, "//div[contains(@class, 'product_item__')]")
        ret = []

        for product in products:
            title = product.find_element(By.XPATH, ".//a[contains(@class, 'product_link__')]").text
            price = product.find_element(By.XPATH, ".//span[contains(@class, 'price_num__')]").text
            # product_compare = product.find_element(By.XPATH, ".//span[contains(@class, 'product_compare__')]").text

            item = {
                'title': title,
                'price': price,
                # 'product_compare': product_compare
            }
            yield item
            ret.append(item)
