#I put explanations for each line of code. I was not able to figure this assignment out on my own, so Brian helped me a lot, and I wrote comments for each command line to explain the usage of each part.

users = {
 'students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Trey', 'last_name' : 'Villafane'}
  ]
 }

for key, value in users.items(): #you need to select 2 variables from users. You also have to say users.items() because it will let you look at all info inside users and not just at the keys.

 	print key.title() #this makes the key values be titles
	counter = 0 #this just applies to the numbering of students in the example

	for x in value: #this means in each line of students
		counter = counter + 1 #the counter needs to go up by 1 each time because that's how counting works
		full_name = x["first_name"] + " " + x["last_name"]
		#you have to do x["first_name"] because it means go to the dictionary x and then take the value that belongs to this key
		full_name_upper = full_name.upper()
		#this is a built in formula called .upper() that takes the variable full_name and makes it all uppercase. You use it by putting it on the end of the variable and creating a new variable to set it to
		name_count = len(x["first_name"]) + len(x["last_name"]) #x["first_name"] also refers to dictionary x and then the value from the key "first_name". it takes the string value and adds it to the same for the value from the key "last_name". You get MichaelJordan for example, or JohnRosales, or MarkGuillen. Then, you perform the len() function which gets you the number of characters in the new string you created by adding.

		print "%d - %s - %d" %(counter, full_name_upper, name_count)
		# %d means a data type (?) and %s means a string. If you want to print them all in the same line, you put it in quotes and substitute %d and %s and then you put %() and fill in the parantheses with the variables that you want to get values from
