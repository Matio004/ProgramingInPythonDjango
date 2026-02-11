# Observations
**Observations** is an aplication developed as an assignment for Programing in Python course. It allows user to store, add and delete data which would later be used to predict category of given observation.
Prediction is made using scikit-learn KNeighborsClassifier (before running algorithm data is scaled using StandardScaler).

## Features
1. Application offers simple navigation.
<img width="619" height="65" alt="obraz" src="https://github.com/user-attachments/assets/1aa41477-4d7e-4524-817f-5872ee88c4bd" />

2. Application allows user to display all collected data in readable way. At this point user can also delete chosen record.
<img width="1852" height="892" alt="obraz" src="https://github.com/user-attachments/assets/3ca9f368-4915-4f06-89e4-b93407a8eab5" />

3. Applcation allows adding new observations using form.
<img width="1892" height="927" alt="obraz" src="https://github.com/user-attachments/assets/8a28e95e-7eac-4854-9397-ca63553b8e8f" />

4. Applcation allows runnting predictions. However user must provide enought train data, or else an error would occur.
<img width="1882" height="896" alt="obraz" src="https://github.com/user-attachments/assets/04319f7f-a113-485f-b55f-6145fb18312c" />
<img width="1906" height="662" alt="obraz" src="https://github.com/user-attachments/assets/875d024f-ffd0-442f-a175-3058568343a5" />

5. Application provides an API allowing access to all features without the browser.

## Built with
* **Language**: Python
* **Frameworks and Libraries**: Django, djangorestframework, scikit-learn

## Getting started
1. ```git clone https://github.com/Matio004/ProgramingInPythonDjango.git```
2. ```uv run python manage.py migrate```
3. ```uv run python manage.py runserver --insecure```
