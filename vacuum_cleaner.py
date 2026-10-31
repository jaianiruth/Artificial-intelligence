def vacuum_cleaner():
    # 0 means clean, 1 means dirty
    room = {'A': 1, 'B': 1}
    current_room = 'A'
    
    print("Initial state of rooms:", room)
    
    # We will do 2 steps to clean both rooms
    for i in range(2):
        if room[current_room] == 1:
            print("Room", current_room, "is dirty. Cleaning it now...")
            room[current_room] = 0
            print("Room", current_room, "is clean.")
        else:
            print("Room", current_room, "is already clean.")
            
        # Move to the other room
        if current_room == 'A':
            print("Moving to Room B")
            current_room = 'B'
        else:
            print("Moving to Room A")
            current_room = 'A'
            
    print("Final state of rooms:", room)

vacuum_cleaner()
