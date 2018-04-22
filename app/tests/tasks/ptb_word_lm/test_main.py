import luigi
from fpck.tasks.ptb_word_lm.main import Train


def test_load():
    luigi.build([Train(fold=0)], scheduler_host='luigi')
