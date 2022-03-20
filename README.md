# Product API

## Project Setup
1. Install Python v3.10.
2. Create a Virtual Environment.
    ```zsh
    python -m venv <environment_name>
    # or
    python3 -m venv <environment_name>
    ```
3. Activate the Environment as per OS.
4. Install Packages.
    ```zsh
    # Poetry
    poetry install
    # pip
    pip install -r requirements.txt
    ```
5. Apply migrations.
    ```zsh
    python manage.py migrate
    ```
6. Create Admin.
    ```zsh
    python manage.py createsuperuser
    ```
7. Run development server.
    ```zsh
    python manage.py runserver
    ```
