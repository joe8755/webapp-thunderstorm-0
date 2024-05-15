#from opentelemetry import trace
#from opentelemetry import metrics

from flask import Flask, request
import platform
import psutil
import psycopg2
import datetime
#import logging

app = Flask(__name__)

# Version 1
@app.route('/v1')
def version1():
    return "Hello World"

# Version 2
@app.route('/v2')
def version2():
    os_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Processor": platform.processor(),
        "CPU Usage": psutil.cpu_percent(interval=1)
    }
    return os_info

# Version 3
@app.route('/v3')
def version3():
    # Logging access to the site to PostgreSQL
    access_time = datetime.datetime.now()
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mPIUBTe1Uo",
        host="my-release-postgresql.default.svc.cluster.local",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO access_logs (access_time, remote_addr, request_url) VALUES (%s, %s, %s)", (access_time, request.remote_addr, request.url))
    conn.commit()
    cur.close()
    conn.close()
    return "Access logged successfully"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
