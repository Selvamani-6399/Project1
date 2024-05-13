"""
locator.py
"""

class WebLocators:


   def __init__(self):
       self.usernameLocator = "username"
       self.passwordLocator = "password"
       self.buttonLocator = "//button[@type='submit']"
       self.invalid_popup = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'
       self.pim = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
       self.addbutton = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
       self.firstnameLocator = "firstName"
       self.lastnameLocator = "lastName"
       self.savebtnlocator = "//button[@type='submit']"
       self.successmassageLocator = '//*[@id="app"]/div[2]/div/div[1]/div[2]/p[2]'
       self.editLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[2]'
       self.editsavebtnlocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
       self.deleteLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]'
       self.deleteconformationLocator = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'


