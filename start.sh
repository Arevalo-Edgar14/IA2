# start nginx
pkill nginx

nginx -e /home/runner/$REPL_SLUG/logs/error.log -c /home/runner/$REPL_SLUG/nginx.conf

# start Flask app
cd backend
python app.py

yarn --cwd frontend/ install
yarn --cwd frontend/ run serve

#mkdir data
#jupyter notebook --ip 0.0.0.0 --port 8080 --notebook-dir /home/runner/$REPL_SLUG/data