#---ONLY USE THIS FILE IF YOU WANT TO DELETE THE VECTORDB COLLECTION
#--SUCH AS:WHEN ADDING NEW DATA SO THAT CHUNKING IS PERFORMED AGAIN AND,
#  NOT USED FROM COLLECTION
# (IN SHORT AFTER DELETING WHEN YOU RUN MAIN.PY EMBEDDINGS WILL BE CREATED AND WILL POPULATE THE CHROMADB COLLECTION)
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from chroma_DB.chroma_client import get_chroma_client

client = get_chroma_client()
client.delete_collection(name="linuxDB")
print("Collection deleted!")
