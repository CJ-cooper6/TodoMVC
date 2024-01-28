python -m venv venv
source venv/Scripts/activate

pip freeze > requirements.txt
pip install -r requirements.txt

python run.py

#frontend
cd frontend
npm install
npm run dev

#npm config set registry https://registry.npm.taobao.org

pre-commit run --hook-stage commit
