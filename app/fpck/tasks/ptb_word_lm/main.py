#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..load import Download
import luigi
import gzip
import pickle
import inspect
from cytoolz.curried import pipe, map
import theano.tensor as T
import theano
import numpy


def contextwin(l, win):
    '''
    win :: int corresponding to the size of the window
    given a list of indexes composing a sentence

    l :: array containing the word indexes

    it will return a list of list of indexes corresponding
    to context windows surrounding each word in the sentence
    '''
    assert (win % 2) == 1
    assert win >= 1
    l = list(l)

    lpadded = win // 2 * [-1] + l + win // 2 * [-1]
    out = [lpadded[i:(i + win)] for i in range(len(l))]

    assert len(out) == len(l)
    return out


class Train(luigi.Task):
    fold = luigi.IntParameter(default=0)

    def requires(self):
        filename = f'ptb_dataset.tgz'
        path = f'/srv/data/{filename}'
        url = f'http://www.fit.vutbr.cz/~imikolov/rnnlm/simple-examples.tgz'
        return Download(url=url, path=path)

    def run(self):
        print('running!')
        print(self.input())
