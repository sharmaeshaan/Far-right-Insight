# OpenRhetoric

The OpenRhetoric project aims to analyse the public communication of prominent figures from across the global political spectrum. 

The project involves using Python to obtain from reliable sources content such as speechs and articles delivered by these figures and run Natural Language Processing (NLP) algorithms on them.

## Figures Analysed So Far

Figure | Data Source
--- | ---
[Joseph Goebbels](https://en.wikipedia.org/wiki/Joseph_Goebbels) | [Calvin College German Propaganda Archive](http://research.calvin.edu/german-propaganda-archive/goebmain.htm)

## System Requirements

OpenRhetoric is built with **Python 3**. The following Python libraries are in use and required to run it:
- [Requests](http://docs.python-requests.org/en/master/user/install/#install)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- [NLTK](https://www.nltk.org/install.html)
- [Matplotlib](https://matplotlib.org/users/installing.html)
- [WordCloud](https://github.com/amueller/word_cloud), an amazing visualization library written in Python by [Andreas Mueller](https://github.com/amueller)

## Running Programs in OpenRhetoric

Every analysed figure has a program which will fetch, analyse and visualize data related to him/her. 

### MacOS and Linux

- Download repository and unzip it to desired location
- Navigate to unzipped folder and open a terminal window
- Run the `.sh` file related to the figure you want to analyse. For example:
```
bash filename.sh
```

## Credits

- [Calvin College](https://calvin.edu/)
- [WordCloud](https://github.com/amueller/word_cloud) by [Andreas Mueller](https://github.com/amueller)
