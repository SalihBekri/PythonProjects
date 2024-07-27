# Note: To test the full version of this code try running it in replit so you can activate the clear() method

from replit import clear
from art import logo
#Function
def find_the_winner(list):
  checker = 0
  bidder_name = ""
  for i in list:
    if list[i] > checker:
      checker = list[i]
      bidder_name = i
  
  print(f"The winner is {bidder_name} with a bid of ${checker}.")

#Start
print(logo)
print("Welcome to the secret auction program.")
bidding_list = {}
on = True
###################
#Main loop
while on == True:
  
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidding_list[name] = bid
  ans = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  if ans == "no":
    find_the_winner(bidding_list)
    on = False
  
