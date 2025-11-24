import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")


# Functions 
def save_data():
    data = input("Enter data to store: ")
    request = {"action": "save", "data": data}
    socket.send(json.dumps(request).encode("utf-8"))
    print("SERVER:", socket.recv().decode("utf-8"))

def view_all():
    request = {"action": "get_all"}
    socket.send(json.dumps(request).encode("utf-8"))
    response = socket.recv().decode("utf-8")
    items = json.loads(response)

    if not items:
        print("No data stored yet.")
    else:
        print("\nStored Data:")
        for i, item in enumerate(items):
            print(f"[{i}] {item}")

def delete_item():
    view_all()
    try:
        index = int(input("\nEnter index number to delete: "))
        request = {"action": "delete", "index": index}
        socket.send(json.dumps(request).encode("utf-8"))
        print("SERVER:", socket.recv().decode("utf-8"))
    except ValueError:
        print("Invalid input. Must be a number.")


# Menu Loop 
def menu():
    while True:
        print("\n====== Data Storage Menu ======")
        print("1) Enter Data")
        print("2) View All Data")
        print("3) Delete a Data Piece")
        print("4) Quit")

        choice = input("\nChoice: ")

        if choice == "1":
            save_data()
        elif choice == "2":
            view_all()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

menu()
