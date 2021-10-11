python MT-python.py 3 4 >temp1.txt
set /P value=<temp1.txt
echo %value%
python MT-checker-python.py 3 4 %value%
