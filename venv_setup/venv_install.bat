python -m venv ..\venv --upgrade-deps --clear
call ..\venv\Scripts\activate
pip install -r ..\requirements.txt -r ..\requirements_dev.txt -r ..\requirements_docs.txt
pause
