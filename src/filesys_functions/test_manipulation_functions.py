from src.filesys_functions.project_safety import DirSafetyException
from pathlib import Path
from src.constants import API_ROOT_DIR
import unittest
from src.filesys_functions.manipulation_functions import touch, rm, mkdir, rmdir

class ManipulationFunctionsTestCase(unittest.TestCase):

    
    def test_touch_and_rm(self):
        filename = 'test_touch.txt'
        
        touched = touch(path=API_ROOT_DIR.joinpath(filename))
        self.assertTrue(touched)
        removed = rm(path=touched)
        self.assertTrue(removed)


    def test_mkdir_and_rmdir(self):
        dirname = 'test_dir'
        with self.assertRaises(DirSafetyException): 
            mkdir(path=Path('../../outside_root_dir'))
        
        madedir = mkdir(path=API_ROOT_DIR / dirname)
        with self.assertRaises(FileExistsError): 
            mkdir(path=madedir)
        
        removed = rmdir(path=madedir)
        with self.assertRaises(FileNotFoundError):
            rmdir(path=removed)
