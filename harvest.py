############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

            
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code 

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType("musk", 1998, "green", True, True, "MuskMelon")
    musk.add_pairing('mint')
    all_melon_types.append(musk)
    #print(musk.code)

    casaba = MelonType("cas", 2003, "orange", True, False, "Casaba")
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    crenshaw.add_pairing('proscuitto')
    casaba.add_pairing('strawberries')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    #melon_types = make_melon_types()

    for melon_type in melon_types:
        #print(melon_type.name)
        for pairing in melon_type.pairings:
            print(f"{melon_type.name} pairs with {pairing}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #Fill in the rest

    melon_dict = {}
    for melon_type in melon_types:
        melon_dict[melon_type.code] = melon_type

    return melon_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, mtype, shape, color, field_number, who_harvested):

        self.mtype = mtype
        self.shape = shape
        self.color = color
        self.field_number = field_number
        self.who_harvested = who_harvested
        self.is_sellable = False

    def can_sell(self):
        if (self.shape > 5 and self.color > 5) and self.field_number != 3:
            self.is_sellable = True
        
        return self.is_sellable






def make_melons(all_melon_types):
    """Returns a list of Melon objects."""
    melon_list2 = []

    melons_running = make_melon_type_lookup(melon_types)
     #list from above
    melons_running[melon.mtype]= mtype

    # Fill in the rest
    melon_1 = Melon("yw", 8, 7, 2, "Sheila") 
    melon_list2.append(melon_1)
    melon_2 = Melon("yw", 3, 4, 2, "Sheila") 
    melon_list2.append(melon_2)
    melon_3 = Melon("yw", 9, 8, 3, "Sheila") 
    melon_list2.append(melon_3)
    melon_4 = Melon("cas", 10, 6, 35, "Sheila") 
    melon_list2.append(melon_4)
    melon_5 = Melon("cren", 8, 9, 35, "Michael") 
    melon_list2.append(melon_5)
    melon_6 = Melon("cren", 8, 2, 35, "Michael") 
    melon_list2.append(melon_6)
    melon_7 = Melon("cren", 2, 3, 4, "Michael") 
    melon_list2.append(melon_7)
    melon_8 = Melon("musk", 6, 7, 4, "Michael") 
    melon_list2.append(melon_8)
    melon_9 = Melon("yw", 7, 10, 3, "Sheila") 
    melon_list2.append(melon_9)

    return melon_list2


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    return


all_melon_types = make_melon_types()


make_melons(all_melon_types)