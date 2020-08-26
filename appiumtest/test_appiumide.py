from appium import webdriver
desire_scap={
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "automationName":"UiAutomator1",
  "noReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desire_scap)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("albabab")