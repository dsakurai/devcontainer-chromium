#!/usr/bin/env python3

from playwright.sync_api import sync_playwright
import os
from pathlib import Path
from datetime import datetime

# Set the download folder to this script's folder
download_folder = Path(__file__).resolve().parent

# Get the current year and month
current_date = datetime.now()
new_file_name = f"{current_date.year}-{current_date.month:02d}.csv"

# URL to open
url = "https://app.getmoneytree.com/app/trends/net-worth"


# Launch Playwright and open the URL in Brave browser
with sync_playwright() as p:

    browser = p.chromium.launch_persistent_context(
        user_data_dir="user-data",
        executable_path="/usr/bin/chromium",
        headless=False,
        accept_downloads=True,
        downloads_path=download_folder
    )
    page = browser.new_page()

    # Notify the user about the download folder
    print(f"Downloads will be saved to: {download_folder}")

    page.goto(url)
    
    # Click on the button with the specified attributes
    button_selector = "div[ui-sref='app.vault'][href='/app/vault']"
    page.click(button_selector)

    # Click on the export button with the specified attributes
    export_button_selector = "button[ng-click='vm.onExportClick(null, credentialAccountMode, vm.transactionsDetails)']"
    # page.click(export_button_selector)

    # Let the user select the date manually
    print("Please select the desired date in the date picker manually.")

    # Define the download button selector
    download_button_selector = "button[ng-click='vm.download()']"

    # Instruct the user and wait for a manual click that triggers a download
    print("Please manually click the download button in the browser.")

    download = page.wait_for_event("download", timeout=0)  # Don't timeout

    print(f"Download started: {download.suggested_filename}")

    # Desired filename
    save_path = os.path.join(download_folder, new_file_name)

    download.save_as(save_path)
    print(f"File saved to: {save_path}")

    # Keep the browser open until manually closed
    # input("Press Enter to close the browser...")
    browser.close()

