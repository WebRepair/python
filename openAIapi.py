import os
import sys

os.environ['OPENAI_API_KEY'] = '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'


from langchain.document_loaders import TextLoader 
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
 
 
query = sys.argv[1]

 
loader = TextLoader ('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query)) 