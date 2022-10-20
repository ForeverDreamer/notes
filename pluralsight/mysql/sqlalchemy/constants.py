CONNECTION_STRING = "{drivername}+{dbapi}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
     drivername="mysql",
     dbapi="mysqldb",
     user="root",
     passwd="my-secret-pw",
     host="localhost",
     port="3306",
     db_name="examples",
)