import luigi
from fpck.tasks.is13.train import Train


def test_load():
    luigi.build([Train(fold=0)], scheduler_host='luigi')
