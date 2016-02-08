#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import re


with open('../data/shakespeare.txt') as SHAKESPEARE:
        words = Counter(re.findall('\w+', SHAKESPEARE.read()))

print words.most_common(10)
