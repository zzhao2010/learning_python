from datetime import time
from functools import wraps

def duration(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    t_start = time()
    result = f(*args, **kwargs)
    t_end = time()
    print(f"func: {f.__name__}, args: [{args}, {kwargs}] took: {t_end - t_start} secs")
    return result
  return wrap