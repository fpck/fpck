import subprocess
import os


def test_load():
    cmd = f'luigi --module tasks.is13.load ExtractDataset --local-scheduler'
    ret = subprocess.call(cmd.split(' '))
    assert ret == 1
