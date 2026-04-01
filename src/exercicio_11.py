def modify_guest_list(guests, unavailable, new_guest):
    index = guests.index(unavailable)
    guests[index] = new_guest
    return guests