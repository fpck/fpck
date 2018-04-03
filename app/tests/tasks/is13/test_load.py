import subprocess
import os


def test_load():
    cmd = f'luigi --module tasks.is13.train Train --local-scheduler --log-level=DEBUG'
    assert subprocess.call(cmd.split(' ')) == 0
