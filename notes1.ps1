git clone https://github.com/Pearcee/my-first2-blog.git
python -m venv venv
python -m pip install --upgrade pip
pip freeze > requirments.txt
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py createsuperuser


python manage.py makemigrations
python manage.py migrate

git checkout master
git fetch -p origin
git merge origin/master
git merge master
git push origin

git config --global user.email "sjpearce@gmail.com"
git config --global user.name "Steve"