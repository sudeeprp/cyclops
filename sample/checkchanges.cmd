@echo off

rem Record the reference at some point in time
copy /y baseline-java.java current-java.java >nul
lizard current-java.java >reference-report.txt

rem Some changes have been made. Measure again
copy /y baseline-java-improved-with-badnew.java current-java.java >nul
lizard current-java.java >new-report.txt

rem Check if the measurement is ok
python ../comparecyclo.py 3 new-report.txt reference-report.txt
if ERRORLEVEL 1 (echo Ok- check failed for new complex code as expected) else (echo Unexpected!)

del current-java.java
del reference-report.txt
del new-report.txt

rem ------------------------------------------------

rem Record the reference at some point in time
copy /y baseline-python.py current-python.py >nul
lizard current-python.py >reference-report.txt

rem Some changes have been made. Measure again
copy /y baseline-python-degrade-with-goodnew.py current-python.py >nul
lizard current-python.py >new-report.txt

rem Check if the measurement is ok
python ../comparecyclo.py 3 new-report.txt reference-report.txt
if ERRORLEVEL 1 (echo Ok- check failed for degrade as expected) else (echo Unexpected!)

del current-python.py
del reference-report.txt
del new-report.txt

rem ------------------------------------------------

rem Record the reference at some point in time
copy /y baseline-cpp.cpp current-cpp.cpp >nul
lizard current-cpp.cpp >reference-report.txt

rem Some changes have been made. Measure again
copy /y baseline-cpp-improved-with-goodnew.cpp current-cpp.cpp >nul
lizard current-cpp.cpp >new-report.txt

rem Check if the measurement is ok
python ../comparecyclo.py 3 new-report.txt reference-report.txt
if ERRORLEVEL 0 (echo Ok- check passed for improvement as expected) else (echo Unexpected!)
