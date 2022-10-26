import sys
import fire
from libs.find_rc import find_rc

print(f"Hello, I'm Python version: {sys.version}")

if __name__ == "__main__":
  fire.Fire(find_rc)

