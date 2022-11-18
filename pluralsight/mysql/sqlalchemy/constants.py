CONNECTION_STRING = "{dialect}+{driver}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
     dialect="mysql",
     driver="mysqldb",
     user="root",
     passwd="my-secret-pw",
     host="localhost",
     port="3306",
     db_name="examples",
)
