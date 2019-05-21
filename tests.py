import time

from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        'app': r'C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.exe'
    })

driver.implicitly_wait(10)
button = driver.find_element_by_name('orderbutton')
button.click()
tabs = driver.find_elements_by_name('tab')
text = []
for tab in tabs:
    tab.click()
    items = driver.find_elements_by_name('item_button')
    for item in items:
        item.click()
        text.append(item.text)

orders = driver.find_elements_by_name('order_item')
counter = 0
for order in orders:
    if order in text:
        counter += 1

assert (counter == len(text))

cost = driver.find_elements_by_name("cost")
total_r = 0
for value in cost:
    total_r += int(cost.text)

total = driver.find_elements_by_name("total_label")

assert (int(total.text) == total_r)

create = driver.find_element("createbutton")
create.click()

time.sleep(10)  # wait for ok click

# написать тест для проверки тотала тарифов
# написать тест для частичного закрытия заказа с разными параметрами
# тест для забития всякой хрени в поля ввода
