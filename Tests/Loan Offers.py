# Testcase: Verify via the UI that as a borrower - you are seeing loan offers, upon filling the required form fields with valid inputs.
# Input URL: https://www.credify.tech/phone/nonDMFunnel
# Input URL: https://www.credify.tech/portal/login

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver= webdriver.Firefox(executable_path="C:\\Users\\mbehera\\Desktop\\PROJECTS\\Automation\\Browser\\geckodriver.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.credify.tech/phone/nonDMFunnel"
portalurl = "https://www.credify.tech/portal/login"

def VerifyLoanOffer():

    #Step1:
    driver.get(url)
    driver.maximize_window()

    #Step2:
    element_LoanAmount= driver.find_element_by_name("desiredAmount")
    element_LoanAmount.click()
    element_LoanAmount.send_keys(2000)
    element_LoanPurpose = driver.find_element_by_css_selector("#root > div > main > div > div > div > div > div.col-xs-12.col-md-5 > div.section--sm.row > form > div > div > div:nth-child(2) > div > select")
    element_LoanPurpose.send_keys('d') # for 'Debt Consolidation'
    element_button= driver.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div/div[2]/div[2]/form/div/div/div[3]/button")
    element_button.submit()

    #Step3:
    firstname= driver.find_element_by_name("borrowerFirstName")
    firstname.send_keys("Tom")
    lastname = driver.find_element_by_name("borrowerLastName")
    lastname.send_keys("sandy")
    address = driver.find_element_by_name("borrowerStreet")
    address.send_keys("1111 Grundy lane, San Bruno, CA, USA")
    city= driver.find_element_by_name("borrowerCity")
    city.send_keys("San Bruno")
    state = driver.find_element_by_name("borrowerState")
    state.send_keys("California")
    zipcode = driver.find_element_by_name("borrowerZipCode")
    zipcode.send_keys(94010)
    DOB = driver.find_element_by_name("borrowerDateOfBirth")
    DOB.send_keys("01/01/1985")
    button_continue = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[1]/div[2]/div[1]/div/div/form/div[2]/button")
    button_continue.submit()
    income=driver.find_element_by_name("borrowerIncome")
    income.send_keys(125000)
    additionaliIncome = driver.find_element_by_name("borrowerAdditionalIncome")
    additionaliIncome.send_keys(6000)
    button_continue2 = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[1]/div[2]/div[1]/div/div/form/div[2]/button")
    button_continue2.submit()
    email= driver.find_element_by_name("username")
    email.send_keys("hello123@upgrade-challnge.com")
    pw= driver.find_element_by_name("password")
    pw.send_keys("Hello@123")
    checkbox= driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[1]/div[2]/div[1]/div/div/form/div[2]/div/label/div[1]")
    checkbox.click()
    checkRate_button= driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[1]/div[2]/div[1]/div/div/form/div[2]/div/label/div[1]")
    checkRate_button.submit()

    #Step4:
    driver.implicitly_wait(5)
    LoanAmount =  driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]")
    MonthlyPayment = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[1]/div/div/span").text
    Term = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[1]").text
    InterestRate = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[2]").text
    APR = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[3]/div[1]").text
    LoanAmountfinal = LoanAmount.text
    print(LoanAmountfinal)
    print(MonthlyPayment)
    print(Term)
    print(InterestRate)
    print(APR)
    menu = driver.find_element_by_xpath("//*[@id='root']/div/main/div/header/div/label")
    menu.click()
    signout = driver.find_element_by_xpath("//*[@id='root']/div/main/div/header/div/nav/ul/li[2]/a")
    signout.click()
    #driver.close()

    #Step5:
    driver.get(portalurl)
    portal_login = driver.find_element_by_name("username")
    portal_login.send_keys("hello123@upgrade-challnge.com")
    portal_pw = driver.find_element_by_name("password")
    portal_pw.send_keys("Hello@123")
    signIn = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div/div/form/button")
    signIn.submit()
    driver.implicitly_wait(5)

    #Step6:
    #offerpage_url = driver.getCurrentUrl()
    header = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[1]/div/h2")
    pageHeader = header.text
    amount= driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]").text
    offeredmonthypayment = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[1]/div/div/span").text
    offered_term = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[1]").text
    offered_InterestRate = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[2]").text
    offered_APR = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[3]/div").text
    if pageHeader == "You qualify for a discount on your debt payoff loan!":
        assert amount == LoanAmountfinal
        print("The Loan amount matches and it is " + str(LoanAmountfinal))
        assert offeredmonthypayment == MonthlyPayment
        print("Monthy payment matches and its" + str(MonthlyPayment))
        assert  offered_term == Term
        print("Term matches and its" + Term)
        assert offered_InterestRate == InterestRate
        print("Interest Rate matches and its" + InterestRate)
        assert offered_APR == APR
        print("APR matches and its" + APR)
    else:
        print("You are not on the offer-page, please check")




VerifyLoanOffer()






