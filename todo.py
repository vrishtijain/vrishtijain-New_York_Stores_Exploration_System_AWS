
from config import *

 # dialect+driver://username:password@host:port/database
engine_query = "postgresql+psycopg2://"+ customuser+":"+custompass + "@" + customhost + ":" +  customport+"/" + customdb
print(engine_query)
