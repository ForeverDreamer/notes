import json
from pprint import pprint as pp

from db_conn import mongo_client

db_name = 'mongodb_example'


def init_db():
    with mongo_client(db_name) as client:
        # client.drop_database(db_name)
        d = client.get_default_database()
        # with open('persons.json', 'rb') as f:
        #     persons = json.load(f)
        # d['persons'].insert_many(persons)
        with open('170-array-data.json', 'rb') as f:
            friends = json.load(f)
        d['friends'].insert_many(friends)


# init_db()


def using_the_aggregation_framework_161(persons):
    # items = mongo_site.db['user_login_times'].aggregate([
    #     {'$match': {'$and': [{'time': {'$gte': time_from}}, {'time': {'$lt': time_to}}]}},
    #     {'$group': {'_id': {'user_id': "$user_id"}, 'login_times': {'$sum': 1}}},
    #     {'$sort': {'login_times': -1}},
    #     # {'$project': {'time': 1}}
    # ])
    female_cursor = persons.aggregate([
        {'$match': {'gender': 'female'}}
    ])
    for female in female_cursor:
        pp(female)
        break


def understanding_the_group_stage_162(persons):
    person_cursor = persons.aggregate([
        {'$match': {'gender': 'female'}},
        {'$group': {'_id': {'state': '$location.state'}, 'total_persons': {'$sum': 1}}}
    ])
    pp(list(person_cursor))


def diving_deeper_into_the_group_stage_163(persons):
    person_cursor = persons.aggregate([
        {'$match': {'gender': 'female'}},
        {'$group': {'_id': {'state': '$location.state'}, 'total_persons': {'$sum': 1}}},
        {'$sort': {'total_persons': -1}}
    ])
    pp(list(person_cursor))


def working_with_project_164(persons):
    person_cursor = persons.aggregate([
        # {'$project': {'_id': 0, 'gender': 1, 'fullname': {'$concat': ['Hello', 'World']}}},
        # {'$project': {'_id': 0, 'gender': 1, 'fullname': {'$concat': ['$name.first', ' ', '$name.last']}}},
        {
            '$project': {
                '_id': 0,
                'gender': 1,
                # 'fullname': {'$concat': [{'$toUpper': '$name.first'}, ' ', {'$toUpper': '$name.last'}]},
                'fullname': {
                    '$concat':
                        [
                            {'$toUpper': {'$substrCP': ['$name.first', 0, 1]}},
                            {'$substrCP': ['$name.first', 1, {'$subtract': [{'$strLenCP': '$name.first'}, 1]}]},
                            ' ',
                            {'$toUpper': {'$substrCP': ['$name.last', 0, 1]}},
                            {'$substrCP': ['$name.last', 1, {'$subtract': [{'$strLenCP': '$name.last'}, 1]}]},
                        ]
                }
            }
        },
    ])
    pp(list(person_cursor))


def turning_the_location_into_a_geojson_object_165(persons):
    person_cursor = persons.aggregate([
        {
            '$project': {
                '_id': 0,
                'email': 1,
                'location': {
                    'type': 'Point',
                    'coordinates': [
                        {'$convert': {'input': '$location.coordinates.longitude', 'to': 'double', 'onError': 0.0, 'onNull': 0.0}},
                        {'$convert': {'input': '$location.coordinates.latitude', 'to': 'double', 'onError': 0.0, 'onNull': 0.0}}
                    ]
                }
            }
        },
        # {
        #     '$project': {
        #         'email': 1,
        #         'location': 1,
        #     }
        # },
    ])
    pp(list(person_cursor))


def transforming_the_birthdate_166(persons):
    person_cursor = persons.aggregate([
        {
            '$project': {
                '_id': 0,
                'name': 1,
                'email': 1,
                'birthdate': {'$convert': {'input': '$dob.date', 'to': 'date'}},
                'age': '$dob.age',
            },

        },
        # {'$count': "num_of_persons"},
        {'$sort': {'age': -1}},
        {'$skip': 100},
        {'$limit': 5},
    ])
    pp(list(person_cursor))


def using_shortcuts_for_transformations_167(persons):
    person_cursor = persons.aggregate([
        {
            '$project': {
                '_id': 0,
                'name': 1,
                'email': 1,
                'birthdate': {'$toDate': '$dob.date'},
                'age': '$dob.age',
            },
        },
        {'$limit': 5},
    ])
    pp(list(person_cursor))


def understanding_the_isoweekyear_operator_168(persons):
    person_cursor = persons.aggregate([
        {
            '$project': {
                '_id': 0,
                'birthdate': {'$toDate': '$dob.date'},
            },
        },
        {'$group': {'_id': {'birthyear': {'$isoWeekYear': '$birthdate'}}, 'num_of_persons': {'$sum': 1}}},
        {'$sort': {'num_of_persons': -1}}
    ])
    pp(list(person_cursor))


def pushing_elements_into_newly_created_arrays_170(friends):
    friend_cursor = friends.aggregate([
        {'$group': {'_id': {'age': '$age'}, 'all_hobbies': {'$push': '$hobbies'}}},
    ])
    pp(list(friend_cursor))


def understanding_the_unwind_stage_171(friends):
    friend_cursor = friends.aggregate([
        {'$unwind': '$hobbies'},
        {'$group': {'_id': {'age': '$age'}, 'all_hobbies': {'$push': '$hobbies'}}},
    ])
    pp(list(friend_cursor))


def eliminating_duplicate_values_172(friends):
    friend_cursor = friends.aggregate([
        {'$unwind': '$hobbies'},
        {'$group': {'_id': {'age': '$age'}, 'all_hobbies': {'$addToSet': '$hobbies'}}},
    ])
    pp(list(friend_cursor))


