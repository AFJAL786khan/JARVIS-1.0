from langchain.document_loaders import TextLoader
import textwrap

# Import missing modules
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

# Set HuggingFace API token
# os.environ["HUGGINGFACE_API_TOKEN"] = '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'

# Load document
loader = TextLoader('data.txt')
document = loader.load()

# PREPROCESSING
def wrap_text_preserve_newlines(text, width=110):
    lines = text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text

# print(wrap_text_preserve_newlines(str(document[0])))

# TEXT SPLITTING
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(document)

# print(docs[0])
# print(len(docs))

# EMBEDDING
embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(docs, embeddings)

query = "when did afzal born"
doc = db.similarity_search(query)

# print(wrap_text_preserve_newlines(str(doc[0].page_content)))

# Q-A
llm = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temperature": 0.8, "max_length": 512},
    huggingfacehub_api_token="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",
)

chain = load_qa_chain(llm, chain_type="stuff")

query_text = "how many rockets spacex launched"
docsResult = db.similarity_search(query_text)
print(chain.run(input_documents=docsResult, question=query_text))
