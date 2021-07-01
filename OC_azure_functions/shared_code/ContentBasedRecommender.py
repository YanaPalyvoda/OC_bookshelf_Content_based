"""
ContentBasedRecommender
Date : 2021-06-20
Recommends a defined number 
of articles for a user
based on 3 last articles already read
"""
import numpy as np 
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel

class ContentBasedRecommender:
    def __init__(self,data_user,df_articles,emb_articles):
        self.data_user = data_user
        self.df_articles = df_articles
        self.emb_articles = emb_articles
        
  
    def _get_index_to_article(self):
        return pd.Series(np.sort(np.unique(self.df_articles['article_id'])))

    def _get_article_to_index(self,index_to_article):
        return pd.Series(data=index_to_article.index, index=index_to_article.values)
        
    def get_recomended_article(self,article_nb):  
        # select the Id of the recommended items by cosine similarity compute
        index_to_article = self._get_index_to_article()
        article_to_index = self._get_article_to_index(index_to_article)
        # select the items read by user
        index_select_articles=[article_to_index[i] for i in self.data_user]
        index_article_ref = article_to_index[self.data_user]        
        emb_all=np.array([self.emb_articles[index_article_ref]])
        nb_art = len(self.data_user)
        # select 3 last articles 
        if nb_art>3:
            emb_all = emb_all[:3:]
        # calcul the mean embedding to 3 last articles 
        emb_ref=(emb_all.sum(axis=0)/nb_art)
        # delete arcicles past read by user
        emb_art=np.delete(self.emb_articles,index_select_articles,0)
        # select similaire items by cosine similarity
        cosine_sim = linear_kernel(emb_ref, emb_art)[0]
        indx_article_similar = (-cosine_sim).argsort()[:article_nb]
        id_recomended_articles = [index_to_article[i] for i in indx_article_similar]
        return id_recomended_articles     

 