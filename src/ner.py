from ckip_transformers.nlp import CkipNerChunker

from .constants import CHINESE_PUNCTUATION

def generate_ner_tags(articles):
    """
    parameters:
        articles : dict
            {article_id: article_text (traditional Chinese)}
    return:
        result : dict
            {article_id: list of ner results}
    """
    # init the model
    ner_model = CkipNerChunker(
        model="albert-base",
        device=0, # cuda 0
    )

    # init texts
    # sorted by id
    texts = [articles[article_id] for article_id in sorted(articles.keys())]


    ner_results = ner_model(
            texts,
            use_delim=True,
            delim_set=CHINESE_PUNCTUATION.split() + ["\n"],
            show_progress=False
        )
    
    result = {}
    for article_id, ner_result in zip(sorted(articles.keys()), ner_results):
        # ner result is of type NERToken
        ner_result_dict = {
            ner.word: ner.ner
            for ner in ner_result
        }
        result[article_id] = ner_result_dict

    return result

