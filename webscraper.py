from selenium import webdriver

class Product:
  def __init__(self):
    self.name = ""
    self.price = ""
    self.availability = ""
  
  def toString(self):
    print("Name: {}, Price: {}, Availability: {}".format(self.name,self.price,self.availability))

class Products:
  def __init__(self):
    self.list = []
    
  def add(self,product):
    self.list.append(product)

  def toString(self):
    for product in self.list:
      print("* ",end="")
      print(product.toString())

products = Products()
driver = webdriver.Chrome()

def scrapeAlternate(url):
  product = Product()
  driver.get(url)

  element = driver.find_element_by_xpath("//*[@id=\"buyProduct\"]/div[3]/div/div[3]/div[4]/meta[@itemprop=\"name\"]")
  if (element!=None):
    product.name = element.get_attribute("content")

  element = driver.find_element_by_xpath("//*[@id=\"buyProduct\"]/div[3]/div/div[3]/div[4]/meta[@itemprop=\"availability\"]")
  if (element!=None):
    product.availability = element.get_attribute("content")

  element = driver.find_element_by_xpath("//*[@id=\"buyProduct\"]/div[3]/div/div[3]/div[4]/span[@itemprop=\"price\"]")
  if (element!=None):
    product.price = element.get_attribute("content")

  products.add(product)
  
scrapeAlternate("https://www.alternate.nl/Ducky/One-2-RGB-DKON1808ST-gaming-toetsenbord/html/product/1472041?")
scrapeAlternate("https://www.alternate.nl/Ducky/One-2-RGB-TKL-DKON1787ST-gaming-toetsenbord/html/product/1472065?")

driver.close()

print("Scraped")
products.toString()