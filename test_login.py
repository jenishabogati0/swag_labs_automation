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
        self.lp = LoginPage(self.driver)
        self.lp.setUserNamee(self.usernamee)
        self.lp.setPasswordd(self.passwordd)
        self.lp.clickLoginn()

    def test_Homepage(self):
        self.test_Login()
        self.lp = HomePage(self.driver)
        self.lp.clickAddtoCart()
        self.lp.clickShoppingCart()
        self.lp.clickCheckOut()

    def test_Checkout(self):
        self.test_Homepage()
        self.lp = CheckOut(self.driver)
        self.lp.setFirstNamee(self.firsnamee)
        self.lp.setLastNamee(self.lastnamee)
        self.lp.setZipPostalCodee(self.zippostalcodee)
        self.lp.clickContinuee()


if __name__ == '__main__':
    login = Test_001_login()
    login.test_Login()
    login.test_Homepage()
    login.test_Checkout()
    
