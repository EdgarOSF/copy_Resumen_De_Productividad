echo "BUILD START"
python311 -m pip install -r requirements.txt
python311 manage.py collectstatic --noinput --clear
echo "BUILD END"