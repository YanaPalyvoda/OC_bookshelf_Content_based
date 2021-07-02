# OC_bookshelf_Content_based
This repo contains the code to implement a Minimum Viable Product (MVP) of the Recommendation Systems for mobile application using Azure function.

<b>Data</b>

The Dataset used to this project is provided by Globo.com and is available on Kaggle: https://www.kaggle.com/gspmoreira/news-portal-user-interactions-by-globocom#clicks_sample.csv

The dataset contains a sample of user interactions (page views) in G1 news portal from Oct. 1 to 16, 2017, including about 3 million clicks, distributed in more than 1 million sessions from 314,000 users who read more than 46,000 different news articles during that period.

<b>Recomender system</b>

In this project the Content Based recommender system was used.
Content-based recommenders systems suggest similar articles based on a particular article. This system uses the metadata of articles to make these recommendations. The general idea of these recommender systems is that if a person read a particular article, they will also read a similar article. And to recommend this, the system uses the metadata of the user's previous articles.

<b>Content</b>

-	<a href="https://github.com/YanaPalyvoda/OC_bookshelf_Content_based/tree/main/bookshelf">bookshelf:</a> contains the code of the mobile application
  Please refer to the readme file in this folder to setup
  
-	<a href="https://github.com/YanaPalyvoda/OC_bookshelf_Content_based/tree/main/OC_azure_functions">OC_azure_functions:</a> contains the code of the HTTP request AZURE function: requirements file, configuration files and init file and the python code of the Content Based recommender model used by this function.


