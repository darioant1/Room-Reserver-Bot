from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta

def move_to_next_day(driver):
    """Click the right arrow to move to the next day."""
    right_arrow = driver.find_element(By.CLASS_NAME, 'fa-chevron-right')
    right_arrow.click()

def check_for_available_rooms(driver):
    """Check for available rooms between 3 PM and 7 PM on the current day."""
    available_times = driver.find_elements(By.XPATH, "//a[contains(@class, 's-lc-eq-avail') and contains(@title, 'Available')]")
    
    filtered_times = []
    for time_element in available_times:
        title = time_element.get_attribute("title")
        time_str = title.split()[0]  # get the time part (ex "3:00pm")
        time_obj = datetime.strptime(time_str, "%I:%M%p")  

        # check if time is between 3:00 PM - 7:00 PM, can change for whatever time wanted
        start_time = datetime.strptime("3:00pm", "%I:%M%p")
        end_time = datetime.strptime("7:00pm", "%I:%M%p")

        if start_time <= time_obj <= end_time:
            filtered_times.append(time_element)

    return filtered_times

def reserve_library_room(email, password, PID, groupName):
    driver = webdriver.Chrome()

    try:
        # go to library page
        driver.get('https://ucf.libcal.com/reserve/largestudyrooms')  

        while True:
            # check if rooms available on current day
            filtered_times = check_for_available_rooms(driver)

            # if rooms are available
            if filtered_times:
                filtered_times[0].click()  # select the first available time

                # click the "Submit Times" button
                submit_button = driver.find_element(By.ID, 'submit_times')
                submit_button.click()

                # handle login (if prompted)
                try:
                    # input username (email)
                    email_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'userNameInput')) 
                    )
                    email_box.send_keys(email)

                    # click "Next" button
                    next_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, 'nextButton')) 
                    )
                    next_button.click()

                    # input password
                    password_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'passwordInput'))  
                    )
                    password_box.send_keys(password)

                    # click "Sign In" button
                    sign_in_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, 'submitButton')) 
                    )
                    sign_in_button.click()

                except Exception as e:
                    print("No email/password prompt or an error occurred:", e)

                # click "Continue" button
                continue_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'terms_accept'))  
                )
                continue_button.click()

                group_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'nick'))
                )
                group_box.send_keys(groupName)

                # click "Status" and "Undergraduate Student"
                status_dropdown = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'q2613'))  
                )
                select_status = Select(status_dropdown)
                select_status.select_by_visible_text('Undergraduate Student')

                # input PID
                pid_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'q2614'))
                )
                pid_box.send_keys(PID)

                # click "Submit" button
                second_submit_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'btn-form-submit'))
                )
                second_submit_button.click()
                
                print("Room reserved successfully!")
                break  # Stop once a room is reserved

            else:
                # If no rooms are available for the current day, move to the next day
                print("No available rooms found for this day, moving to the next day.")
                move_to_next_day(driver)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
