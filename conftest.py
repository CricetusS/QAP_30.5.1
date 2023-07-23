from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

LOGIN = "user@mailbox.com"
PASS = "12345678"


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('c:/SkillF/ChromeDriver/chromedriver.exe')
    pytest.driver.set_window_size(1200, 1000)
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    pytest.driver.find_element(By.ID, 'email').send_keys(LOGIN)
    pytest.driver.find_element(By.ID, 'pass').send_keys(PASS)

    # Неявное ожидание
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends", 'Включилась не главная страница'

    yield

    pytest.driver.quit()
