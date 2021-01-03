from room import Room 
from characterList import enemies

# Defining Rooms
room = {
    'village': Room("Village Center", False, "In the Village Center you see the BlackSmith's Shop to the West, the Apothecary to the East, and a Path leading North towards the lost forest"),

    'blacksmith': Room("Blacksmith's Shop", False, "You enter the Blacksmith's shop, the walls are lined with weapons and armors, though you cannot buy anything as you are poor, return to the Village Center by heading South"),

    'apothecary': Room("Apothecary", False, "You enter the Apothecary, the shelves lined with different herbs and potions, though you cannot buy anything as you are poor, return to the Village Center by heading South"),

    'path': Room("Path to Lost Forest", False, "You head North, stopping halfway to the Lost Forest to rest. You can continue North to the Lost Forest, or head South to get to the Village Center"),

    'lostForestEntrance': Room("Lost Forest Entrance", False, "You arrive at the line of the Lost Forest. There's a path to the west that leads to a river, and a path North to brave the insides of the Lost Forest. " ),

    'river': Room("River", False, "You stop at the river. It is clear blue, and inside of it you see a shiny object. To the East is a path. "),

    'lostForestPath': Room("Lost Forest Path", False,  "You brave your way into the forest. Before you lies a branching path. You see a clearing to the west. In front of you the path continues, but it is dark, and you cannot see what lies ahead."),

    'clearing': Room("Clearing", False,  "You stop in the middle of the clearing. There is a firepit in the middle of it, with an iron poker stuck in it. There are paths to the North and East. Heading west will lead you to the river."),

    'caveEntrance': Room("Cave Entrance",  False, "As you walk forwared you see a Cave Entrance. There are wooden boards restricting you from entering. To the East there is a path."),

    'cabin': Room("Cabin", False, "You walk through the path and stop upon a Cabin. Theres a key on the front deck. The door to the Cabin is locked."),

    'cabinInside': Room("Cabin Inside", False, "Inside, the cabin is small, with a wooden table and chair sitting next to a fireplace, there's an open chest with treasure inside"),

    'secretHatch': Room("Secret Hatch", False, "You go down the hatch, halfway down the ladder you realize there is almost no light"), 
}

