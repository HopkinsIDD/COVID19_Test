import pytest
import os
import subprocess
import multiprocessing

def a_test(test_dir):
    os.chdir(test_dir)
    subprocess.run(["make", "clean"])

    # Make Makefile
    cmd = ["Rscript", "../COVIDScenarioPipeline/R/scripts/make_makefile.R",
            "-c", f"config.yml",
            "-p", "../COVIDScenarioPipeline",
            "-n", str(multiprocessing.cpu_count())]
    complete = subprocess.run(cmd)
    assert complete.returncode == 0
    assert os.path.exists("Makefile")

    # Run the Makefile
    cmd = ["make"]
    complete = subprocess.run(cmd)
    assert complete.returncode == 0

def teardown_function(self):
    subprocess.run(["make", "clean"])
    os.chdir("..")

def test_1():
    a_test("test1")

def test_importation():
    a_test("test_importation")
