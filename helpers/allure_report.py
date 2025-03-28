import os
import subprocess

def generate_allure_report(results_dir="allure-results", report_dir="allure-report"):
    allure_cmd = "allure.bat" if os.name == "nt" else "allure"

    # flag "--single-file" option, this will instruct Allure to embed all resources into a single index.html file.
    subprocess.run([allure_cmd, "generate", results_dir, "-o", report_dir, "--clean", "--single-file"], check=True)
    return report_dir

def open_allure_report(report_dir="allure-report"):
    allure_cmd = "allure.bat" if os.name == "nt" else "allure"
    
    try:
        subprocess.Popen([allure_cmd, "open", report_dir])
    except Exception as e:
        print(f"⚠️ ERROR opening Allure report: {e}")