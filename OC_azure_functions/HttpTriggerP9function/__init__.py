import logging
import azure.functions as func
import sys
import pandas as pd
from pathlib import Path
from io import BytesIO
import _pickle as cPickle
import sys
import os
#sys.path.append(os.path.abspath(""))
#sys.path.append('../scripts')
#logging.info(Path.cwd())
from shared_code.select_recomended_articles import * 



def main(req: func.HttpRequest, interactionsBlob: func.InputStream,articlesBlob: func.InputStream,embeddingsBlob: func.InputStream) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    articles_embeddings = cPickle.load(BytesIO(embeddingsBlob.read()))
    df_interactions = pd.read_csv(BytesIO(interactionsBlob.read()),index_col=None, header=0)
    df_articles = pd.read_csv(BytesIO(articlesBlob.read()),index_col=None, header=0)
    userId = req.params.get('userId')
    if not userId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userId = req_body.get('userId')

    if userId:
        ids_articles = get_ids_recomended_articles(int(userId),df_interactions,df_articles,articles_embeddings,article_nb=5)
        str_result = ' '.join(str(elem)+"," for elem in ids_articles)
        result = str_result.rstrip(str_result[-1])
        return func.HttpResponse(result)
           
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. userId is not find",
             status_code=200
        )
