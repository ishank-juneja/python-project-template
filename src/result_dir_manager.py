import os


# A path (or disk location) consists of an absolute path and a relative path
class MyPath:
    def __init__(self, pth, abspth):
        # Hold relative path
        self.pth = pth
        # Hold absolute path for above path
        self.abspth = abspth


# Class to translate between absolute and relative paths while reading/writing
# programmatically generated results in python scripts
# User specifies a human readable loc_name for every location of interest and a relative path for the location initially
# Later while using user only deals with convenient loc_name while absolute and relative paths are handled internally
class ResultDirManager:
    # Optionally initialize file_paths manager object as
    def __init__(self):
        # Dict to hold folder types and the (relative) path locations of those folder types
        # Example {'imgs': 'results/images', 'arrays': 'data/arrays_folder'}
        self.mypaths = {}
        # Dict to hold folder types and the absolute path locations of those folder types
        # Example {'imgs': 'home/ishank/Desktop/project/results/images',
        # 'arrays': 'home/ishank/Desktop/project/data/arrays_folder'}
        self.myabspaths = {}
        # Get absolute current working directory
        self.mycwd = os.getcwd()
        # My locations/keys
        self.mylocs = []

    # Takes a relative path name and location and creates a dir if there is none
    def add_location(self, loc_name: str, loc_rel_pth: str, make_dir_if_none: bool = True):
        self.mylocs.append(loc_name)
        # Assemble absolute path for loc_rel_pth
        abs_loc_pth = os.path.join(self.mycwd, loc_rel_pth)
        # Check if loc_dir actually exists and is a dir, if not make the folder
        if not os.path.isdir(abs_loc_pth) and make_dir_if_none:
            os.makedirs(abs_loc_pth)
        # Add to dicts
        self.mypaths[loc_name] = loc_rel_pth
        # Add to abs dicts
        self.mypaths[loc_name] = loc_rel_pth
        return

    def loc_exists(self, loc_name: str):
        if loc_name in self.mylocs:
            return True
        else:
            raise KeyError("Unknown location name {0} for dict with keys {1}".format(loc_name, self.mylocs))

    # Get the relative path for a certain location name
    def get_rel_path(self, loc_name: str):
        if self.loc_exists(loc_name):
            return self.mypaths[loc_name]

    # Get the abs path for a certain location name
    def get_abs_path(self, loc_name: str):
        if self.loc_exists(loc_name):
            return self.myabspaths[loc_name]

    # Courtesy: https://stackoverflow.com/questions/17984809/how-do-i-create-an-incrementing-filename-in-python
    # Finds the next free path in a sequentially named list of files via exponential search
    def next_path(self, loc_name: str, prefix: str, postfix: str):
        if self.loc_exists(loc_name):
            pass
        # Append default or custom postfix to prefix
        # Example prefix = 'trajplt' and postfix = '-%s.png' to assemble file names of the form trajplt-i.png, i \in N
        name_w_pattern = prefix + postfix
        full_pattern_pth = os.path.join(self.get_abs_path(loc_name), name_w_pattern)
        i = 1
        # First do an exponential search for what files already exist
        while os.path.exists(full_pattern_pth % i):
            i = i * 2
        # Result lies somewhere in the interval (i/2..i]
        # We call this interval (a..b] and narrow it down until a + 1 = b
        a, b = (i // 2, i)
        while a + 1 < b:
            c = (a + b) // 2  # interval midpoint
            a, b = (c, b) if os.path.exists(full_pattern_pth % c) else (a, c)
        return full_pattern_pth % b

    # Scrapes a location (folder) to find files exactly matching a certain prefix
    # In the file names everything except for the prefix should be an integer
    def scrape_loc_for_prefix(self, loca_name: str, prefix: str):
        #TODO: Write in conjuntion with scraping the folder in run.py