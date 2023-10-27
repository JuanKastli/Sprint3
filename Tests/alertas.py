from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Bertoldiregistro:
    def __init__(self):
        # Inicializar el navegador web (en este caso, Chrome)
        self.driver = webdriver.Chrome()
    
    def accept_cookies(self):
        # Abrir la página de registro de Bertoldi
        self.driver.get("https://bertoldi.com.ar/account/register")
        
    

    def complete_registration(self):
        #Ingresamos a la pagina de registro de Bertoldi
        self.driver.get("https://bertoldi.com.ar/account/register")
        #Ingresar Nombre
        self.driver.find_element(By.ID,"FirstName").send_keys("")
        #Ingresar Apellido
        self.driver.find_element(By.ID,"LastName").send_keys("")
        #Ingresar Correo Electrónico
        self.driver.find_element(By.ID,"Email").send_keys("")
        #Ingresar Contraseña
        self.driver.find_element(By.ID,"CreatePassword").send_keys("")
        #Hacer screenshot de la página
        self.screenshot = self.driver.get_screenshot_as_file("C:\\Users\\juank\\Python Framework\\Automation Proyect\\Práctica Automation\\src\\data\\evidencia\\Alertablanco.png")
        time.sleep(10)
        #Botón Crear
        self.driver.find_element(By.XPATH, "//input[@id='register-submit']").click()
        self.driver.implicitly_wait (100)
        time.sleep(10)
        #aceptar publicidad
        self.driver.find_element(By.XPATH, "/html/body/div[10]/dialog/div/div[2]/div/button[1]").click()
        time.sleep(200)
        #Botón Enviar
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/input[2]').click()
        time.sleep(200)
        #Hacer screenshot de la página
        self.screenshot = self.driver.get_screenshot_as_file("C:\\Users\\juank\\Python Framework\\Automation Proyect\\Práctica Automation\\src\\data\\evidencia\\Alerta2.png")
        time.sleep(50)
        

    def close_browser(self):
        # Cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    automation = Bertoldiregistro()
    automation.accept_cookies()
    automation.complete_registration()
    automation.close_browser()
