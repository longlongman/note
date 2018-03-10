import pymysql


db = pymysql.connect(host="hdm317309136.my3w.com", user="hdm317309136", passwd="hdmpassword123", db="hdm317309136_db", charset="utf8")
cursor = db.cursor()

def input_sql(strsql, flag):
    try:
        cursor.execute(strsql)
        if flag == 0:
            db.commit()
        else:
            return cursor.fetchall()
    except Exception as e:
        print(e)
