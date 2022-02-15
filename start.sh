# start nginx
pkill nginx

nginx -e /home/runner/$REPL_SLUG/logs/error.log -c /home/runner/$REPL_SLUG/nginx.conf

# start Flask app
cd backend
python app.py

cd ../frontend
yarn install
yarn run serve
cd ..

#mkdir data
#jupyter notebook --ip 0.0.0.0 --port 8080 --notebook-dir /home/runner/$REPL_SLUG/data