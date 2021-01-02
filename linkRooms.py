from roomList import room

# Linking Rooms

room['village'].n_to = room['path']
room['village'].w_to = room['blacksmith']    
room['village'].e_to = room['apothecary']
room['blacksmith'].s_to = room['village']
room['apothecary'].s_to = room['village']
room['path'].s_to = room['village']
room['path'].n_to = room['lostForestEntrance']
room['lostForestEntrance'].w_to = room['river']
room['lostForestEntrance'].n_to = room['lostForestPath']
room['lostForestEntrance'].s_to = room['path']
room['lostForestPath'].w_to = room['clearing']
room['lostForestPath'].n_to = room['caveEntrance']
room['river'].s_to = room['lostForestEntrance']
room['river'].e_to = room['clearing']
room['clearing'].s_to = room['lostForestPath']
room['clearing'].w_to = room['river']
room['clearing'].n_to = room['cabin']
room['caveEntrance'].s_to = room['lostForestPath']
room['cabin'].s_to = room['clearing']
room['cabin'].n_to = room['cabinInside']