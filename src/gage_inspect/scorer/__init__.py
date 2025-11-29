from gage_inspect.patch import patch_task_dataset

from ._match import match

# Intended side effect of using any scorer is to support decoupled
# datasets
patch_task_dataset()

__all__ = [
    "match",
]
