import nlpcloud
class NLPAPI:
    def __init__(self):
        pass
        

    def sentiment_api(self,text):
        client = nlpcloud.Client("gpt-oss-120b", "8fd75ae81f6b8ca135168fd2b2f72b91b17b4b56", gpu=True)
        response  = client.sentiment(text,target="NLP Cloud")

        return response
    
    def translate_api(self,text,lang):
        

        client = nlpcloud.Client("nllb-200-3-3b", "8fd75ae81f6b8ca135168fd2b2f72b91b17b4b56", gpu=False)
        response = client.translation(text, source="", target=lang)
        return response
    

    def ner_api(self,text,entity):
        
        
        client = nlpcloud.Client("gpt-oss-120b", "8fd75ae81f6b8ca135168fd2b2f72b91b17b4b56", gpu=True)
        response = client.entities(text, searched_entity=entity)

        return response