from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import ReadPreference
from pymongo import WriteConcern

from db_conn import mongo_client


with mongo_client('mongodb://mongo1:27021,mongo2:27022,mongo3:27023/?replicaSet=dbrs') as client:
    wc_majority = WriteConcern("majority", wtimeout=1000)

    # Prereq: Create collections.
    client.get_database("mydb1", write_concern=wc_majority).foo.insert_one({"abc": 0})
    client.get_database("mydb2", write_concern=wc_majority).bar.insert_one({"xyz": 0})

    # Step 1: Define the callback that specifies the sequence of operations to perform inside the transactions.
    def callback(session):
        collection_one = session.client.mydb1.foo
        collection_two = session.client.mydb2.bar

        # Important:: You must pass the session to the operations.
        collection_one.insert_one({"abc": 1}, session=session)
        collection_two.insert_one({"xyz": 999}, session=session)

    # Step 2: Start a client session.
    with client.start_session() as session:
        # Step 3: Use with_transaction to start a transaction, execute the callback, and commit (or abort on error).
        session.with_transaction(
            callback,
            read_concern=ReadConcern("local"),
            write_concern=wc_majority,
            read_preference=ReadPreference.PRIMARY,
        )
