import os
import subprocess

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('business_model_presentation.html')
pdf_path = os.path.abspath('Kaleva_Tasku_Business_Model.pdf')

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=5000',
    f'--print-to-pdf={pdf_path}',
    f'file:///{html_path.replace(os.sep, "/")}'
]

print("Executing Chrome headless PDF render...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
print("Return code:", res.returncode)

if os.path.exists(pdf_path):
    size = os.path.getsize(pdf_path)
    print(f"SUCCESS: {pdf_path} created with size {size} bytes")
else:
    print("ERROR: PDF was not generated.")
