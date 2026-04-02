from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_fixed(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0
    )
    return splitter.split_documents(documents)


def chunk_overlap(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)
