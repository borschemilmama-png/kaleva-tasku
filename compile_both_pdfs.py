import os
import subprocess

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

tasks = [
    ('business_model_presentation.html', 'Kaleva_Tasku_Business_Model.pdf'),
    ('presentation.html', 'Kaleva_Tasku_Presentation.pdf')
]

for html_file, pdf_file in tasks:
    html_abs = os.path.abspath(html_file)
    pdf_abs = os.path.abspath(pdf_file)
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw',
        '--virtual-time-budget=5000',
        f'--print-to-pdf={pdf_abs}',
        f'file:///{html_abs.replace(os.sep, "/")}'
    ]
    print(f"Rendering {html_file} -> {pdf_file}...")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if os.path.exists(pdf_abs):
        size = os.path.getsize(pdf_abs)
        print(f"SUCCESS: {pdf_file} created ({size} bytes)")
    else:
        print(f"FAILED: {pdf_file} not found! Stderr: {res.stderr}")
