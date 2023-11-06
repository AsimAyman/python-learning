# ---------------------------------
# ------loop =>While training -----
# ------Simple Bookmark Manage ----
# ---------------------------------

# Empty list to fill later
myFavWebs = []
# Maxumum Allowed websites
mxWebs = 5
while mxWebs > 0:
    # input the websit
    web = input('Input your website after https://')
    # add to the fave list
    myFavWebs.append(f"https://{web.strip().lower()}")
    mxWebs -= 1
    print(
        f'Website {myFavWebs[-1]} is add successfully, you still have {mxWebs} places left')

else:
    print("you finished all the places you")
    print(f"your courrent favorent list {myFavWebs}")

#check list is not empty
if myFavWebs:
    #sort()
    myFavWebs.sort()
    idx =0
    print("printing the list of the websit ")
    while idx < len(myFavWebs):
        print(f"{idx+1} ==>> {myFavWebs[idx]}")
        idx +=1
