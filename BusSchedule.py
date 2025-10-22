#BusSchedule.py
#Name:
#Date:
#Assignment:

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents


def main():
  url = "https://myride.ometro.com/Schedule?stopCode=1264&date=2025-10-21&routeNumber=24&directionName=NORTH"
  c1 = loadURL(url) #loads the web page
  #c1 = loadTestPage() #loads the test page
 

  c1= c1.split()
  
  times = []
  for i in c1:
    if ("AM" in i):
      times.append(i)
    if ("PM" in i):
      times.append(i)
  
  Time(times)
def Time (times):
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute
  
  half_of_day = "AM"
  
  if currentHour == 12:
    half_of_day = "PM"
  if currentHour > 12:
    currentHour = currentHour %12
    half_of_day = "PM"
  if currentHour == 0:
    currentHour = 12
  print(f"{currentHour}:{currentMinute} {half_of_day}")
  currentTime = f"{currentHour}:{currentMinute}{half_of_day}"
  futureTime(times, currentTime)

def futureTime(times, currentTime):
  counter = 0
  currentTime = datetime.datetime.strptime(currentTime, "%I:%M%p").time()
  

  today = datetime.date.today()
  nowTime = datetime.datetime.combine(today, currentTime)

  futureBus = []
  for i in times:
    i= datetime.datetime.strptime(i, "%I:%M%p").time()
    if i > currentTime:
      futureBus.append(i)
    if len(futureBus) == 2:
      break

 

  if len(futureBus)== 0:
    first_bus_time = datetime.datetime.strptime(times[0], "%I:%M%p").time()
    tomorrow_dt = datetime.datetime.combine(today + datetime.timedelta(days=1), first_bus_time)
    wait_minutes = int((tomorrow_dt - nowTime).total_seconds() // 60)
    hours = wait_minutes // 60
    minutes = wait_minutes % 60
    print(f"No more buses for today.")
    print(f"The first bus tomorrow will arrive in {hours} hours and {minutes} minutes.")
    return

    
  next_bus_dt = datetime.datetime.combine(today, futureBus[0])
  wait1 = int((next_bus_dt - nowTime).total_seconds() // 60)
  print(f"The next bus will arrive in {wait1} minutes.")
  if len(futureBus) > 1:
    followingBus = datetime.datetime.combine(today, futureBus[1])
    wait2 = int((followingBus - nowTime).total_seconds() // 60)
    print(f"The following bus will arrive in {wait2} minutes.")
      
    

  


  
  
  

  
  


main()
