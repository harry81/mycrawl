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

    def __init__(self, *args, **kwargs):
        super(NaverShoppingSpider, self).__init__(*args, **kwargs)
        self.keyword = kwargs.get('keyword')

    def start_requests(self):
        url = "https://shopping.naver.com/home"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        driver = response.meta['driver']

        target_banner_xpath = "//div[contains(@class, '_targetBanner_target_banner_')]"
        target_banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, target_banner_xpath)))
        target_banner.click()

        search_button_xpath = "//button[contains(@class, '_combineHeader_expansion_search_button_')]"
        search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_button_xpath)))
        search_button.click()

        search_input_xpath = "//input[contains(@class, '_searchInput_input_text')]"
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_input_xpath))
        )

        search_input.send_keys(self.keyword)
        search_input.send_keys(Keys.ENTER)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'product_list_item__')]"))
        )

        # 스크롤 다운 (더 많은 결과 로딩)
        for _ in range(0, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)

        # 상품 정보 추출
        products = driver.find_elements(By.XPATH, "//div[contains(@class, 'product_list_item__')]")
        ret = []

        for product in products:
            title = product.find_element(By.XPATH, ".//span[contains(@class, 'product_info_tit')]").text
            price = product.find_element(By.XPATH, ".//div[contains(@class, 'product_price__')]").text
            link = product.find_element(By.XPATH, ".//a")
            link_text = link.get_attribute('href')

            item = {
                'title': title,
                'price': price,
                'link': link_text,
            }
            yield item
            ret.append(item)
