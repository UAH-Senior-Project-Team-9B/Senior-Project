# Development Environment Setup

1. Install Docker:

    - Download and install Docker Desktop appropriate to your OS.
    - Ensure Docker is running before proceeding.

2. Install the "Remote - Containers" extension:

    - Open VSCode and go to the Extensions panel.
    - Search for "ms-vscode-remote.remote-containers" and install it.

3. Reopen in the container:

    - Use the Command Palette (Ctrl+Shift+P) to select "Remote-Containers: Reopen in Container".
    - This launches VSCode in the container context, enabling you to build, run, and debug the application.

# Introduction To Taskfiles

[Taskfile](https://taskfile.dev) is a modern task runner and build tool used in this project. To explore available tasks:

1. List all tasks:

    ```bash
    task --list
    ```

2. Get detailed information about a specific task:
    ```bash
    task <taskname> --summary
    ```

These commands help you understand and execute the automated workflows defined in our `Taskfile.yml`.

Next, I'd recommend running all checks to familiarize yourself with how you should go about running our various automated tests and confirming your local setup is working as expected.

```bash
task check
```
