from nir.parser import NIRParser
from data.model.documentType import DocumentType
from data.model.document import Document
import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response


'''
Istanza dell'applicazione FastAPI
'''
app = FastAPI()



@app.middleware("http")
async def add_cors_header(request, call_next):

    '''
    Consente di aggiungere l'header "Access-Control-Allow-Origin" alla risposta
    di ogni richiesta HTTP, ovvero consente di effettuare richieste da un
    dominio diverso da quello del server.
    '''

    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"


    return response



@app.get("/{document}/{article}")
def get_article(document: str, article: str):


    parsed: Document = NIRParser.parse(DocumentType(document.upper()))

    try:
        return parsed.get_article_from_id(article).json()
    except:
        return {"Error": "No article found"}


@app.get("/{document}")
def get_list(document: str):
    
    parsed: Document = NIRParser.parse(DocumentType(document.upper()))

    return parsed.get_ids()



if __name__ == "__main__":
    
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)