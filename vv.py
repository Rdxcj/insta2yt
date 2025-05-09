from seleniumbase import SB
with SB(user_data_dir="/app/chrome/google-chrome", headless2=True, uc=True, ad_block=True) as sb:
  url = "https://www.youtube.com"
  sb.driver.uc_open_with_reconnect(url, 3)
  sb.save_screenshot("/app/yt_screenshot/1.png")
