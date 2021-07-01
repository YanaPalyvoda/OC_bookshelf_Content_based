"""
Date : 2021-06-20
Recommends a defined number 
of articles for a user
based on 3 last articles already read
Outputs: Id of the recommended items
"""
import numpy as np 
import pandas as pd 
import shared_code.ContentBasedRecommender as cbr


def get_articles_populaires(article_nb,df_interactions):
    #Computes the most popular items if new user
    item_popularity_df = df_interactions.groupby('article_id')['click_timestamp'].count().sort_values(ascending=False).reset_index()
    return item_popularity_df['article_id'].head(article_nb).to_list()

def get_user_articles(userId,df_interactions):
        # get iteams read by user in the past
        return df_interactions[df_interactions['user_id']==userId][['article_id','click_timestamp']
                                                          ].sort_values(by = 'click_timestamp',
                                                                        ascending=True)['article_id'
                                                                                 ].to_list()

def get_ids_recomended_articles(userId,df_interactions,df_articles,articles_embeddings,article_nb):    
    # load user profile
    data_user = get_user_articles(userId,df_interactions)
    if len(data_user)>0:
        contentBasedRecommender_model = cbr.ContentBasedRecommender(data_user=data_user,df_articles=df_articles,emb_articles=articles_embeddings)
        id_recomended_articles = contentBasedRecommender_model.get_recomended_article(article_nb)
    else:
        # most popular items for the new user
        id_recomended_articles = get_articles_populaires(article_nb,df_interactions)
    return id_recomended_articles
     
