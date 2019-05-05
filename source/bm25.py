import db
import configfile as cfile
from math import log


def idf(n, df):
    return log(
        (n - df + 0.5)
        / (df + 0.5)
    )


def bm25(document_id, term, k, b):
    document_count = len(db.DB)

    assert 1 <= term <= 2, 'Invalid term'
    assert 0 <= document_id < document_count, 'Invalid document_id'

    average_document_length = db.DB.document_length.sum()
    current_document_length = db.DB.document_length[document_id]

    term_header = 'freq_word_{}'.format(term)
    documents_containing_term_count = len(
        db.DB[db.DB[term_header] != 0]
    )
    term_frequency = db.DB[term_header][document_id]

    inverse_doc_freq = idf(document_count, documents_containing_term_count)
    numerator = term_frequency * (k + 1)
    denominator = term_frequency + k * (1 - b + b * current_document_length / average_document_length)

    return inverse_doc_freq * (numerator / denominator)


if __name__ == '__main__':
    cfg = cfile.get_config()
    for i in range(5):
        print('[+] BM25 for document {}: {:.4f}'.format(
            i, bm25(i, 1, **cfg) + bm25(i, 2, **cfg)
        ))
