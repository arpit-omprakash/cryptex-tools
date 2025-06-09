import importlib
import pathlib
import glob
import os 

# Directory containing all cipher modules
CIPHERS_DIR = pathlib.Path(__file__).parent.parent / "ciphers"

def list_ciphers():
    """
    List all available cipher modules based on file names.

    Returns:
        list[str]: List of cipher module names (without .py extension).
    """
    return [
        f.stem
        for f in CIPHERS_DIR.glob("*.py")
        if not f.stem.startswith("_") and f.stem != "__init__"
    ]

def load_ciphers():
    """
    Load all cipher modules and return a dictionary mapping cipher names to modules.

    Returns:
        dict[str, module]: Dictionary mapping lowercase cipher names to their modules.
    """
    cipher_files = glob.glob(os.path.join(CIPHERS_DIR, "*.py"))
    ciphers = {}
    for path in cipher_files:
        mod_name = os.path.splitext(os.path.basename(path))[0]
        if mod_name.startswith("__"):
            continue
        # Dynamically import the cipher module
        mod = importlib.import_module(f"src.cryptex_tools.ciphers.{mod_name}")
        info = mod.get_info()
        ciphers[info["name"].lower()] = mod
    return ciphers

def load_cipher_module(name):
    """
    Dynamically import a cipher module by name.

    Args:
        name (str): The name of the cipher module (without .py extension).

    Returns:
        module: The imported cipher module.
    """
    return importlib.import_module(f"..ciphers.{name}", package=__package__)

def get_cipher_info():
    """
    Collect metadata from all cipher modules.

    Returns:
        list[dict]: List of metadata dictionaries for each cipher.
    """
    info_list = []
    for cipher_name in list_ciphers():
        module = load_cipher_module(cipher_name)
        if hasattr(module, "get_info"):
            info = module.get_info()
            info["id"] = cipher_name  # e.g., 'caesar'
            info_list.append(info)
    return info_list
