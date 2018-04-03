#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import luigi


class Download(luigi.Task):
    url = luigi.Parameter()
    path = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.filename)

    def run(self):
        urllib.request.urlretrieve(self.url, self.path)


class ExtractDataset(luigi.Task):
    def requires(self):
        for fold in range(5):
            filename = f'atis.fold{fold}.pkl.gz'
            path = f'data/{filename}'
            url = f'http://lisaweb.iro.umontreal.ca/transfert/lisa/users/mesnilgr/atis/{filename}'
            yield Download(url=url, path=path)
