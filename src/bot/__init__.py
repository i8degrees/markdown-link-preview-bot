# src/bot/__init__.py:jeff
#

import importlib.util
from importlib.machinery import SourceFileLoader

def load_mod(module_name, file_path):
    # Works even if the target file has a non-standard extension or no extension
    loader = SourceFileLoader(module_name, str(file_path))
    spec = importlib.util.spec_from_loader(module_name, loader)

    if spec is not None:
        module = importlib.util.module_from_spec(spec)
        loader.exec_module(module)
        return module
    raise ImportError(f"Could not load script at {file_path}")

util = load_mod("util", "./src/util/util.py")
