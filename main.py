from flask import Flask, request
import platform
import psutil
import psycopg2

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
    conn = psycopg2.connect(
        dbname="your_database",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO access_logs (timestamp, remote_addr, request_url) VALUES (%s, %s, %s)", (str(request.timestamp), request.remote_addr, request.url))
    conn.commit()
    cur.close()
    conn.close()
    return "Access logged successfully"

if __name__ == '__main__':
    app.run(debug=True)
