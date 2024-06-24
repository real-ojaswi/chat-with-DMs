import warnings
from langchain_community.embeddings import HuggingFaceEmbeddings   

warnings.filterwarnings('ignore')
# Specify the model name and additional arguments
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device' : 'cpu'}
encode_kwargs = {'normalize_embeddings': True}

# Initialize HuggingFace Embeddings
hfembeddings = HuggingFaceEmbeddings(
    model_name = model_name,
    model_kwargs = model_kwargs,
    encode_kwargs = encode_kwargs
)