# MyCrawl

MyCrawl은 Scrapy와 Selenium을 사용하여 동적으로 웹사이트에서 데이터를 추출하는 웹 스크래핑 프로젝트입니다. Selenium을 사용하여 JavaScript로 렌더링된 콘텐츠를 처리합니다.

## 사전 요구사항

- Python 3.10.4
- Scrapy
- Selenium
- WebDriver (예: ChromeDriver)

## 설치

1. 저장소를 클론합니다:

    ```bash
    git clone https://github.com/harry81/mycrawl.git
    cd mycrawl
    ```

2. 가상 환경을 생성하고 활성화합니다:

    ```bash
    python -m venv venv
    source venv/bin/activate  # 윈도우의 경우 `venv\Scripts\activate`
    ```

3. 필요한 패키지를 설치합니다:

    ```bash
    pip install -r requirements.txt
    ```

4. 브라우저용 WebDriver를 다운로드하고 알려진 디렉토리에 위치시킵니다.

## 설정

`mycrawl/settings.py` 파일을 업데이트하여 Selenium 및 WebDriver 경로를 설정합니다:

```python
from shutil import which
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  # 헤드리스 모드를 사용할 경우 '--headless'
```


## 실행

```bash
    $ scrapy crawl naver_shopping -o products.json
```

## 기여

- 원하시면 누구든지 마음대로 코드 사용하실 수 있습니다.
- 추가기능 알려주시면 개선하겠습니다.



[![네이버 쇼핑 크롤링하기](http://img.youtube.com/vi/Z6UAz6GaMbc/0.jpg)](http://www.youtube.com/watch?v=Z6UAz6GaMbc "네이버 쇼핑 크롤링하기")
