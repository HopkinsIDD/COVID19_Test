import pytest
import os
import subprocess
import multiprocessing

def a_test(test_dir):
    # Make Makefile
    cmd = ["Rscript", "COVIDScenarioPipeline/R/scripts/make_makefile.R",
            "-c", f"{test_dir}/config.yml",
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

def test_1():
    a_test("test1")
