import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://demoqa.com/'

# данные для ввода в необходимые поля в Text box:
name = 'Ivan Ivanov'
mail = 'mail@mail.com'
c_address = 'Moscow, Tverskaya st. 1'
p_address = 'Saint Petersburg, Small Garden st. 3'

# данные для ввода в последний Alert:
Test_name = 'Test name'


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'eager'
    chrome_options.executable_path = 'drivers/chromedriver.exe'
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestdemoQA:
    @allure.feature('Open website')
    @allure.story('Открываем страницу https://demoqa.com/')
    @allure.severity('blocker')
    def test_open_website(self):
        self.driver.get(link)

    @allure.feature('Find elements')
    @allure.story('Находим блок Elements и нажимаем на него')
    @allure.severity('critical')
    def test_find_elements(self):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div['
                                                                        '1]/div/div[2]')))
        elements.click()

    @allure.feature('Find Text box')
    @allure.story('Находим кнопку Text box и нажимаем на неё')
    @allure.severity('critical')
    def test_find_text_box(self):
        self.driver.find_element(By.XPATH, '//*[@id="item-0"]/span').click()

    @allure.feature('Fill inbox')
    @allure.story('Заполняем нужные поля')
    @allure.severity('critical')
    def test_fill_inbox(self):
        self.driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys(mail)
        self.driver.find_element(By.XPATH, '//*[@id="currentAddress"]').send_keys(c_address)
        self.driver.find_element(By.XPATH, '//*[@id="permanentAddress"]').send_keys(p_address)

    @allure.feature('Submit button')
    @allure.story('Нажимаем кнопку Submit')
    @allure.severity('critical')
    def test_submit_button(self):
        submit = self.driver.find_element(By.ID, 'submit')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        submit.click()

    @allure.feature('Check output')
    @allure.story('Проверяем соответствие выведенных данных с введёнными')
    @allure.severity('critical')
    def test_check_output(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "output")))
        assert name in element.text
        assert mail in element.text
        assert c_address in element.text
        assert p_address in element.text

    @allure.feature('Buttons')
    @allure.story('Находим кнопку Buttons и нажимаем на неё')
    @allure.severity('critical')
    def test_buttons(self):
        self.driver.find_element(By.XPATH, '//*[@id="item-4"]/span').click()

    @allure.feature('Click me button')
    @allure.story('Находим кнопку Click me и нажимаем на неё')
    @allure.severity('critical')
    def test_click_me_button(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button').click()

    @allure.feature('Click me output')
    @allure.story('Проверяем, что появился нужный текст')
    @allure.severity('major')
    def test_click_me_output(self):
        wait = WebDriverWait(self.driver, 10)
        click_elem = wait.until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))
        assert 'You have done a dynamic click' in click_elem.text

    @allure.feature('Right click me button')
    @allure.story('Находим кнопку Right click me и нажимаем на неё')
    @allure.severity('critical')
    def test_right_click_button(self):
        rb = self.driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
        act = ActionChains(self.driver)
        act.context_click(rb).perform()

    @allure.feature('Right click me output')
    @allure.story('Проверяем, что появился нужный текст')
    @allure.severity('major')
    def test_right_click_output(self):
        wait = WebDriverWait(self.driver, 10)
        r_click_elem = wait.until(EC.presence_of_element_located((By.ID, "rightClickMessage")))
        assert 'You have done a right click' in r_click_elem.text

    @allure.feature('Double click me button')
    @allure.story('Находим кнопку Double click me и нажимаем на неё')
    @allure.severity('critical')
    def test_double_click_button(self):
        db = self.driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
        act = ActionChains(self.driver)
        act.double_click(db).perform()

    @allure.feature('Double click me output')
    @allure.story('Проверяем, что появился нужный текст')
    @allure.severity('major')
    def test_double_click_output(self):
        wait = WebDriverWait(self.driver, 10)
        d_click_elem = wait.until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))
        assert 'You have done a double click' in d_click_elem.text

    @allure.feature('Alerts, frame & windows')
    @allure.story('Нажимаем на кнопку Alerts, frame & windows')
    @allure.severity('critical')
    def test_alerts_frame_windows(self):
        afw = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[3]/span/div/div[1]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", afw)
        afw.click()

    @allure.feature('Browser windows')
    @allure.story('Нажимаем на кнопку Browser windows')
    @allure.severity('critical')
    def test_browser_windows_button(self):
        wait = WebDriverWait(self.driver, 10)
        browser_windows = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div['
                                                                               '1]/div/div/div[3]/div/ul/li[1]/span')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", browser_windows)
        browser_windows.click()

    @allure.feature('New tab')
    @allure.story('Нажимаем на кнопку New tab')
    @allure.severity('critical')
    def test_new_tab(self):
        self.driver.find_element(By.ID, 'tabButton').click()

    @allure.feature('Close new tab')
    @allure.story('Закрываем новую вкладку')
    @allure.severity('critical')
    def test_close_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.feature('New window')
    @allure.story('Нажимаем на кнопку New window')
    @allure.severity('critical')
    def test_new_window(self):
        self.driver.find_element(By.ID, 'windowButton').click()

    @allure.feature('Close new window')
    @allure.story('Закрываем новое окно')
    @allure.severity('critical')
    def test_close_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.feature('Alerts')
    @allure.story('Нажимаем кнопку Alerts')
    @allure.severity('critical')
    def test_alerts(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]'
                                           '/div/div/div[3]/div/ul/li[2]').click()

    @allure.feature('Simple alert')
    @allure.story('Нажимаем на кнопку, вызывающую первый alert')
    @allure.severity('critical')
    def test_simple_alert(self):
        self.driver.find_element(By.ID, 'alertButton').click()

    @allure.feature('Close simple alert')
    @allure.story('Закрываем уведомление')
    @allure.severity('major')
    def test_close_simple_alert(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

    @allure.feature('Time alert')
    @allure.story('Нажимаем на кнопку, вызывающую второй alert')
    @allure.severity('critical')
    def test_time_alert(self):
        self.driver.find_element(By.ID, 'timerAlertButton').click()

    @allure.feature('Close time alert')
    @allure.story('Дожидаемся и закрываем уведомление')
    @allure.severity('major')
    def test_close_time_alert(self):
        wait = WebDriverWait(self.driver, 10)
        alert_obj = wait.until(EC.alert_is_present())
        alert_obj.accept()

    @allure.feature('Confirm alert')
    @allure.story('Нажимаем на кнопку, вызывающую третий alert')
    @allure.severity('critical')
    def test_confirm_alert(self):
        self.driver.find_element(By.ID, 'confirmButton').click()

    @allure.feature('Close confirm alert')
    @allure.story('Нажимаем "Да" и закрываем уведомление')
    @allure.severity('major')
    def test_click_confirm_alert(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

    @allure.feature('Check confirm alert')
    @allure.story('Проверяем, что появился нужный текст')
    @allure.severity('major')
    def test_check_confirm_alert(self):
        wait = WebDriverWait(self.driver, 10)
        confirm_elem = wait.until(EC.presence_of_element_located((By.ID, "confirmResult")))
        assert f'You selected Ok' in confirm_elem.text

    @allure.feature('Prompt alert')
    @allure.story('Нажимаем на кнопку, вызывающую четвёртый alert')
    @allure.severity('critical')
    def test_prompt_alert(self):
        self.driver.find_element(By.ID, 'promtButton').click()

    @allure.feature('Send keys prompt alert')
    @allure.story('Вводим необходимые данные в четвёртый alert')
    @allure.severity('critical')
    def test_send_keys_prompt_alert(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.send_keys(Test_name)
        alert_obj.accept()

    @allure.feature('Check prompt alert')
    @allure.story('Проверяем, что появился нужный текст в соответствии с введёнными данными')
    @allure.severity('critical')
    def test_check_prompt_alert(self):
        wait = WebDriverWait(self.driver, 10)
        prompt_elem = wait.until(EC.presence_of_element_located((By.ID, "promptResult")))
        assert f'You entered {Test_name}' in prompt_elem.text


if __name__ == '__main__':
    pytest.main()
