def create_index(es, index, body):
    return es.indices.create(index=index, body=body)


def close_index(es, index):
    return es.indices.close(index=index)


def open_index(es, index):
    return es.indices.open(index=index)


def delete_index(es, index):
    return es.indices.delete(index=index)


def get_mapping(es, index):
    return es.indices.get_mapping(index=index)


def put_mapping(es, body, index):
    return es.indices.put_mapping(body=body, index=index)


def get_settings(es, index):
    return es.indices.get_settings(index=index)


def put_settings(es, body, index):
    return es.indices.put_settings(body=body, index=index)


def add_document(es, index, doc_id, body):
    return es.index(index=index, id=doc_id, body=body)


def replace_document(es, index, doc_id, body):
    return es.index(index=index, id=doc_id, body=body)


def update_document(es, index, doc_id, body):
    return es.update(index=index, id=doc_id, body=body)


def get_document(es, index, doc_id):
    return es.get(index=index, id=doc_id)


def search_document(es, index, body):
    return es.search(index=index, body=body)


def analyze(es, index, body):
    return es.indices.analyze(index=index, body=body)


def explain(es, index, doc_id, body):
    return es.explain(index=index, id=doc_id, body=body)


def pp_tokens(res):
    print(', '.join([t['token'] for t in res['tokens']]))
