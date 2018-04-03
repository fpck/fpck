#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..load import Download
import luigi
import gzip
import pickle
import inspect


class Train(luigi.Task):
    fold = luigi.IntParameter(default=0)

    def requires(self):
        filename = f'atis.fold{self.fold}.pkl.gz'
        path = f'/srv/data/{filename}'
        url = f'http://lisaweb.iro.umontreal.ca/transfert/lisa/users/mesnilgr/atis/{filename}'
        return Download(url=url, path=path)

    def run(self):
        with gzip.open(self.input().path, 'rb') as f:
            train_set, valid_set, test_set, dicts  = pickle.load(f, encoding='bytes')
        train_lex, train_ne, train_y = train_set
        valid_lex, valid_ne, valid_y = valid_set
        test_lex,  test_ne,  test_y  = test_set


