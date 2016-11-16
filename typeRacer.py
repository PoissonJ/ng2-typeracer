import argparse
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser(description='Type racer cheater')
parser.add_argument('--link', help='Url link to server')
args = parser.parse_args()

caps = DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings'] = True

driver = webdriver.Ie(
    "C:\\Users\\jpoisson\\Downloads\\IEDriverServer_Win32_2.53.0\\IEDriverServer.exe"
)

def main():
  if not args.link:
    print 'Please supply link'
    sys.exit()
  driver.get(args.link)

  print 'test'

  # join_game = WebDriverWait(driver, 180).until(
  #   EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "join"))
  # )
  # join_game.click()
  while True:
    runLoop()

def runLoop():
  join_game = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located((By.CLASS_NAME, "lightLabel"))
  )
  waitForCountdownToFinish()
  text_array = buildTextString()
  print text_array
  text_array.reverse()
  input_box = driver.find_element_by_class_name('txtInput')
  while text_array:
    input = text_array.pop()
    input_box.send_keys(input)
    input_box.send_keys(" ")


def waitForCountdownToFinish():
  print 'in light label'
  try:
    while True:
      driver.find_element_by_class_name('lightLabel')
  except:
    return

def buildTextString():
  first_word = driver.find_element_by_xpath('//*[contains(@id, "nhwMiddlegwt-uid")]')
  first_word = first_word.text

  rest_of_string = driver.find_element_by_xpath('//*[contains(@id, "nhwRightgwt-uid")]')
  rest_of_string = rest_of_string.text
  print rest_of_string
  string_array = rest_of_string.split(" ")

  string_array.insert(0, first_word)

  print string_array
  return string_array


if __name__ == '__main__':
  main()

# ID nhwMiddlegwt-uid-10 for first word
# ID nhwRightgwt " words... end. "
