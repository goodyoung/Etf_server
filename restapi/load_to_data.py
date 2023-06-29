import os,json
import sqlalchemy as sqla
import pandas as pd

class JsonData:
    def __init__(self):
        os.chdir("/Users/goodyoung/Desktop/대학교/Dash")
        with open(f'./.api_keys/secret_homedb.json') as f:
            secrets = json.loads(f.read())
        self.DB_USER, self.DB_PW = secrets['stockmart']['userid'], secrets['stockmart']['password']
        self.engine = sqla.create_engine(f'mysql+pymysql://{self.DB_USER}:{self.DB_PW}@220.121.140.51:3030/financedb')
        
    def getData(self,query):
        query =  sqla.text(query)
        result = pd.read_sql(query, con=self.engine).to_json(orient="records",force_ascii = False)
        parsed = json.loads(result)
        parsedData = json.dumps(parsed,ensure_ascii=False, separators=(',', ':')) 
        return parsedData
        