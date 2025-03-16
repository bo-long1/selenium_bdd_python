import os
import subprocess

def generate_allure_report(results_dir="reports/allure-results", report_dir="reports/allure-report"):
    allure_cmd = "allure.bat" if os.name == "nt" else "allure"
    
    try:
        subprocess.run([allure_cmd, "generate", results_dir, "-o", report_dir, "--clean"], check=True)
        print(f"✅ Allure Report created at: {report_dir}")
        return report_dir
    except FileNotFoundError:
        print("⚠️ ERROR: Allure not found! Check your installation and PATH.")
        return None
    except Exception as e:
        print(f"⚠️ ERROR generating Allure report: {e}")
        return None

def open_allure_report(report_dir="reports/allure-report"):
    allure_cmd = "allure.bat" if os.name == "nt" else "allure"
    
    try:
        subprocess.Popen([allure_cmd, "open", report_dir])
    except Exception as e:
        print(f"⚠️ ERROR opening Allure report: {e}")
