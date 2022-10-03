CONNECTION_STRING = "{drivername}+{dbapi}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
     drivername="mysql",
     dbapi="mysqldb",
     user="root",
     passwd="my-secret-pw",
     host="192.168.80.129",
     port="3306",
     db_name="examples",
)