#coding:utf-8

import configparser
import os
from oper_cfg import *

def getUrl():

    here_path = os.path.dirname(os.path.abspath(__file__))
    cfg_path = here_path + '/addUserConfig.cfg'
    #print(cfg_path)
    cfg = readCfg(cfg_path)

    url = cfg.get('url','url')

    return url
if __name__ == '__main__':
    print(getUrl())