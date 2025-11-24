# Data Saver Microservice
Data Storage Microservice that uses ZMQ

This microservice stores data sent from a client.
Data is saved persistently to a JSON file, allowing it to be reloaded even after the microservice is closed.
The client provides a menu to:

1) Enter Data
2) View All Data
3) Delete Data
4) Quit

To run:
```
python3 -m venv myenv 
source myenv/bin/activate 
pip install zmq 
```
Terminal 1:\
`python data-saver.py`

Terminal 2:\
`python3 test_client.py`
