"""
Downloads the following:
- Stanford parser
- Stanford POS tagger
- Glove vectors
- SICK dataset (semantic relatedness task)
- Stanford Sentiment Treebank (sentiment classification task)

"""

from __future__ import print_function
import urllib2
import sys
import os
import shutil
import zipfile
import gzip

def download(url, dirpath):
    filename = url.split('/')[-1]
    filepath = os.path.join(dirpath, filename)
    try:
        u = urllib2.urlopen(url)
    except:
        print("URL %s failed to open" %url)
        raise Exception
    try:
        f = open(filepath, 'wb')
    except:
        print("Cannot write %s" %filepath)
        raise Exception
    try:
        filesize = int(u.info().getheaders("Content-Length")[0])
    except:
        print("URL %s failed to report length" %url)
        raise Exception
    print("Downloading: %s Bytes: %s" % (filename, filesize))

    downloaded = 0
    block_sz = 8192
    status_width = 70
    while True:
        buf = u.read(block_sz)
        if not buf:
            print('')
            break
        else:
            print('', end='\r')
        downloaded += len(buf)
        f.write(buf)
        status = (("[%-" + str(status_width + 1) + "s] %3.2f%%") %
            ('=' * int(float(downloaded) / filesize * status_width) + '>', downloaded * 100. / filesize))
        print(status, end='')
        sys.stdout.flush()
    f.close()
    return filepath

def unzip(filepath):
    print("Extracting: " + filepath)
    dirpath = os.path.dirname(filepath)
    with zipfile.ZipFile(filepath) as zf:
        zf.extractall(dirpath)
    os.remove(filepath)

def download_tagger(dirpath):
    tagger_dir = 'stanford-tagger'
    if os.path.exists(os.path.join(dirpath, tagger_dir)):
        print('Found Stanford POS Tagger - skip')
        return
    url = 'http://nlp.stanford.edu/software/stanford-postagger-2015-01-29.zip'
    filepath = download(url, dirpath)
    zip_dir = ''
    with zipfile.ZipFile(filepath) as zf:
        zip_dir = zf.namelist()[0]
        zf.extractall(dirpath)
    os.remove(filepath)
    os.rename(os.path.join(dirpath, zip_dir), os.path.join(dirpath, tagger_dir))

def download_parser(dirpath):
    parser_dir = 'stanford-parser'
    if os.path.exists(os.path.join(dirpath, parser_dir)):
        print('Found Stanford Parser - skip')
        return
    url = 'http://nlp.stanford.edu/software/stanford-parser-full-2015-01-29.zip'
    filepath = download(url, dirpath)
    zip_dir = ''
    with zipfile.ZipFile(filepath) as zf:
        zip_dir = zf.namelist()[0]
        zf.extractall(dirpath)
    os.remove(filepath)
    os.rename(os.path.join(dirpath, zip_dir), os.path.join(dirpath, parser_dir))

def download_wordvecs(dirpath):
    if os.path.exists(dirpath):
        print('Found Glove vectors - skip')
        return
    else:
        os.makedirs(dirpath)
    url = 'http://www-nlp.stanford.edu/data/glove.840B.300d.zip'
    unzip(download(url, dirpath))

def download_sst(dirpath):
    if os.path.exists(dirpath):
        print('Found SST dataset - skip')
        return
    url = 'http://nlp.stanford.edu/~socherr/stanfordSentimentTreebank.zip'
    parent_dir = os.path.dirname(dirpath)
    unzip(download(url, parent_dir))
    os.rename(
        os.path.join(parent_dir, 'stanfordSentimentTreebank'),
        os.path.join(parent_dir, 'sst'))
    shutil.rmtree(os.path.join(parent_dir, '__MACOSX')) # remove extraneous dir

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # data
    data_dir = os.path.join(base_dir, 'data')
    wordvec_dir = os.path.join(data_dir, 'glove')
    sst_dir = os.path.join(data_dir, 'sst')

    # libraries
    lib_dir = os.path.join(base_dir, 'lib')

    # download dependencies
    download_tagger(lib_dir)
    download_parser(lib_dir)
    download_wordvecs(wordvec_dir)
    download_sst(sst_dir)
