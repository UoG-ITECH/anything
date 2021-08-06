# 5012-ITECH

### How to run app locally on your machine


1. Clone the repository

`git clone https://github.com/UoG-ITECH/itech-5012.git`
   
2. Go inside the directory and crate a virtual environment

`git python3 -m venv anyname_for_virtualenviornment`

3. You see newly created virtual environment inside the directory
   

4. Make sure you do not see anything when `pip freeze` is executed
   

5. Install dependencies listed inside `requirements.txt`

`pip install -r requirements.txt`
   
6. Using python3, makemigrate and apply the migration to the app

`python3 manage.py makemigrations rango`

`python3 manage.py migrate`

`python3 manage.py runserver`

---
### How to test app
Simply run the command in terminal

`python3 manage.py test --pattern="tests.py"`


---

### Contributed by our team

* Jose Mendoza 2607752M
* Hwisun Bae 2587100B
* Ramón Martínez Fernández 2593406M