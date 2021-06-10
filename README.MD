# How to run 

Run locally as
 
```
python3 run.py
```

Produces on my machine: 


```
❯ python3 run.py 
[nltk_data] Downloading package stopwords to /home/artur/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
[nltk_data] Downloading package punkt to /home/artur/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
Took: 221.904
Took: 74.512
Took: 72.9
Took: 75.799
Took: 73.905
Took: 74.02
Took: 74.952
Took: 74.097
Took: 74.42999999999999
Took: 74.09100000000001
```

Build on docker and run: 

```
docker build . -t slow_runner
docker run slow_runner
```

Produces on my machine: 


```
❯ docker run slow_runner
[nltk_data] Downloading package stopwords to /root/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
[nltk_data] Downloading package punkt to /root/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
Took: 488.0
Took: 119.86
Took: 120.099
Took: 121.837
Took: 120.134
Took: 118.04299999999999
Took: 121.629
Took: 120.025
Took: 120.975
Took: 120.01599999999999
```

 
