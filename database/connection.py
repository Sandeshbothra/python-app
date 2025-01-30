from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Abcd1234@localhost:3306/SurveyTech", echo=True)