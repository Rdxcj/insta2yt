from seleniumbase import SB
with SB(user_data_dir="/app/chrome/google-chrome", headless2=True, uc=True, ad_block=True, incognito=True) as sb:
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