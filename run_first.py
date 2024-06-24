import argparse
from prepare_data import get_vector_db

def main():
    parser= argparse.ArgumentParser(description='Create a vector database for your messages')

    parser.add_argument('root', type=str, help='Directory where your message files are stored')
    parser.add_argument('--chunk_size', type=int, default=20, help='Number of messages that you want in a chunk')
    parser.add_argument('--overlap', type=int, default=5, help='Overlap between two message chunks')

    args= parser.parse_args()
    root= args.root
    chunk_size= args.chunk_size
    overlap= args.overlap

    get_vector_db(root, chunk_size, overlap)

if __name__=='__main__':
    main()