# flask-app-vercel

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)

Flask application templates hosted on Vercel, included with unit testing and Python modules.

## Structure 📂
```
flask-app-vercel
├── .github
├── handlers
├── modules
├── static
│   ├── images
│   ├── scripts
│   └── styles
├── templates
├── tests
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
└── vercel.json
```
- [.github](.github/) is a folder that used to place Github related stuff, like CI pipeline.
- [handlers](handlers/) contain handler to handling HTTP request methods.
- [modules](modules/) contain the main modules of the app.
- [static](static/) contain static files like images, CSS, and JavaScript files.
- [templates](templates/) contain the file that will be rendered for display in the browser.
- [tests](tests/) contain unit test of the app.
- [.gitignore](.gitignore) is a file to exclude some folders like venv.
- [LICENSE](LICENSE) is a file that contains the license used in this app.
- [README.md](README.md) is the file you are reading now.
- [app.py](app.py) is the main file of this app.
- [requirements.txt](requirements.txt) is a file that contains a list of dependencies used in this app.
- [vercel.json](vercel.json) is a file that contains configuration and override the default behavior of Vercel.

## Installation 🛠️
- Clone the repository:
```
git clone https://github.com/putuwaw/flask-app-vercel.git
```
- Create a virtual environment:
```
python -m venv venv
```
- Activate virtual environment:
```
source venv/Scripts/activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Run app:
```
python app.py
```
- Run test:
```
pytest
```
