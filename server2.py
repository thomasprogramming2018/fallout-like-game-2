import socket
import pickle
import threading
import multiprocessing
import errno
import traceback
import asyncio

if __name__ == '__main__':
    # Define the host and port for your server
    HOST = '193.168.2.6'  # Listen on all available network interfaces
    PORT = 49152

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    #server_socket.setblocking(0)
    print(f"Server listening on {HOST}:{PORT}")

    #data_ready_event = threading.Event()
    
    # A dictionary to hold player data
    
    player_data = {
        "Aroyo_online" : {

        }, "Raiders_online" : {

        }
        
    }
    first_player_data = {
        "player_id": 'id',
        "current_sprite": 'objects/animations/playerIdleSprites/3/playerIdle (1).png',
        "x" : 300,
        "y" : 300,
        "loc" : 'Aroyo_online'
    }

    current_online_turn = 0
    
    player_turn_id = ""

    previous_turn = ""

    online_players = []

    #holds the ids of each enemy in a location
    enemies_online = {
        "Aroyo_online" : []
    }
    player_data2 = {}
    # Function to handle client connections
    class online_player():
        def __init__(self, name, has_turn):
            self.has_turn = has_turn
            self.id = name
    async def handle_client(client_socket22):
        global connections
        global client_sockets
        global prev_client_socket
        global data_ready_event
        global server_socket
        global player_data
        global enemies_online
        global current_online_turn
        global player_turn_id
        global online_players
        global previous_turn
        while True:
            #print(client_sockets)
            for client_socket2 in client_sockets:
                
                if prev_client_socket != client_socket2:
                    try:
                        #print(client_socket2)
                        #player_data2[first_player_data["player_id"]] = first_player_data  # Store player data on the server
                        players_and_client_data2 = {"player_data" : player_data}
                        pickle_data = pickle.dumps(players_and_client_data2)
                        #print(pickle_data)
                        #rint('test111')
                        await loop.sock_sendall(client_socket2, pickle_data)
                        #client_socket.send(pickle_data)
                        #print('sended')
                        #print(f"client: {client_socket}")
                        # Receive the JSON data from the client
                        data = await loop.sock_recv(client_socket2, 1024)
                        #data = client_socket.recv(1024)
                        # Deserialize the JSON data into a Python dictionary
                        #messages = data.split("\n")
                        #for message in messages:
                        try:
                            #print('loading and sending')
                            #print(data)
                            #print('data: ', str(data))
                            player_data_received = pickle.loads(data)
                            #print(player_data)
                            #print(connections)
                            #print(player_data_received)
                                # Handle player_data_received
                            #except json.decoder.JSONDecodeError:
                            # Handle JSON decoding errors
                                #print('json decoder error',str(messages))
                            # Process the player's data
                            
                            maps = ["Aroyo_online"]
                            for w in maps:
                                if w in player_data:
                                    if len(enemies_online[w]) == 0:
                                        current_online_turn = 0
                                        player_turn_id = ""
                                    if len(enemies_online[w]) >= 2:
                                        if player_data_received["player_data_rec"]["ap"] == 0:
                                            player_data_received["player_data_rec"]["has_turn"] = False
                                            try:
                                                if enemies_online[current_online_turn] != player_data_received["player_data_rec"]["player_id"]:
                                                    
                                                    for i in online_players:
                                                        if i == enemies_online[w][current_online_turn]:
                                                            player_data["player_data"][w][previous_turn]["has_turn"] = False
                                                            player_data["player_data"][w][i]["has_turn"] = True
                                                            previous_turn = i
                                                            current_online_turn += 1
                                                else:
                                                    player_data["player_data"][w][previous_turn]["has_turn"] = False
                                                    player_data_received["player_data_rec"]["has_turn"] = True
                                                    player_data_received["player_data_rec"]["ap"] = player_data_received["player_data_rec"]["ap_max"]
                                                    current_online_turn += 1
                                            except IndexError:
                                                current_online_turn = 0
                                                for i in online_players:
                                                    if i == enemies_online[w][current_online_turn]:
                                                        player_data["player_data"][w][previous_turn]["has_turn"] = False
                                                        player_data["player_data"][w][i]["has_turn"] = True
                                                        previous_turn = i
                                                        current_online_turn += 1
                                    for i, playeron in player_data[w].items():
                                        if playeron["shooted_player"] == player_data_received["player_data_rec"]["player_id"]:
                                            player_data_received["player_data_rec"]["hp"] -= playeron["DMG"]
                                            if player_data_received["player_data_rec"]["player_id"] not in enemies_online[w]:
                                                enemies_online[w].append(player_data_received["player_data_rec"]["player_id"])
                                                if playeron["player_id"] not in enemies_online[w]:
                                                    enemies_online[w].append(playeron["player_id"])
                                    
                                #try:
                                #    for (o, plr1), (i, plr2) in zip(player_data[w].items(), player_data_received["player_data"][w].items()):
                                #        if plr1["player_id"] == plr2["player_id"]:
                                #            plr1["enemies"] = plr2["enemies"]
                                #            plr1["has_turn"] = plr2["has_turn"]
                                #            plr1["DMG"] = plr2["DMG"]
                                #            plr1["shooted_player"] = plr2["shooted_player"]
                                #            plr1["hp"] = plr2["hp"]
                                #except Exception:
                                #    pass

                            player_loc = player_data_received["player_data_rec"]["loc"]
                            player_id = player_data_received["player_data_rec"]["player_id"]

                            if player_loc not in player_data:
                                player_data[player_loc] = {}
                            if player_id not in player_data:
                                player_data[player_id] = {}
                            
                            #player_data[player_loc] = player_data_received["player_data_rec"]["player_id"]
                            
                            player_data[player_loc][player_id] = player_data_received["player_data_rec"]  # Store player data on the server
                            
                            for i in player_data:
                                for e in player_data[i]:
                                    
                                    online_players.append(e)
                            #print('player_data: ',str(player_data))
                            connections = len(client_sockets)
                            players_and_client_data = {"player_data" : player_data, "player_data_rec" : player_data_received["player_data_rec"], "conn_id" : connections, "turn_system" : player_data_received["turn_system"]}
                            pickle_data = pickle.dumps(players_and_client_data)
                            # Broadcast the player's data to other connected clients
                            #for client in client_sockets:
                             #   if client != client_socket:
                            #print('sending')
                                #client.send(data.encode())  # Send the player's data to other clients
                            #client_socket.send(pickle_data)
                            await loop.sock_sendall(client_socket2, pickle_data)
                            #print("sending to:  ", str(client_socket2))
                            #print("players_and_client_data:     ", str(players_and_client_data))
                            #print(player_data)
                            #print('data_sent')
                            try:
                                pass
                                #print('sending: ', str(players_and_client_data))
                            except Exception:
                                pass
                        except pickle.UnpicklingError:
                            print('error')
                            print(data)
                            #traceback.print_exc()
                            #print(f"An UnpicklingError occurred: {e}")
                            pass
                    except ConnectionResetError:
                        if prev_client_socket != client_socket2:
                            player_data[player_loc].pop(player_id, None)
                            prev_client_socket = client_socket2
                            print("connection reset error")
                            connections -= 1
                            client_socket2.close()
                            client_sockets.remove(client_socket2)

                    except BlockingIOError:
                        # Handle the case where no data is available to read
                        #data = b''
                        #print('blockingio')
                        pass
    async def run():
        while True:
            client_socket, addr = await loop.sock_accept(server_socket)
            client_sockets.append(client_socket)
            print(f"Accepted connection from {addr}")
            loop.create_task(handle_client(client_socket))
    async def main():
        while True:
            task2 = loop.create_task(run())
            task1 = loop.create_task(handle_client('test'))
            

            await task1
            await task2
            
        try:
            global connections
            
            #client, addr = server_socket.accept()
            #if bool(client):
             #   connections += 1
            #print(f"Accepted connection from {addr}")
            #client_sockets.append(client)  # Add the new client socket to the list
            #for sockett in client_sockets:
                #print("handling the client")
                #client_thread = threading.Thread(target=handle_client, args=(sockett,))
                #client_thread.start()



                #data_ready_event.wait()
                #start_new_thread(handle_client, (sockett,))
            #handle_client(socket)
            #process = multiprocessing.Process(target=handle_client, args=(socket,))
            #process.start()
            #start_new_thread(handle_client(socket), (client,))
        except (socket.error, BlockingIOError) as e:
            if e.errno == errno.EWOULDBLOCK:
                for sockett in client_sockets:
                    #print("handling the client")
                   #client_thread = threading.Thread(target=handle_client, args=(sockett,))
                   #client_thread.start()
                    #data_ready_event.wait()
                    #start_new_thread(handle_client, (sockett,))
                    # No connection is pending, continue the loop
                    pass
            else:
                pass
                #for sockett in client_sockets:
                    #print("handling the client")
                 #   start_new_thread(handle_client, (sockett,))
                    # Handle other socket errors here
                #print(f"Socket error: {e}")
                    

            
    # List to store client sockets
    client_sockets = []

    connections = 0

    prev_client_socket = None

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    # Accept client connections and handle them
    #while True:
     #   run()

        #client_handler = threading.Thread(target=handle_client, args=(client,))
        #client_handler.start()
