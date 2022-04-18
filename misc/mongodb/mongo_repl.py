from pprint import pprint as pp

from data_manipulate.db import mongo_client
from data_manipulate.utils import *

# name = 'xiaorui_test'
# name = 'xiaorui_development'
with mongo_client('xiaorui_development') as client:
    db = client.get_default_database()
    # pp(client.server_info())
    # qas = db['qa'].find(
    #             {'$or': [
    #                 {'question.main': {'$regex': '^你'}},
    #                 {'question.similar': {'$regex': '^吃了'}}]
    #             },
    #             {'question': 1}
    #         )
    # pp(list(qas))
    # pp(db['qa_xr1'].count_documents(filter={}))
    pp(list(find(db['qa_xr1'], {'type': {'$exists': False}})))
