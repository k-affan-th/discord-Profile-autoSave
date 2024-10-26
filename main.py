# %% [markdown]
# # 1. Import the list of ID from 'data' folders

# %%
# Create the empty list to store the list of IDs
ids = []
log_msg = []

# Open the file IDs, Read it and Store in list
try:
    with open('data/IDs.txt', 'r') as f:
        ids = f.read().split('\n')
except:
    log_msg.append(f'\n>> PLEASE INSERT ID list in `data/IDs.txt`')

log_msg.append(f'\n\nLoading ID list (#{len(ids)}):\n{ids}')

# %% [markdown]
# # 2. Import and Initial the driver

# %%
from selenium import webdriver
from selenium.webdriver.edge.options import Options

edgeOption = Options()
edgeOption.add_argument('--headless=new')
edgeOption.add_argument("--log-level=3")
edgeOption.add_experimental_option("excludeSwitches", ["enable-logging"])
log_msg.append("\nSet Edge WebDriver with headless options.")

# Initialize the WebDriver and Open the webpage
driver = webdriver.Edge(options=edgeOption)
log_msg.append("Edge WebDriver initialized.")


driver.get('https://toolscord.com/')
log_msg.append("Opened webpage: https://toolscord.com/")

# %% [markdown]
# # 3. Get information of avatar URL and Account name 

# %%
try:
    from data.script.AvatarInfo import getAvatarByIDs
    log_msg.append("Loaded Avatar info script.")
except Exception as e:
    log_msg.append(e)
    driver.close()
    exit()

avatar_infos = getAvatarByIDs(driver, ids)
log_msg.append(f'\navatar_infos:')
for i, item in enumerate(avatar_infos.items()):
    log_msg.append(f'   {i}:  {item}')

# %% [markdown]
# # 4. Save file and handle the same file in output folder

# %%
try:
    from os import makedirs
    from data.script.download_img import *
    log_msg.append("\nLoaded download images script.")
except Exception as e:
    log_msg.append(e)
    driver.close()
    exit()

new_file_counter = 0
for index, user in enumerate(avatar_infos.keys()):
    path = f'data/output/{user}/'
    makedirs(path, exist_ok=True)

    temp_path = 'data/output/temp/'
    # Check if the temp directory exists
    if not os.path.exists(temp_path):
        makedirs(temp_path, exist_ok=True)

    name, avatar_url = [x for x in avatar_infos[user].values()]
    filename = f"[{name}] {avatar_url.split('/')[-1].split('?')[0]}"

    avatar_temp_file = f'{temp_path}{filename}.jpeg'
    avatar_correct_path = f'{path}{filename}.jpeg'

    
    download_image(avatar_url, avatar_temp_file)
    
    try:
        count, msg = check_for_duplicates_and_handle(avatar_temp_file, path)
        new_file_counter += count
        log_msg.append(msg)
    except Exception as e:
        log_msg.append(f'Error {e}')

log_msg.append(f"{'_'*10}\nReport:")
log_msg.append(f'Complete to download and store `{new_file_counter} new file(s)` to output folder.')
print(f"\n{'_'*10}\nReport:")
print(f'Complete to download and store `{new_file_counter} new file(s)` to output folder.')

# %% [markdown]
# ### Close the WebDriver

# %%
driver.close()

# %% [markdown]
# # 5. Report as Log

# %%
import logging
import time

# Create the log directory if it doesn't exist
log_dir = "data/log/"
os.makedirs(log_dir, exist_ok=True)

# Create a timestamp for the log file name
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"{log_dir}{timestamp}.log"

# Configure the logger
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Create a logger instance
logger = logging.getLogger('Dev')

# Log some messages
logger.info('\n'.join(log_msg))

print(f'\n{"_"*10}\nDone, You can see the report at `data/log`.\n')