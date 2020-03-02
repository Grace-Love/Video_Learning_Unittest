#coding:utf-8

import configparser

def readCfg(file_name):
    cfg = configparser.ConfigParser()
    cfg.read(file_name,encoding='utf-8')
    return cfg

if __name__ == '__main__':
    cfg = readCfg('/addUserConfig.cfg')
    print(cfg)
