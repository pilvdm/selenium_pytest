# Selenium + PyTest Guide
## Requirements and Installations
Run pip install -r requirements.txt

# How to Launch
Run the following from the root directory of the project:\
python -m pytest tests/name_of_test_file

# Writing Tests and Maintenance
- Page object files are located in page_objects, having locator classes and methods to work with the page
- Actual test scenarios with assestions are in the tests folder
- Global configurations and variables are in the config.py file

# Improvements and TODOs
 - Wrap to docker img
 - Embed to be executed in CI/CD
 - Integrate reporting module to Allure
 - Colonize Mars