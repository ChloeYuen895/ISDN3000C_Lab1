# MarkdownPress - A Simple Static Site Generator
This project converts Markdown files into a static HTML website.

Go to project directory with
```powershell
cd path\markdown-press
```

Create virutal environment
```powershell
py -3.11 -m venv venv
```
Activate virtual environment
```powershell
.\venv\Scripts\activate
```

Install all the libraries with 
```powershell
pip install -r requirements.txt
```

To run the code
```powershell
py main.py
```
After running the code check the public folder for the generated html files
```
markdown-press/
├── public
    ├── about.html
    ├── index.html
```