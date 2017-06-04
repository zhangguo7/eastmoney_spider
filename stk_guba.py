# -*- coding:utf-8 -*-
import re
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

def get_stks_guba(headers):
    """

    :param headers:
    :return:
    """
    root_url = 'http://guba.eastmoney.com/remenba.aspx'
    res = requests.get(root_url, headers=headers, timeout=3)
    soup = BeautifulSoup(res.text, 'html.parser')
    stk_block = soup.find('div', {'class': 'ngbggulbody'})
    tag_a_lst = stk_block.find_all('a')

    stk_cd_lst = [];stk_name_lst = [];stk_gb_url_lst = []
    for i,tag_a in enumerate(tag_a_lst):
        try:
            stk_cd,stk_name = tag_a.get_text().split(")")
            stk_cd = stk_cd.replace("(","")
        except Exception as e:
            print(tag_a.get_text(),e)
        else:
            if re.match('^600|000|002|300',stk_cd):
                stk_cd_lst.append(stk_cd)
                stk_name_lst.append(stk_name)
                stk_gb_url_lst.append('http://guba.eastmoney.com/list,%s.html' % stk_cd)
        # if i>10:break
    gb_df = pd.DataFrame(data=np.transpose([stk_cd_lst,stk_name_lst,stk_gb_url_lst]),
                         columns=['stk_cd','stk_name','stk_gb_url'])

    return gb_df

if __name__ == '__main__':

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'guba.eastmoney.com',
        'Referer':'http://guba.eastmoney.com/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    }


    gb_df = get_stks_guba(headers)