# learning_python

private repo for learning python

## setup environment

[reference](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)

[video instruction](https://www.youtube.com/watch?v=31WU0Dhw4sk)

[manage multiple python versions and virtual environments](https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/)

- Set python version for the project

  `pyenv local <version>`

* Create an isolated virtual env:

  ```
  python -m venv <.venv_name>

  source /path/to/env1/bin/activate
  ```

* Switch between venv:

  ```
  /path/to/env/bin/deactivate

  source /path/to/env2/bin/activate
  ```

- Use venv in VSC

  ```
  "python.terminal.activateEnvironment": true
  ```
