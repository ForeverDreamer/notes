from elasticsearch import Elasticsearch

es = Elasticsearch('http://192.168.71.20:9200')


def info():
    return es.info()


def cluster_health():
    return es.cluster.health()


def cat_indices(show_all=False):
    params = {'v': 'true'}
    if show_all:
        params['expand_wildcards'] = 'all'
    return es.cat.indices(params=params)


def cat_nodes():
    return es.cat.nodes(params={'v': 'true'})


def cat_shards():
    return es.cat.shards(params={'v': 'true'})


def create_index(index, body):
    return es.indices.create(index=index, body=body)


def close_index(index):
    return es.indices.close(index=index)


def open_index(index):
    return es.indices.open(index=index)


def delete_index(index):
    return es.indices.delete(index=index)


def get_mapping(index):
    return es.indices.get_mapping(index=index)


def put_mapping(body, index):
    return es.indices.put_mapping(body=body, index=index)


def get_settings(index):
    return es.indices.get_settings(index=index)


def put_settings(body, index):
    return es.indices.put_settings(body=body, index=index)


def add_document(index, doc_id, body):
    return es.index(index=index, id=doc_id, body=body)


def replace_document(index, doc_id, body):
    return es.index(index=index, id=doc_id, body=body)


def update_document(index, doc_id, body):
    return es.update(index=index, id=doc_id, body=body)


def get_document(index, doc_id):
    return es.get(index=index, id=doc_id)


def search_document(index, body):
    return es.search(index=index, body=body)


def analyze(index, body):
    return es.indices.analyze(index=index, body=body)


def explain(index, doc_id, body):
    return es.explain(index=index, id=doc_id, body=body)


def pp_tokens(res):
    print(', '.join([t['token'] for t in res['tokens']]))
