from POMProjectDemo.pageObjects.CheckOut import CheckOut
from POMProjectDemo.pageObjects.LoginPage import LoginPage
from POMProjectDemo.pageObjects.homepage import HomePage
from confest import setup

class Test_001_login:
    baseURLL = "https://www.saucedemo.com/"
    usernamee = "standard_user"
    passwordd = "secret_sauce"
    firsnamee = "jenny"
    lastnamee = "bogati"
    zippostalcodee = "44600"

 
    def test_Login(self):
        self.driver = setup()
        self.driver.get(self.baseURLL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserNamee(self.usernamee)
        self.loginpage.setPasswordd(self.passwordd)
        self.loginpage.clickLoginn()
        self.homepage = HomePage(self.driver)
        self.homepage.clickAddtoCart()
        self.homepage.clickShoppingCart()
        self.homepage.clickCheckOut()
        self.checkout = CheckOut(self.driver)
        self.checkout.setFirstNamee(self.firsnamee)
        self.checkout.setLastNamee(self.lastnamee)
        self.checkout.setZipPostalCodee(self.zippostalcodee)
        self.checkout.clickContinuee()


if __name__ == '__main__': 
    login = Test_001_login()
    login.test_Login()
    
