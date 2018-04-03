#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import luigi


class Download(luigi.Task):
    url = luigi.Parameter()
    path = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.path)

    def run(self):
        urllib.request.urlretrieve(self.url, self.path)
