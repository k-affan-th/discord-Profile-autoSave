from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getAvatarByIDs(driver:webdriver.Edge, IDs:list) -> dict:
    """
    Processes a list of Discord IDs, finding and extracting avatar URLs.

    Args:
        driver (webdriver): The Selenium WebDriver instance.
        IDs (list): A list of Discord user IDs.

    Returns:
        list: A list of extracted avatar URLs.
    """
    # Define the empty list to stores all of avatar urls
    avatar_info = {}

    for id in IDs:
        input_box = driver.find_element(By.ID, 'input')
        input_box.send_keys(id)
        input_box.submit()

        # Wait for the element to be present on the page
        avatar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "avatar")))
        
        user_name = driver.find_element(By.ID, 'username').text
        avatar_url = avatar.get_attribute('href')

        # Set the Dictionary to avatar ID
        avatar_info[id] = {'name': user_name,'avatar_url': avatar_url}
        driver.execute_script('location.reload()')

    return avatar_info