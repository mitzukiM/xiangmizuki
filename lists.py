given_name = "Vasyl Kartychak"
given_name = given_name.title()
analizing_data = given_name.split()

students = ["Anna" , "Rita"]

pencils = ["grey" , "black"]
crayons =["red" , "blue" , "black" , "black"]
pencil_red = crayons[0]
pencil_red_2 = crayons[-4]
pencil_blue = crayons[1]
pencil_black = crayons[-2]



# add element
crayons.append("orange")

#remove element
crayons.remove("black")

# merge 2 lists
# crayons.append(pencils)
crayons.extend(pencils)


what_is_list = ["Vasyl" , "Kartychak" , "Anna" , "Alex" , 55, [55], True , False , 3.874]
print(what_is_list)
pass
