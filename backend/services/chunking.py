from langchain_text_splitters import RecursiveCharacterTextSplitter

#here we have used the two separate method for chunking, one without overlapping some chunk data and anther with overlapping
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
