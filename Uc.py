from seleniumbase import SB
import time
from sbvirtualdisplay import Display
from seleniumbase import Driver

#display = Display(visible=0, size=(1440, 1880))
#display.start()
with SB(user_data_dir="/app/chrome/google-chrome", headless2=True, uc=True, ad_block=True) as sb:
    url = "https://www.youtube.com"
    sb.activate_cdp_mode(url)
    sb.sleep(15.5)
    sb.cdp.click("//*[@id=\"buttons\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
    sb.sleep(5)
    sb.cdp.save_screenshot("1", "/app/yt_screenshot")
    sb.cdp.click("ytd-compact-link-renderer:nth-of-type(1) div:nth-of-type(2) > yt-formatted-string:nth-of-type(1)")
    sb.sleep(10)
    sb.cdp.save_screenshot("2", "/app/yt_screenshot")
    sb.sleep(15)
    
#    sb.uc_open_with_reconnect(url, 15.111)
#    sb.uc_click("//*[@id=\"buttons\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]", 4.1)
#    time.sleep(9)
#    sb.uc.click("ytd-compact-link-renderer:nth-of-type(1) div:nth-of-type(2) > yt-formatted-string:nth-of-type(1)", 10)
#    time.sleep(7)


#from sbvirtualdisplay import Display
#from seleniumbase import Driver

#display = Display(visible=0, size=(1440, 1880))
#display.start()

#driver = Driver(uc=True, headless=True)
#driver.uc_open_with_reconnect("https://pixelscan.net/", reconnect_time=10)
#time.sleep(10)
#driver.save_screenshot("/app/yt_screenshot/1.png")
#driver.quit()

#display.stop()
