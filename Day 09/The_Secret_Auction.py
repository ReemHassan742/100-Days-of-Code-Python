def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_value = bidding_dictionary[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(winner)


bids={}
should_continue = True
while should_continue:
    name = input("What is your name? ")
    price = input("What is your bid? $ ")
    bids[name] = price
    should_continue = input("Would you like to continue? (Y/N) ")
    if should_continue == "N":
        should_continue = False
        find_highest_bid(bids)
    elif should_continue == "Y":
            print("\n" *20)