def using_projection_with_arrays_173(friends):
    friend_cursor = friends.aggregate([
        # {'$project': {'_id': 0, 'examscore': {'$slice': ['$examScores', 1]}}},
        {'$project': {'_id': 0, 'examscore': {'$slice': ['$examScores', -2]}}},
        # {'$project': {'_id': 0, 'examscore': {'$slice': ['$examScores', 2, 1]}}},
    ])
    pp(list(friend_cursor))


def getting_the_length_of_an_array_174(friends):
    friend_cursor = friends.aggregate([
        {'$project': {'_id': 0, 'num_of_scores': {'$size': '$examScores'}}},
    ])
    pp(list(friend_cursor))


def using_the_filter_operator_175(friends):
    friend_cursor = friends.aggregate([
        {'$project': {
            '_id': 0,
            'scores': {'$filter': {'input': '$examScores', 'as': 'sc', 'cond': {'$gt': ['$$sc.score', 60]}}}
        }},
    ])
    pp(list(friend_cursor))


def applying_multiple_operations_to_our_array_176(friends):
    friend_cursor = friends.aggregate([
        {'$unwind': '$examScores'},
        {'$project': {'_id': 1, 'name': 1, 'age': 1, 'score': '$examScores.score'}},
        {'$group': {'_id': '$_id', 'name': {'$first': '$name'}, 'maxscore': {'$max': '$score'}}},
        {'$sort': {'maxscore': -1}},
    ])
    pp(list(friend_cursor))


def understanding_bucket_177(persons):
    person_cursor = persons.aggregate([
        {
            '$bucket': {
                'groupBy': '$dob.age',
                'boundaries': [18, 30, 40, 50, 60, 80],
                'output': {
                    'num_of_persons': {'$sum': 1},
                    'average_age': {'$avg': '$dob.age'},
                    # 'names': {'$push': '$name.first'}
                }
            }
        },
    ])
    pp(list(person_cursor))
    print('===========================================')
    person_cursor = persons.aggregate([
        {
            '$bucketAuto': {
                'groupBy': '$dob.age',
                'buckets': 5,
                'output': {
                    'num_of_persons': {'$sum': 1},
                    'average_age': {'$avg': '$dob.age'},
                    # 'names': {'$push': '$name.first'}
                }
            }
        },
    ])
    pp(list(person_cursor))


def diving_into_additional_stages_178(persons):
    person_cursor = persons.aggregate([
        {'$match': {'gender': 'male'}},
        {
            '$project': {
                '_id': 0,
                'name': {'$concat': ['$name.first', ' ', '$name.last']},
                'birthdate': {'$toDate': '$dob.date'}
            }
        },
        {'$sort': {'birthdate': 1}},
        {'$skip': 10},
        {'$limit': 10},
    ])
    pp(list(person_cursor))


def writing_pipeline_results_into_a_new_collection_180(persons):
    person_cursor = persons.aggregate([
        {
            '$project': {
                '_id': 0,
                'email': 1,
                'location': {
                    'type': 'Point',
                    'coordinates': [
                        {'$convert': {'input': '$location.coordinates.longitude', 'to': 'double', 'onError': 0.0,
                                      'onNull': 0.0}},
                        {'$convert': {'input': '$location.coordinates.latitude', 'to': 'double', 'onError': 0.0,
                                      'onNull': 0.0}}
                    ]
                }
            }
        },
        {
            '$project': {
                'email': 1,
                'location': 1,
            }
        },
        {'$out': {'db': db_name, 'coll': 'transformedPersons'}}
    ])
    pp(list(person_cursor))


def update_addfields(friends):
    friend_cursor = friends.aggregate([
        {'$match': {'name': 'Max'}},
        {'$addFields': {'f1': 1, 'f2': ['hello', 'world'], 'f3': {'k': 'v'}}},
    ])
    pp(list(friend_cursor))


def update_replaceroot(friends):
    # friend_cursor = friends.aggregate([
    #     {'$replaceRoot': {'newRoot': {'k1': 'v1', 'k2': 'v2'}}},
    # ])
    # friend_cursor = friends.aggregate([
    #     {'$match': {'name': 'Max'}},
    #     {'$replaceRoot': {'newRoot': {'$mergeObjects': [{'_id': '$_id', 'name': '$name', 'age': '$age'}]}}},
    # ])
    # friend_cursor = friends.aggregate([
    #     {'$unwind': "$examScores"},
    # ])
    friend_cursor = friends.aggregate([
        {'$unwind': "$examScores"},
        {'$match': {'examScores.score': {'$gte': 60}}},
        {'$replaceRoot': {'newRoot': '$examScores'}},
    ])
    pp(list(friend_cursor))


with mongo_client(db_name) as client:
    coll = client.get_default_database()['persons']
    # using_the_aggregation_framework_161(coll)
    # understanding_the_group_stage_162(coll)
    # diving_deeper_into_the_group_stage_163(coll)
    # working_with_project_164(coll)
    # turning_the_location_into_a_geojson_object_165(coll)
    # transforming_the_birthdate_166(coll)
    # using_shortcuts_for_transformations_167(coll)
    # understanding_the_isoweekyear_operator_168(coll)
    # coll = client.get_default_database()['friends']
    # pushing_elements_into_newly_created_arrays_170(coll)
    # understanding_the_unwind_stage_171(coll)
    # eliminating_duplicate_values_172(coll)
    # using_projection_with_arrays_173(coll)
    # getting_the_length_of_an_array_174(coll)
    # using_the_filter_operator_175(coll)
    # applying_multiple_operations_to_our_array_176(coll)
    # understanding_bucket_177(coll)
    # diving_into_additional_stages_178(coll)
    writing_pipeline_results_into_a_new_collection_180(coll)
    # update_addfields(coll)
    # update_replaceroot(coll)
