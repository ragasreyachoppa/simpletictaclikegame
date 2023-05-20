#!/usr/bin/env python
# coding: utf-8

# In[1]:


#tic tac toe practice


# In[2]:


#displaying information


# In[3]:


print([1,2,3])


# In[4]:


print([4,5,6])


# In[5]:


print([7,8,9])


# In[6]:


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


# In[7]:


example_row=[1,2,3]
display(example_row,example_rpw,example_row)


# In[8]:


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


# In[9]:


row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']


# In[10]:


display(row1,row2,row3)


# In[11]:


row2[1]='X'


# In[12]:


display(row1,row2,row3)


# In[13]:


def user_choice():
    choice=input("please enter a number(1-10): ")
    return int(choice)


# In[14]:


user_choice()


# In[15]:


user_choice()


# In[16]:


def user_choice():
    choice=''
    while choice.isdigit()==False:
        choice=input("please enter a number(1-10): ")
    return int(choice)


# In[17]:


user_choice()


# In[18]:


user_choice()


# In[19]:


def user_choice():
    choice=''
    while choice.isdigit()==False:
        choice=input("please enter a number(1-10): ")
        if choice.isdigit()==False:
            print("it is not a digit!")
    return int(choice)


# In[20]:


user_choice()


# In[21]:


user_choice()


# In[22]:


def user_choice():
    #initial choice
    choice=''
    acceptable_range = range(0,10)
    within_range = False
    
    
    while choice.isdigit() == False or within_range == False:
        choice=input("please enter a number(1-10): ")
        
        #digit check
        if choice.isdigit() == False:
            print("it is not a digit!")
            
        #range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print("sorry! it is out of range")
                within_range = False
             
    return int(choice)


# In[23]:


user_choice()


# In[24]:


game_list=[0,1,2]


# In[25]:


def display_game(game_list):
    print("Here is the game list")
    print(game_list)


# In[26]:


display_game(game_list)


# In[27]:


def position_choice():
    choice=' '
    while choice not in ['0','1','2']:
        choice=input("please pick a position (0,1,2) ")
        if choice not in ['0','1','2']:
            print("invalid range!")
    return int(choice)


# In[28]:


position_choice()


# In[29]:


def replacement_choice(game_list,position):
    user_placement=input("please select a string to place at position: ")
    game_list[position]=user_placement
    return game_list


# In[30]:


replacement_choice(game_list,2)


# In[31]:


def gameon_choice():
    choice=' '
    while choice not in ['Y','N']:
        choice=input("keep playing? Y or N")
        if choice not in ('Y','N'):
            print("sorry! i didnot understand please select Y or N ")
    if choice == 'Y':
        return True
    else:
        return False


# In[32]:


gameon_choice()


# In[33]:


gameon_choice()


# In[34]:


game_on=True
game_list=[0,1,2]

while game_on:
    
    display_game(game_list)
    
    position=position_choice()
    
    game_list=replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on=gameon_choice()
    


# In[ ]:




