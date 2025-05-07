import time
import html
import requests
from functools import wraps
from dataclasses import dataclass, field
from lxml import etree
from typing import Optional, List, Any, Generator, Tuple
import subprocess
import json
import os
import sys
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

try:
    import orjson as json
    JSON_LIB_USED = "orjson"
except ImportError:
    import json
    JSON_LIB_USED = "standard json"

cookies = {
    'mid': 'Z58xlAABAAHzDxO3N95qadJWbLkA',
    'datr': 'lDGfZ6xOHOklymM1llgwAk8P',
    'ig_did': 'EA8A4FE6-5870-48C6-A124-71326FE4083C',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'csrftoken': 'hzWAR712MJ3qudh1z5jsJOfSbK2L9tnu',
    'dpr': '2.4749999046325684',
    'sessionid': '51941737982%3AACAwFjDUA8GSyA%3A6%3AAYd8M-XOIgyH4ie088IUU89mRl3xKpyMhd23moCH4A',
    'ds_user_id': '51941737982',
    'wd': '980x1890',
    'rur': '"HIL\\05451941737982\\0541777947410:01f7005ce8ae3e688c7ed174f0c8afeb4a84f16394058334d72a8daedc4ebd20eb49c25b"'
}

headers = {
    'Host': 'www.instagram.com',
    'Connection': 'keep-alive',
    'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.50", "Chromium";v="133.0.6943.50"',
    'sec-ch-ua-platform': '"Linux"',
    'X-Root-Field-Name': 'xdt_api__v1__feed__user_timeline_graphql_connection',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-mobile': '?0',
    'X-IG-App-ID': '936619743392459',
    'X-FB-LSD': 'j8aO14g-mApYuvTg6vqIVl',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-CSRFToken': 'hzWAR712MJ3qudh1z5jsJOfSbK2L9tnu',
    'X-FB-Friendly-Name': 'PolarisProfilePostsQuery',
    'X-BLOKS-VERSION-ID': '446750d9733aca29094b1f0c8494a768d5742385af7ba20c3e67c9afb91391d8',
    'X-ASBD-ID': '359341',
    'sec-ch-prefers-color-scheme': 'light',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'DNT': '1',
    'sec-ch-ua-platform-version': '""',
    'Accept': '*/*',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/_ragava_d_k_/',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ta;q=0.6'
}

data = {
    'av': '17841451899472717',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '7',
    '__hs': '20213.HYP:instagram_web_pkg.2.1...1',
    'dpr': '3',
    '__ccg': 'GOOD',
    '__rev': '1022509427',
    '__s': 'fnn0ze:12ikyb:piv58t',
    '__hsi': '7500780228313674370',
    '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0DU2wx609vCwjE1EE2Cw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2swtUd8-U2zxe2GewGw9a361qwuEjUlwhEe87q0oa2-azqwt8d-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlA3a3zhA6bwIxeUnAwHxW1oxe6UaU3cyUC4o16Usw',
    '__csr': 'ggMT8zjMWgZcAh58YyiuJFEJmFBmBtnRTuBppWh6_KCmjgJ3pRDK8BWx6DhdkBSiFby49nAECFA8BJbAFadAcTy9UlKaCxBeagLF8C4UGjKm8Jeil4J7AK48XQKK8yaJeaDzVpUHiVHhA6FEOV9bUhzGAAzWhrBV4Wxqm9LVRG211eexa7oXU01iSUkS0bBxKU15o8o21onDw4gDw6twYK1yw1eO04u8apBe1Cw8u5U2PCKq2C2x46pE3_yki581E82Gc11w4wDO0go4N1qeoLQ6EeNhQaAoOuFU9A1By8G3hwt80KO1fxS6Ei811xUODg6qpa71pAaBg06LW0r-0fSw',
    '__hsdp': 'l0MgAB2O9Ej-oYlaRD2USlk55J5GD94T6QCLk7QwK4ER2vF0wQ8zMwsgfwlhg9Ugwty0Fx-fx0wFebzU4lDBg9-aCVocUiwn8K18yp61KwFBwGK2G6o8FUhw2iU39wGg1i83Oxy3C1YwPw964Eco8o5W261OxO1nxKm1gwUwi8K2ShlJof8iwDwkUK1vwlo2AWUV0BGE2gwXwFy4',
    '__hblpi': '045wdW0YE3Sx6bwnUbKaCVo4q1syU4y9wtoapoaHwrU0BS0OoaA0ky0YEowVwv8cU2hxa36261uwxwsEswlU7a3y18yUbp5mRwYxa2u1jyU5-1lwajHzA2mGw923K2C8g',
    '__hblpn': '0mU4616weW0WU5-2y9x25o4q1kwAxa9G2O6u17wwy8gyEvzqyUS3q2a5ocUiwiUvwemU1XU4K12yEeUnwsqw4Ywde0hWq14Ay8pw951m1Vw_DwGwr86m2ycy8-2Wi13wCwkE6-0GEf982awoEK',
    '__comet_req': '7',
    'fb_dtsg': 'NAcNc5Rsvo26XYHJThmB8wcmChfDUBAETGIkHLGKAwICy2McDEV_ylw:17865379441060568:1746375030',
    'jazoest': '26191',
    'lsd': 'j8aO14g-mApYuvTg6vqIVl',
    '__spin_r': '1022509427',
    '__spin_b': 'trunk',
    '__spin_t': '1746411488',
    '__crn': 'comet.igweb.PolarisProfilePostsTabRoute',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisProfilePostsQuery',
    'variables': '{"data":{"count":5,"include_reel_media_seen_timestamp":true,"latest_reel_media":true},"username":"_ragava_d_k_","__relay_internal__pv__PolarisIsLoggedInrelayprovider":true,"__relay_internal__pv__PolarisShareSheetV3relayprovider":true}',
    'server_timestamps': 'true',
    'doc_id': '9654017011387330',
}

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"DEBUG: [{func.__name__}] executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@dataclass(frozen=True)
class StreamUrls:
    video_url: Optional[str] = None
    audio_url: Optional[str] = None

@dataclass(frozen=True)
class ClipInfo:
    clip_id: Optional[str] = None
    pk: Optional[str] = None
    mpd_manifest: Optional[str] = None
    title: str = ""
    description: str = ""
    timestamp: int = 0
    
class InstagramClipExtractor:
    def __init__(self, json_data: bytes | str | dict):
        self.raw_json_data = json_data
        self._parsed_data: Optional[dict] = None
        self._latest_clip_node: Optional[dict] = None
        print(f"INFO: Using {JSON_LIB_USED} for JSON parsing.")

    @timing_decorator
    def _parse_json(self) -> None:
        if self._parsed_data is not None:
            return

        try:
            if isinstance(self.raw_json_data, (bytes, bytearray)):
                self._parsed_data = json.loads(self.raw_json_data)
            elif isinstance(self.raw_json_data, str):
                self._parsed_data = json.loads(self.raw_json_data)
            elif isinstance(self.raw_json_data, dict):
                self._parsed_data = self.raw_json_data
            else:
                raise TypeError("Input must be JSON string, bytes, or dict")
        except (json.JSONDecodeError, TypeError) as e:
            print(f"ERROR: Failed to parse JSON data: {e}")
            self._parsed_data = None

    @staticmethod
    def _get_nodes_with_manifest(data: dict) -> Generator[dict, None, None]:
        """Generator yielding feed nodes that contain a video dash manifest."""
        if not data:
            return
        edges: List[dict] = data.get("data", {})\
                                .get("xdt_api__v1__feed__user_timeline_graphql_connection", {})\
                                .get("edges", [])

        for edge in edges:
            node = edge.get("node")
            if node and node.get("video_dash_manifest") and node.get("caption"):
                yield node

    @timing_decorator
    def find_latest_clip_node(self) -> Optional[dict]:
        if self._latest_clip_node:
            return self._latest_clip_node

        self._parse_json()
        if not self._parsed_data:
            return None
        latest_node_info = max(
            (
                (node.get("caption", {}).get("created_at", 0), node)
                for node in self._get_nodes_with_manifest(self._parsed_data)
            ),
            key=lambda item: item[0],
            default=(0, None)
        )

        timestamp, node = latest_node_info
        if timestamp > 0 and node:
            print(f"DEBUG: Found latest clip node - Timestamp: {timestamp}")
            self._latest_clip_node = node
            return node
        else:
            print("DEBUG: No suitable video node found in JSON.")
            self._latest_clip_node = None
            return None

    def extract_clip_info_from_node(self, node: Optional[dict]) -> ClipInfo:
        if not node:
            return ClipInfo() # Return default empty ClipInfo

        full_text = node.get("caption", {}).get("text", "")
        split_text = full_text.split('#', 1)
        title = split_text[0].strip().replace('\n', ' ') or "No Title"
        desc = ('#' + split_text[1].replace('\n', ' ').strip()) if len(split_text) > 1 else "No Hashtags"

        return ClipInfo(
            clip_id=node.get("code"),
            pk=node.get("pk"),
            mpd_manifest=node.get("video_dash_manifest"),
            title=title + " #bgmi #bgmitamil #fyp #funny",
            description=desc,
            timestamp=node.get("caption", {}).get("created_at", 0)
        )

    @staticmethod
    @timing_decorator
    def extract_stream_urls_from_mpd(mpd_content: Optional[str]) -> StreamUrls:
        """Parses MPD manifest and extracts highest quality stream URLs."""
        if not mpd_content:
            return StreamUrls()

        try:
            parser = etree.XMLParser(recover=False, resolve_entities=False)
            if isinstance(mpd_content, str):
                mpd_bytes = mpd_content.encode('utf-8')
            elif isinstance(mpd_content, bytes):
                mpd_bytes = mpd_content
            else:
                raise TypeError("MPD content must be string")

            root = etree.fromstring(mpd_bytes, parser)

            best_video = (-1, None)
            best_audio = (-1, None)
            for adaptation_set in root.xpath('//*[local-name()="AdaptationSet"]'):
                content_type = adaptation_set.get("contentType", "").lower()

                valid_reps = (
                    (int(rep.get("bandwidth", 0)), rep.find('.//{*}BaseURL'))
                    for rep in adaptation_set.xpath('.//*[local-name()="Representation"]')
                    if rep.get("bandwidth", "").isdigit() and rep.find('.//{*}BaseURL') is not None
                )

                if content_type == "video":
                    current_best = max(valid_reps, key=lambda x: x[0], default=(-1, None))
                    if current_best[0] > best_video[0]:
                         best_video = (current_best[0], html.unescape(current_best[1].text.strip()))

                elif content_type == "audio":
                    current_best = max(valid_reps, key=lambda x: x[0], default=(-1, None))
                    if current_best[0] > best_audio[0]:
                        best_audio = (current_best[0], html.unescape(current_best[1].text.strip()))


            print(f"DEBUG: Best Video - BW: {best_video[0]}, URL: {best_video[1]}")
            print(f"DEBUG: Best Audio - BW: {best_audio[0]}, URL: {best_audio[1]}")
            return StreamUrls(video_url=best_video[1], audio_url=best_audio[1])

        except (etree.XMLSyntaxError, TypeError) as e:
            print(f"ERROR: Failed processing MPD content: {e}")
            return StreamUrls()
        except Exception as e:
            print(f"ERROR: Unexpected error during MPD processing: {e}")
            return StreamUrls()

def setup_driver():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("-profile")
    options.add_argument("za73pwwo.default")
    service = Service("/usr/local/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(5)
    return driver

def wait_and_click(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.click()
    except TimeoutException:
        raise TimeoutException(f"Timeout waiting for element to be clickable: {locator}")

def set_video(driver, locator, keys, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.send_keys(keys)
    except TimeoutException:
        raise TimeoutException(f"Timeout waiting for element to be clickable: {locator}")

def wait_and_send_keys(driver, locator, keys, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(keys)
    except TimeoutException:
        raise TimeoutException(f"Timeout waiting for element: {locator}")

def click_next_buttons(driver, num_clicks):
    next_button_locator = (By.XPATH, "//ytcp-button[@id='next-button']/ytcp-button-shape")
    for _ in range(num_clicks):
        wait_and_click(driver, next_button_locator)
        time.sleep(8)

def upload_video(driver, video_path, title, description):
    try:
        driver.get("https://www.youtube.com")
        time.sleep(10)
        wait_and_click(driver, (By.XPATH, "//*[@id=\"buttons\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"))
        time.sleep(3)
        wait_and_click(driver, (By.CSS_SELECTOR, "ytd-compact-link-renderer:nth-of-type(1) div:nth-of-type(2) > yt-formatted-string:nth-of-type(1)"))
        set_video(driver, (By.XPATH, "//*[@id=\"content\"]/input"), video_path)
        time.sleep(20)
        wait_and_send_keys(driver, (By.CSS_SELECTOR, "div.title ytcp-social-suggestion-input > div"), title)
        time.sleep(5)
        wait_and_send_keys(driver, (By.CSS_SELECTOR, "div.description ytcp-social-suggestion-input > div"), description)
        time.sleep(5)
        wait_and_click(driver, (By.CSS_SELECTOR, "ytkc-made-for-kids-select tp-yt-paper-radio-button:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1)"))
        time.sleep(8)
        click_next_buttons(driver, 3)
        wait_and_click(driver, (By.CSS_SELECTOR, "tp-yt-paper-radio-button:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1)"))
        time.sleep(8)
        wait_and_click(driver, (By.XPATH, "//ytcp-button[@id='done-button']/ytcp-button-shape"))
        time.sleep(8)
    except TimeoutException as e:
        print(f"ERROR: {e}")
        driver.save_screenshot("upload_error.png")
        raise
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        driver.save_screenshot("upload_error.png")
        raise
        
# --- 4. Main Execution Logic ---
@timing_decorator
def main():
    try:
        print("INFO: Fetching data from Instagram API...")
        response = requests.post(
            'https://www.instagram.com/graphql/query',
            cookies=cookies,
            headers=headers,
            data=data
        )
                
        if response.status_code != 200:
            print(f"ERROR: API request failed with status {response.status_code}")
            return
        extractor = InstagramClipExtractor(response.content)

        latest_node = extractor.find_latest_clip_node()

        if latest_node:
            clip_info = extractor.extract_clip_info_from_node(latest_node)

            if clip_info.mpd_manifest:
                stream_urls = extractor.extract_stream_urls_from_mpd(clip_info.mpd_manifest)

                if stream_urls.video_url and stream_urls.audio_url:
                    output_file = f"{clip_info.clip_id}.mp4"
                    print(f"INFO: Downloading video and audio to '{output_file}'...")
                    ffmpeg_cmd = [
                        "ffmpeg",
                        "-i", stream_urls.video_url,
                        "-i", stream_urls.audio_url,
                        "-c", "copy",
                        output_file
                    ]
                    try:
                        subprocess.run(ffmpeg_cmd, check=True, capture_output=True)
                        print("INFO: Download complete.")
                    except subprocess.CalledProcessError as e:
                        print(f"ERROR: FFmpeg failed: {e.stderr.decode()}")
                else:
                    print("ERROR: Could not download, missing video or audio URL.")
                print(f"\n--- Results ---")
                print(f"📹 Highest Quality Video: {stream_urls.video_url or 'Not Found'}")
                print(f"🔊 Highest Quality Audio: {stream_urls.audio_url or 'Not Found'}")
                print(f"\n📌 Metadata:")
                print(f"ID: {clip_info.clip_id}\nPK: {clip_info.pk}")
                print(f"📝 Title: {clip_info.title}")
                print(f"🏷️ Description: {clip_info.description}")
                print(f"🕒 Timestamp: {clip_info.timestamp}")
                driver = setup_driver()
                try:
                    video_path = f"{clip_info.clip_id}.mp4"
                    upload_video(driver, video_path, clip_info.title, clip_info.description)
                    print("Video uploaded successfully")
                finally:
                    driver.quit()
            else:
                print("❌ Clip node found, but it's missing the MPD manifest.")
        else:
            print("❌ No suitable clip node found in the JSON data.")

    except requests.exceptions.RequestException as e:
            print(f"ERROR: HTTP request failed - {str(e)}")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred in main: {e}")
        
if __name__ == "__main__":
    main()
