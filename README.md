# trellis-law-interview

# backend
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
python manage.py runserver


# frontend
cd frontend
yarn
yarn serve



http://localhost:8080

# Notes
- This is far from production grade.
- Local dev will work, but the proxy rewrite would break in upper environment
- I can CSS, but time was a factor. Completed this in a few hours last night and one this morning.
- At 2am the numbers math started getting foggy, probably not the optimal solution, but it works.
- This was my first ground up Vue 'project'. I mostly review PRs in vue and do some light debugging or component fixup.
- My django is similar position, but with Django Rest Framework on top.
- This was fun, thanks.
- Usually my commits are smaller.
- Testing is a thing I can do, but not illustrated here.