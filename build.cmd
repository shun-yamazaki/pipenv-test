echo "build start."

rmdir /s /q dist
del requirements.txt

mkdir dist
xcopy /e src dist
pipenv lock -r > requirements.txt
pip install -r requirements.txt -t dist
del requirements.txt

cd dist
rmdir /s /q bin
for /F %%d in ('dir /ad /b /w *dist-info') do rmdir /s /q %%d
cd ..
echo "please zip files in the dist dir."
