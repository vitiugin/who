### WHO Twitter influencers analysis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3798212.svg)](https://doi.org/10.5281/zenodo.3798212)

### Launch project

Create new folder:

`$ mkdir who`

`$ cd who`

Create a new virtual environment inside new folder:

`$ python -m venv who`

Activate it:

`$ source who/bin/activate`

Clone repository from github:

`(who) $ git clone https://github.com/vitiugin/who.git`

Install requirements for environment:

`(who) $ pip install -r requirements.txt`

Install a new kernel for Jupyter Notebook:

`(who) $ ipython kernel install --user --name=who`

Create folder for data:

`(who) $ mkdir data`

Download [data](https://doi.org/10.5281/zenodo.3798212 "data") and unzip it in data folder.

###  Information about data

- Total number of tweets: 4 054 411
- Undefiened number of tweets: 30 877

Top-20 languages in dataset:

| en | es | fr  | id  |  it  | th   | ca   | hi   |  pt  | ja   | de   | ar   | ta   | tr   | nl   | pl   | tl   |  ur  | sw   |  el  |
| :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: |
| 64| 16.5 |  6.4| 1.5  | 1.4 |  1.1 | 1.1  | 1.1  | 0.9  | 0.8  | 0.8  |  0.6 |  0.4 |  0.3 | 0.2  | 0.16  | 0.15  | 0.15  | 0.14  | 0.14  |

![](https://github.com/vitiugin/who/blob/master/src/lang_dist.png)
