# Development Environment Setup

1. Install Visual Studio Code:

    - Download and install Visual Studio Code appropriate to your OS.
    - Ensure that you are using the Visual Studio Code terminal when running any commands for the project.

1. Install Docker:

    - Download and install Docker Desktop appropriate to your OS.
    - Ensure Docker is running before proceeding.

1. Install the "Remote - Containers" extension:

    - Open VSCode and go to the Extensions panel.
    - Search for "ms-vscode-remote.remote-containers" and install it.

1. Reopen in the container:

    - Use the Command Palette (Ctrl+Shift+P) to select "Remote-Containers: Reopen in Container".
    - This launches VSCode in the container context, enabling you to build, run, and debug the application.

# Running the Project

1. Setting up the Database:

    - Ensure that your container is running.
    - Enter the command `uv run python manage.py migrate` in your VSCode terminal.
    - Enter the command `uv run python manage.py test_data` in your VSCode terminal.

2. Setting up the CSS:

    - Enter the command `npm run watch:css` in your VSCode terminal.

3. Running the project:

    - Enter the command `uv run python manage.py runserver` in your VSCode terminal

4. Notes about testing data

    - The manager's daily exam is tied to exams of the day that the `uv run python manage.py test_data` command is run, and users can not schedule exams on the current date. So if you need to check the functionality of daily exams on a later date, you will need to run the following commands in your VSCode terminal in order:
        - `uv run python manage.py flush` after running this, it will prompt you and ask if you are sure that you want to flush the database, respond yes.
        - `uv run python manage.py test_data` after this finishes running, your database will be good to go.
    - `test_data` creates users for each of the user types (e.g., Patient, Doctor, Manager, Super Admin)
        - Usernames
            - Patient usernames: `patient`, `patient2`, `patient3`, and `patient4`
            - Doctor usernames: `doctor`, and `doctor2`
            - Manager username: `manager`
            - Super Admin username: `admin`
        - Passwords
            - For Patient, Doctor, and Manager, the passwords are `1234`
            - For the Super Admin, the password is `ABCD_1234`
