from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion'] ='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'
desired_caps['automationName']='UiAutomator1'
desired_caps['noreset'] = 'True'
desired_caps['dontStopAppOnReset'] = 'True'
desired_caps['skipDeviceInitialization'] = 'True'
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.back()#返回
driver.back()#返回
driver.quit()