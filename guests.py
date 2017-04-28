# Default list
guests = ['Geoffrey', 'Malcom','Nerd','Pinket','Dru Hill']
guests.append('Jake')
guests.append('Jenny')
guests.append('Sue')

print(guests)
print()

# Send message to the guests
message = " Package lost, your mission is compromised."
print("Hello "+ guests[5] + " "+ message)
print("Hello "+ guests[6] + "  "+ message)
print("Hello "+ guests[7] + ""+ message)
print()

# One guest unable to attend meeting, need a quick replacement
innatendance = guests.pop(5)
print(innatendance, " will not attend the meeting")
guests.insert(5,'Doe')
print()

# Message to all attending guests
print("Hello " + guests[5] + " " + message)
print("Hello "+ guests[6] + " "+ message)
print("Hello "+ guests[7] + " "+ message)

print()

# Who will occupy the Oval Office?
message = " will occupy the oval office"
print(guests[5] + " " + message)
print(guests[6] + " "+ message)
print(guests[7] + " "+ message)
print()

guests.insert(5,'Cameron')
guests.insert(6,'Aleppo')
guests.append('Finch')
print(guests[5] + " " + message)
print(guests[6] + " "+ message)
print(guests[-1] + " "+ message)

print()

print("Only two guests will be allowed in the situation room")
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
print()

message = "The following guests are invited to the situation room " + str(guests[0]) +" and " + str(guests[1])+"."
print (message)

# Delete assets
del guests[0]
del guests[0]

if guests == "":
	print('Guests found')
else:
	print('List Empty')



