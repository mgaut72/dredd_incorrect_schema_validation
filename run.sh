python api.py &

sleep 5

dredd ./apiary.apib http://localhost:5000 -d

kill $(pgrep python)


