from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


url = 'https://learn.ontariotechu.ca/'
options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument("headless")
driverService = Service(r'C:\Users\COCRe\Downloads\CasualSoftwares\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=driverService, options=options)
driver.get(url)


def get_login_info():

    info = []
    f = open('login.txt', 'r')

    for line in f.readlines():
        info.append(line.strip('\n'))

    f.close()
    return info


def beautify(name: BeautifulSoup, title: BeautifulSoup, due_date: BeautifulSoup):

    assign_date: list

    title = title.text.strip()
    due_date = "Due on: " + due_date.text.strip()
    temp = name.text.strip()
    name = temp.split('-')[1] + ": " + title
    assign_date = [name, due_date]

    return assign_date


def log_in():

    USERNAME = get_login_info()[0]
    PASSWORD = get_login_info()[1]

    driver.find_element(by=By.NAME, value="UserName").send_keys(USERNAME)
    driver.find_element(by=By.NAME, value="Password").send_keys(PASSWORD)
    driver.find_element(by=By.CSS_SELECTOR, value="span.submit").click()
    time.sleep(3)
    print("Successfully Logged In")


def main():

    schedule = []
    courses = ['21839', '21707', '21871', '21918', '21436']

    for c in courses:

        path_str = '//a[@href="/courses/' + c + '/assignments"]'
        time.sleep(1.5)
        driver.find_element(by=By.XPATH, value=path_str).click()
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        assignments = []
        name = soup.find("a")
        try:
            area_filter = soup.find(id='assignment_group_upcoming_assignments')
            assignments = area_filter.find_all("div", class_="ig-info")
        except AttributeError:
            pass

        try:
            area_filter = soup.find(id='assignment_group_undated_assignments')
            assignments = area_filter.find_all("div", class_="ig-info")
        except AttributeError:
            pass

        if len(assignments) != 0:
            for a in assignments:
                title = a.find("a")

                try:
                    due_data_div = a.find("div", class_='ig-details__item assignment-date-due')
                except AttributeError:
                    due_data_div = a.find("div", class_='ig-details__item assignment-date-available')

                try:
                    due_date = due_data_div.find("span", class_='screenreader-only')
                except AttributeError:
                    due_date = a.find("span", class_='screenreader-only')

                schedule.append(beautify(name, title, due_date))

            driver.find_element(by=By.XPATH, value='//a[@href="https://learn.ontariotechu.ca/"]').click()
            time.sleep(2.5)

    file = open('schedule.txt', 'w')

    for value in schedule:
        file.write(value[0] + '\n' + value[1] + '\n')

    file.close()


def schedule_to_string():
    main()
    assignment_pair = []
    f = open('schedule.txt')

    for line in f:
        assignment_pair.append(line)

    f.close()

    output = ''
    for i in range(len(assignment_pair)):
        if i % 2 == 0:
            output += "```" + assignment_pair[i]
        else:
            output += assignment_pair[i] + '\n' + "```"

    return output


if __name__ == "__main__":
    main()
