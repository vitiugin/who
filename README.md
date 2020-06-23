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

- Total number of tweets: 6 508 227
- Undefiened number of tweets: 75 184

Top-10 languages in dataset:

| en | es | fr  | it  |  id  | hi | pt   | ca   |  th  | ja   | 
| :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: |
|4 139 337|1 131 755|386 705|90 235|90 235|77 732|77 710|71 133|61 629|48 855|

![](https://github.com/vitiugin/who/blob/master/src/lang_dist.png)
