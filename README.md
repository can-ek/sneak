# Sneak
Throwback to the old phone game in python

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) project and packet manager

## Steps for development

1. Create a new uv project on your computer.

``
uv init your-project-name

cd your-project-name
``

2. Create a virtual environment at the top level of your project directory:

``
uv venv
``

3. Activate the virtual environment:

``
source .venv/bin/activate
``

__You should see (your-project-name) at the beginning of your terminal prompt, for example, mine is: (sneak) xxxxxx@ubuntu sneak %__

4. Add the pygame library as a project dependency:

``
uv add pygame==2.6.1
``

This tells Python that this project requires pygame version 2.6.1.

5. Make sure pygame is installed:

``
uv run -m pygame
``

This will result in an error (the test expects an exit code of 1), but the output will show that pygame is installed.
If you are on WSL, you will probably need to install [VcXsrv](https://vcxsrv.com/) to run pygame.
