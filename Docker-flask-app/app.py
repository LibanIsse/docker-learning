From flask import Flask
Import Redis

app = Flask (__name__)
r = redis.Redis(host='Redis', port=5002)

@app.route('/')
def welcome ():
    return 'Welcome to coderco challenge'

@app.route('/')
def count ():
    count = r.incr('visits')
    return f'This page has been visited {count} times.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002 )
    