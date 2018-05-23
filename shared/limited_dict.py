from typing import Any
from collections import OrderedDict

# https://stackoverflow.com/a/2437645
class LimitedSizeDict(OrderedDict):
  def __init__(self, *args: Any, **kwds: Any) -> None:
    self.size_limit = kwds.pop("size_limit", None)
    OrderedDict.__init__(self, *args, **kwds)
    self._check_size_limit()

  def __setitem__(self, key, value):
    OrderedDict.__setitem__(self, key, value)
    self._check_size_limit()

  def _check_size_limit(self) -> None:
    if self.size_limit is not None:
      while len(self) > self.size_limit:
        self.popitem(last=False)
