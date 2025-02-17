#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import argparse
import pickle
import numpy as np


def check_if_should_pause(tag):
    fname = tag + '.pause.pkl'
    ret = False
    if os.path.exists(fname):
        s = pickle.load(open(tag + '.pause.pkl', 'rb'))
        if s == 'pause':
            ret = True
        os.remove(fname)
    return ret


def pause_trainer(args):
    fname = args.tag + '.pause.pkl'
    if os.path.exists(fname):
        os.remove(fname)
    pickle.dump('pause', open(fname, 'wb'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='training')
    parser.add_argument('--tag', type=str, nargs='?', default='default')
    args = parser.parse_args()

    pause_trainer(args)
