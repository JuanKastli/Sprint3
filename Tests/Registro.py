from selenium import webdriver
#from selenium.webdriver import wait
from selenium.webdriver.common.by import By
import time

class Bertoldiregistro:
    def __init__(self):
        # Inicializar el navegador web (en este caso, Chrome)
        self.driver = webdriver.Chrome()
    
    def accept_cookies(self):
        # Abrir la página de registro de Bertoldi
        self.driver.get("https://bertoldi.com.ar/account/register")
        #self.driver.SetPreference("profile.default_content_setting_values.notifications", 2) 
    

    def complete_registration(self):
        #Ingresamos a la pagina de registro de Bertoldi
        self.driver.get("https://bertoldi.com.ar/account/register")
        #Ingresar Nombre
        self.driver.find_element(By.ID,"FirstName").send_keys("Hola")
        #Ingresar Apellido
        self.driver.find_element(By.ID,"LastName").send_keys("Que tal")
        #Ingresar Correo Electrónico
        self.driver.find_element(By.ID,"Email").send_keys("hola16@gmail.com")
        #Ingresar Contraseña
        self.driver.find_element(By.ID,"CreatePassword").send_keys("123456789#")
        #Hace un screenshot de la página
        self.screenshot = self.driver.get_screenshot_as_file("C:\\Users\\juank\\Python Framework\\Automation Proyect\\Práctica Automation\\src\data\\evidencia\\evidenciaregistro1.png")
        time.sleep(10)
        #Botón Crear
        self.driver.find_element(By.XPATH, "//input[@id='register-submit']").click()
        self.driver.implicitly_wait (100)
        #aceptar publicidad
        self.driver.find_element(By.XPATH, "/html/body/div[10]/dialog/div/div[2]/div/button[1]").click()
        self.driver.implicitly_wait (100)
        time.sleep(10)
        #Aceptar Captcha
        #self.driver.find_element(By.ID, '//*[@id="g-recaptcha-response-100000"]').click()
        #self.driver.implicitly_wait(100)
        #Verificar Captcha manualmente
        #self.driver.find_element(By.XPATH, '//*[@id="MainContent"]/div/form/input[2]').click()
        #self.driver.implicitly_wait(100)
        #btnSignIn = driver.find_element_by_id('//*[@id="MainContent"]/div/form/input[2]')
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btnSignIn))
        #btnSignIn.click()
        #Hacer screenshot de la página
        self.screenshot = self.driver.get_screenshot_as_file("C:\\Users\\juank\\Python Framework\\Automation Proyect\\Práctica Automation\\src\data\\evidencia\\evidenciacapcha.png")
        time.sleep(20)
        #Ir a Cuenta
        self.driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
        time.sleep(200)
        #Hacer screenshot de la página
        self.screenshot = self.driver.get_screenshot_as_file("C:\\Users\\juank\\Python Framework\\Automation Proyect\\Práctica Automation\\src\data\\evidencia\\evidenciaregistrocuenta1.png")
        time.sleep(20)
        self.driver.find_element(By.ID,'//*[@id="CustomerEmail"]').send_keys("hola16@gmail.com")
        time.sleep(20)
        self.driver.find_element(By.ID,'//*[@id="CustomerEmail"]').send_keys("123456789#")
        time.sleep(20)
        
    def close_browser(self):
        # Cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    automation = Bertoldiregistro()
    automation.accept_cookies()
    automation.complete_registration()
    automation.close_browser()