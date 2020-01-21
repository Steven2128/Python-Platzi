import os
import logging
logging.basicConfig(level=logging.INFO)
import subprocess
import datetime


logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal', 'bbc']


def main():
    _extract()
    _transform()
    


def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        now = datetime.datetime.now().strftime('%Y_%m_%d')
        subprocess.run(['python', 'main.py', news_site_uid], cwd='./extract')
        os.system('move extract'+'\\'+'{news_site_uid}_{datetime}_articles.csv transform'.format(
        news_site_uid=news_site_uid,
        datetime=now))


def _transform():
    logger.info('Starting transform process')
    for news_site_uid in news_sites_uids:
        now = datetime.datetime.now().strftime('%Y_%m_%d')
        dirty_data_filename = '{news_site_uid}_{datetime}_articles.csv'.format(
        news_site_uid=news_site_uid,
        datetime=now)
        subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
        os.system('move transform\\{news_site_uid}_{datetime}_articles.csv ..\\'.format(
        news_site_uid=news_site_uid,
        datetime=now))



if __name__ == '__main__':
    main()
