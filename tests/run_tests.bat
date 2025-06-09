@echo off
echo Running all tests with unittest discovery...

python -m unittest discover -s tests
if errorlevel 1 (
    echo Some tests failed.
    exit /b 1
)

echo All tests passed!
exit /b 0
