import functions_framework
import pymysql
import os
from dotenv import load_dotenv

import json
import time


@functions_framework.http
def hello_http(request):
    load_dotenv()

    request_json = request.get_json(silent=True)

    map = {}
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db="Blog",
            cursorclass=pymysql.cursors.DictCursor
        )

        if request_json and 'action' in request_json and request_json['action'] == "put":
            with conn:
                with conn.cursor() as cursor:
                    message = request_json['message']
                    autor = request_json['autor']
                    date = time.strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute("insert into Messages (message,autor,date) values ('{}','{}','{}');".format(
                        message, autor, date))
                    conn.commit()
                    map["message"] = "put executed successfully"
        elif request_json and 'action' in request_json and request_json['action'] == "get":
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("select * from Messages")
                    map["messages"] = []
                    for message in cursor.fetchall():
                        map["messages"].append({
                            "autor": message["autor"],
                            "message": message["message"],
                            "date": message["date"].strftime("%m/%d/%Y, %H:%M"),
                        })

        else:
            map["message"] = "action missing or with wrong value!"
    except Exception as e:
        map["message"] = 'Error: {}'.format(str(e))

    return json.dumps(map)


@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)

    map = {}
    try:
        conn = pymysql.connect(
            host="34.69.13.139",
            # host="34.69.13.141",
            port=3306,
            user="root",
            password="v$a;qgX#8~T3q08G",
            # password="exa844senha",
            db="Blog",
            cursorclass=pymysql.cursors.DictCursor
        )

        if request_json and 'action' in request_json and request_json['action'] == "put":
            with conn:
                with conn.cursor() as cursor:
                    message = request_json['message']
                    autor = request_json['autor']
                    date = time.strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute("insert into Messages (message,autor,date) values ('{}','{}','{}');".format(
                        message, autor, date))
                    conn.commit()
                    map["message"] = "put executed successfully"
        elif request_json and 'action' in request_json and request_json['action'] == "get":
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("select * from Messages")
                    map["messages"] = []
                    for message in cursor.fetchall():
                        map["messages"].append({
                            "autor": message["autor"],
                            "message": message["message"],
                            "date": message["date"].strftime("%m/%d/%Y, %H:%M"),
                        })

        else:
            map["message"] = "action missing or with wrong value!"
    except Exception as e:
        map["message"] = 'Error: {}'.format(str(e))

    return json.dumps(map)
