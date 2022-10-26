import os
import pathlib

def find_rc(rc_name=".zshrc"):
  # check for ENV variable
  var_name = "RC_DIR"
  rc_dir = os.environ.get(var_name)
  if rc_dir:
    dir_path = pathlib.Path(rc_dir)
    config_path = dir_path / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
      return config_path.as_postix()
  
  # check the current working directory
  config_path = pathlib.Path.cwd() / rc_name
  print(f"Checking {config_path}")
  if config_path.exists():
    return config_path.as_posix()
  
  # check user home directory
  config_path = pathlib.Path.home() / rc_name
  print(f"Checking {config_path}")
  if config_path.exists():
    return config_path.as_posix()
  
  # check directory of this file
  file_path = pathlib.Path(__file__).resolve()
  parent_path = file_path.parent
  config_path = parent_path / rc_name
  print(f"Checking {config_path}")
  if config_path.exists():
    return config_path.posix()
  
  print(f"File {rc_name} has not been found...")
