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
        filename = f'atis.fold{self.fold}.pkl.gz'
        path = f'/srv/data/{filename}'
        url = f'http://lisaweb.iro.umontreal.ca/transfert/lisa/users/mesnilgr/atis/{filename}'
        return Download(url=url, path=path)

    def run(self):
        with gzip.open(self.input().path, 'rb') as f:
            train_set, valid_set, test_set, dicts = pickle.load(
                f, encoding='latin1')
        idx2label = dict((k, v) for v, k in dicts['labels2idx'].items())
        idx2word = dict((k, v) for v, k in dicts['words2idx'].items())

        train_lex, train_ne, train_y = train_set
        valid_lex, valid_ne, valid_y = valid_set
        test_lex,  test_ne,  test_y = test_set
        nv, de, cs = 1000, 50, 7
        embeddings = theano.shared(
            0.2 * numpy.random.uniform(-1.0, 1.0, (nv + 1, de)).astype(theano.config.floatX))
        idxs = T.imatrix()
        x = embeddings[idxs].reshape((idxs.shape[0], de * cs))
        f = theano.function(inputs=[idxs], outputs=x)

        sample = numpy.array([0, 1, 2, 3, 4], dtype=numpy.int32)
        csample = contextwin(sample, 7)
        feature = f(csample)
        print(feature.shape)

        #  data = pipe(range(5), lambda x: contextwin(x, 3), list)
