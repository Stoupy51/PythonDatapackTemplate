
# Imports
import os
ROOT: str = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")  # This line gets the full root path to this folder, don't change it unless you know what you're doing.
IGNORE_UNSET: bool = False                          # If True, the program will ignore unset optionnal values in the configuration dictionnary


# Folders
MERGE_FOLDER: str = f"{ROOT}/merge"                 # If a file exists in both merge and build folder, they will be merged. Otherwise, it's just copied.
BUILD_FOLDER: str = f"{ROOT}/build"                 # Folder where the final datapack and resource pack are built
ASSETS_FOLDER: str = f"{ROOT}/assets"               # Folder containing the all assets (textures, sounds, ... folders) for the datapack and resource pack
LIBS_FOLDER: str = f"{ROOT}/libs"                   # The libraries are copied to the build destination, and merged with the datapack using Weld
BUILD_COPY_DESTINATIONS: tuple[list, list] = (["D:/latest_snapshot/world/datapacks"], ["D:/minecraft/snapshot/resourcepacks"])	# Can be empty lists if you don't want to copy the generated files to other folders.


# Dev constants
HAS_MANUAL: bool = True                             # Do the program generate a manual/guide? (WARNING: if an item is malformed in the database, the server log will be flooded on load by the manual hiding the malformed item)
DATABASE_DEBUG: str = f"{ROOT}/database_debug.json" # Dump of the database for debugging purposes
ENABLE_TRANSLATIONS: bool = True                    # Will convert all the text components to translate and generate a lang file in the resource pack. Meaning you can easily translate the datapack in multiple languages!
MERGE_LIBS: bool = True                             # Make new zip of merged libraries with the datapack and resource pack using Smithed Weld


# Project information
AUTHOR: str = "Stoupy51"                # Author(s) name(s) displayed in pack.mcmeta, also used to add convention.debug tag to the players of the same name(s) <-- showing additionnal displays like datapack loading
PROJECT_NAME: str = "Python Datapack Template"          # Name of the datapack, used for messages and items lore
VERSION: str = "1.21.615"               # Project version in the following mandatory format: major.minor.patch, ex: 1.0.0 or 1.21.615
NAMESPACE: str = "your_namespace"       # Simplified version of the datapack name. Used to namespace functions, tags, etc. Should be the same you use in the merge folder.
DESCRIPTION = f"{PROJECT_NAME} [{VERSION}] by {AUTHOR}" # Pack description displayed in pack.mcmeta
DEPENDENCIES: dict[str, dict[str, list[int] | str]] = {
    # Automagically, the datapack will check for the presence of dependencies and their minimum required versions at runtime
    # The url is used when the dependency is not found to suggest where to get it
    # The version dict key contains the minimum required version of the dependency in [major, minor, patch] format
    # The main key is the dependency namespace to check for
    # The name can be whatever you want, it's just used in messages
    
    # Example for DatapackEnergy >= 1.8.0
    #"energy": {"version":[1, 8, 0], "name":"DatapackEnergy", "url":"https://github.com/ICY105/DatapackEnergy"},
}


# Technical constants
SOURCE_LORE: list[dict] = [{"text":"ICON"},{"text":f" {PROJECT_NAME}","italic":True,"color":"blue"}] # Appended lore to any custom item, can be an empty string


# Manual configuration
DEBUG_MODE: bool = False                            # Shows up grids in manual
MANUAL_PATH: str = f"{ROOT}/manual"                 # Cached manual assets
MANUAL_OVERRIDES: str = f"{ASSETS_FOLDER}/manual_overrides" # Path to a folder containing manual overrides to replace the default manual assets
MANUAL_HIGH_RESOLUTION: bool = True                 # Enable the high resolution for the manual to increase the craft resolutions
CACHE_MANUAL_ASSETS: bool = True                    # Caches the MC assets and the items renders for the manual (manual/items/*.png)
CACHE_MANUAL_PAGES: bool = False                    # Caches the content of the manual and the images (manual/pages/*.png)
MANUAL_DEBUG: str = f"{ROOT}/debug_manual.json"     # Dump of the manual for debugging purposes
MANUAL_NAME: str = f"{PROJECT_NAME} Manual"         # Name of the manual, used for the title of the book and first page
MAX_ITEMS_PER_ROW: int = 5                          # Max number of items per row in the manual, should not exceed 6
MAX_ROWS_PER_PAGE: int = 5                          # Max number of rows per page in the manual, should not exceed 6
OPENGL_RESOLUTION: int = 256                        # Resolution of the OpenGL renders used in the manual, best value is 256 <--- 256x256
MANUAL_FIRST_PAGE_TEXT: list[dict] = [{"text":"Modify in config.py the text that will be shown in this first manual page", "color":"#505050"}] # Text for the first page of the manual




# Configuration dictionnary
configuration = {
    "ignore_unset": IGNORE_UNSET,

    "merge_folder": MERGE_FOLDER,
    "manual_path": MANUAL_PATH,
    "build_folder": BUILD_FOLDER,
    "assets_folder": ASSETS_FOLDER,
    "libs_folder": LIBS_FOLDER,
    "build_copy_destinations": BUILD_COPY_DESTINATIONS,
    "has_manual": HAS_MANUAL,
    "debug_mode": DEBUG_MODE,
    "database_debug": DATABASE_DEBUG,
    "cache_manual_assets": CACHE_MANUAL_ASSETS,
    "cache_manual_pages": CACHE_MANUAL_PAGES,
    "manual_debug": MANUAL_DEBUG,
    "enable_translations": ENABLE_TRANSLATIONS,
    "merge_libs": MERGE_LIBS,
    "author": AUTHOR,
    "project_name": PROJECT_NAME,
    "version": VERSION,
    "namespace": NAMESPACE,
    "manual_name": MANUAL_NAME,
    "description": DESCRIPTION,
    "dependencies": DEPENDENCIES,
    "source_lore": SOURCE_LORE,
    "max_items_per_row": MAX_ITEMS_PER_ROW,
    "max_rows_per_page": MAX_ROWS_PER_PAGE,
    "opengl_resolution": OPENGL_RESOLUTION,
    "manual_first_page_text": MANUAL_FIRST_PAGE_TEXT,
    "manual_high_resolution": MANUAL_HIGH_RESOLUTION,
    "manual_overrides": MANUAL_OVERRIDES,
}

