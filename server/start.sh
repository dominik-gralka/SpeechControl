clear
pkill screen
screen -dmS server node server.js
screen -dmS hook-daemon ultrahook api 3000/webhook
echo ""
echo "Server and Hook-Daemon successfully started."
echo ""
screen -ls
echo ""