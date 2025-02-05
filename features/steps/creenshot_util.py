import os

def take_screenshot(context, step_name, screenshots_dir="./screenshots"):
    try:

        # Tạo thư mục nếu chưa tồn tại
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Tạo ảnh chụp màn hình
        screenshot_file = os.path.join(screenshots_dir, f"{step_name}.png")
        context.driver.save_screenshot(screenshot_file)

    except Exception as e:
        print(f"Error while saving screenshot: {e}")
