mkdir djangogirls
cd djangogirls
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install --upgrade django
pip install pylint
pip install djangorestframework
pip install django-pwa
pip install -r requirements.txt
pip freeze > requirements.txt

django-admin.exe startproject mysite .
python manage.py startapp blog
python manage.py migrate
python manage.py runserver
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py createsuperuser

# Git
git init
git config --global user.name "Steven"
git config --global user.email sjpearce@gmail.com
git remote add origin https://github.com/Pearcee/my-first2-blog.git
git push -u origin master
git pull
git push

git status
git add --all .
git commit -m "99%"
git push

python manage.py startapp api
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

git commit -m "steve"
git push

python manage.py startapp article


python manage.py startapp pages

Last note

cd A:\GIT\djangogirls\pages\static\css\images
$source_photo = "trees.jpg"
$destination = "trees.jpg"
$scale = 30
Resize-Image -InputFile $source_photo -Scale $scale -OutputFile $destination+$scale  -Verbose

python manage.py startapp stevelanding
