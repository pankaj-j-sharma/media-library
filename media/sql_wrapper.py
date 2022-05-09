
from django.db import connection

# raw queries for all diffrent types of data

all_media_query = '''
    select mi.id,mi.path,mi.name,mi.path,mi.size,
    mt.name as "type",
    mc.name as "category" ,
    mi.created_on,
    mu.name as "created_by"
	from Media_Item mi
    inner join Media_Type mt on mt.id=mi.type_id
    inner join Media_User mu on mu.id=mi.[Created By_id]
    inner join Media_Category mc on mc.id=mi.category_id
'''

all_category_query = '''
    select * from Media_Category mc
'''


def get_data_from_db(name, params=None):
    query = None
    if name == 'all_media':
        query = all_media_query
        if params and 'id' in params:
            query += ' where mi.id={id}'.format(id=params['id'])
    elif name == 'all_category':
        query = all_category_query

    with connection.cursor() as cursor:
        cursor.execute(query)
        records = __recordToJson(cursor)
    return records


def __recordToJson(cursor):
    colnames = [x[0] for x in cursor.description]
    tmprec = cursor.fetchall()
    records = []
    for rec in tmprec:
        records.append(dict(zip(colnames, rec)))
    return records
