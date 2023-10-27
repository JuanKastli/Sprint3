echo. ##############TEST PATH #############
cd ./src/data/Tests
python -m pytest alertas.py Registro.py Formato.py --html=../Results/KastliJuan.html --self-contained-html
pause

