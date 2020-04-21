@echo off

rem Record the reference at some point in time
copy /y baseline-java.java current-java.java >nul
lizard current-java.java -o reference-report.csv

rem Some changes have been made. Measure again
copy /y baseline-java-improved-with-badnew.java current-java.java >nul
lizard current-java.java -o new-report.csv

rem Check if the measurement is ok
python ../comparecyclo.py 3 new-report.csv reference-report.csv
if ERRORLEVEL 1 (echo Ok- check failed for new complex code as expected) else (echo Unexpected!)

del current-java.java
del reference-report.csv
del new-report.csv

rem ------------------------------------------------

rem Record the reference at some point in time
copy /y baseline-python.py current-python.py >nul
lizard current-python.py -o reference-report.csv

rem Some changes have been made. Measure again
copy /y baseline-python-degrade-with-goodnew.py current-python.py >nul
lizard current-python.py -o new-report.csv

rem Check if the measurement is ok
python ../comparecyclo.py 3 new-report.csv reference-report.csv
if ERRORLEVEL 1 (echo Ok- check failed for degrade as expected) else (echo Unexpected!)

del current-python.py
del reference-report.csv
del new-report.csv

rem ------------------------------------------------

rem Record the reference at some point in time
copy /y baseline-cpp.cpp current-cpp.cpp >nul
lizard current-cpp.cpp -o reference-report.csv

rem Some changes have been made. Measure again
copy /y baseline-cpp-improved-with-goodnew.cpp current-cpp.cpp >nul
lizard current-cpp.cpp -o new-report.csv

rem Check if the measurement is ok
python ../comparecyclo.py 3 new-report.csv reference-report.csv
if ERRORLEVEL 0 (echo Ok- check passed for improvement as expected) else (echo Unexpected!)
