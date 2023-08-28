import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_Credence:

    #@pytest.mark.xfail
    def test_CredKart_Login_008(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("Anmol94@test.in")
        driver.find_element(By.CSS_SELECTOR, "input[id = 'password']").send_keys("Credence9@143")
        driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space() = 'CredKart']")
            print("Login TestCase is Passed")
            assert True

        except:
            print("Login TestCase is Failed")
            assert False

        driver.close()

    #@pytest.mark.credence
    def test_CredKart_OrderAmountVerification_009(self):

        driver = webdriver.Chrome()

        # options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        # driver = webdriver.Chrome(options=options)

        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Anmol94@test.in")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence9@143")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(5)

        # Click on Product--Macbook
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()

        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)

        # Click on Continue Shopping
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # Click on Product--Headphone
        driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()

        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # Click on Continue Shopping
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # Click on Product--Ipad
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()

        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(4)

        # Select Quantity dropdown value for product 1
        product_quantity1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select[1]"))
        product_quantity1.select_by_index(3)

        # Select Quantity dropdown value for product 2
        product_quantity2 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select[1]"))
        product_quantity2.select_by_index(2)

        time.sleep(5)
        # Select Quantity dropdown value for product 3
        product_quantity3 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select[1]"))
        product_quantity3.select_by_index(4)
        time.sleep(4)

        # Find out len checking subtotal & your total
        l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        l = 6

        # l-2 because of we want on 3 product values
        Product_Price_List = []
        for r in range(1, l - 2):
            var1 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            # Slicing for remove $
            product_price = (var1[1:])
            Product_Price_List.append(float(product_price))

        # Addition of Productwise  # 2 digit tak round off karne ke liye
        Exp_Subtotal = round(sum(Product_Price_List), 2)
        print("Exp_Subtotal-->" + str(Exp_Subtotal))

        print(Product_Price_List)
        time.sleep(5)

        System_Value = []
        for r in range(l - 2, l + 1):
            var2 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            # Replace "," value ['13,499.88', '1,754.98', '15,254.86']
            var3 = var2.replace(',', '')
            # Slicing for remove $
            system_price = (var3[1:])
            System_Value.append(float(system_price))

        print(System_Value)
        time.sleep(5)

        if Exp_Subtotal == System_Value[0]:
            print("Subtotal is match")
            assert True
        else:
            print("Subtotal is not match")
            assert False

        driver.close()

    #@pytest.mark.credence
    def CredKart_Order_CheckOut(self):

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options=chrome_options)

        driver = webdriver.Chrome()
        driver.maximize_window()

        # Open URL
        driver.get("https://automation.credence.in/login")

        # Inspect Email Address
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Anmol94@test.in")

        # Inspect Password
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence9@143")

        # Click Login Button
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        time.sleep(5)

        # Click on Product--Macbook
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()

        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)

        # Inspect Proceed to Checkout
        driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to Checkout']").click()
        time.sleep(4)

        # Inspect Enter First Name
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Amol")

        # Inspect Enter Last Name
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Deshmukh")

        # Inspect Enter Phone
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9999888877")

        # Inspect Enter Address
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Hinjewadi, Pune")

        # Inspect Zip Code
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411013")
        time.sleep(2)

        # Inspect Select State & Dropdown
        State = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        State.select_by_index(1)

        # Inspect Enter Owner Name
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")

        # Inspect CVV
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")

        # Inspect Card Number
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")

        # Inspect Expiration Date
        Exp_Year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        Exp_Year.select_by_index(2)

        Exp_Month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        Exp_Month.select_by_index(2)

        # Inspect Click on Continue to Checkout
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()

        # After Checkout capture Successfull message
        print(driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)
        time.sleep(10)

        driver.close()















