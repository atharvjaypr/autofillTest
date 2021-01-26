from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


import time
print("------------Welcome to AandaFill-----------------")
Cname = input("Cardholder name: ")
Cmail = input("Email address: ")
Cnum = input("Card number: ")
Ccvc = input("Security Code(CVC): ")
Cexp = input("Expiration: ")
Caddy = input("Billing address: ")
Ccity = input("City: ")
Cstate = input("State: ")
Czip = input("Zip Code: ")

print("...")
print("...")
print("...")
print("...")
print("Saved!")
yn = input("Would you like to autosubmit?(Y/N): ")
if yn == "Y":
    a = 0
else:
    a = 1
print("Beginning process...")




web = webdriver.Chrome('/Users/atharvjayprakash/Desktop/chromedriver')
web.get('https://stripe-payments-demo.appspot.com/')

time.sleep(2)

#Cname = "Ath Jay"
name = web.find_element_by_xpath('//*[@id="payment-form"]/section[1]/fieldset/label[1]/input')
name.send_keys(Cname)

#Cmail = "mailskdnojsn@gdncx.com"
mail = web.find_element_by_xpath('//*[@id="payment-form"]/section[1]/fieldset/label[2]/input')
mail.send_keys(Cmail)

#Caddy = "2"
addy = web.find_element_by_xpath('//*[@id="payment-form"]/section[1]/fieldset/label[3]/input')
addy.send_keys(Caddy)

#Ccity = "morganivuik"
city = web.find_element_by_xpath('//*[@id="payment-form"]/section[1]/fieldset/label[4]/input')
city.send_keys(Ccity)

#Cstate = "nj"
state = web.find_element_by_xpath('//*[@id="payment-form"]/section[1]/fieldset/label[5]/input')
state.send_keys(Cstate)

#Czip = "07751"
zzip = web.find_element_by_xpath('//*[@id="payment-form"]/section[1]/fieldset/label[6]/input')
zzip.send_keys(Czip)

#Cnum = "1234 5678 9101 1123"
wait(web, 10).until(EC.frame_to_be_available_and_switch_to_it('//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input'))
num = web.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')
#num.click()
num.send_keys(Cnum)
web.switch_to.default_content()


#Cexp = "01/23"
exp = web.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[2]/span/span/input')
exp.send_keys(Cexp)

#Ccvc = "123"
cvc = web.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[3]/span/span/input')
cvc.send_keys(Ccvc)




#CheckoutClick

if a == 0:
    submit = web.find_element_by_xpath('//*[@id="payment-form"]/button')
    submit.click()







