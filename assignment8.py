#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3


# In[2]:


def question1():
    list1=["string","float","int","bool"]
    sliced_list = list1[1:3]
    for value in reversed(sliced_list):
        print(value)


# In[3]:


question1()


# In[4]:


def question2():
    list2 = {"string":"Apple","float":3.14,"int":11,"bool":True}
    for key,value in list2.items():
        print(f"{key}:{value}")


# In[5]:


question2()


# In[6]:


def question3():
    list3=list(range(1,7))
    for number in list3:
        if number%5==0:
            print("5 is in the list")
            break
    else:
        print("5 is not in the list")


# In[7]:


question3()


# In[8]:


from collections import defaultdict
def question4():
    sentence = "If code and data are not open source, who will source the code and data of the future?"
    word_count = defaultdict(int)
    words = sentence.split()
    for word in words:
        word_count[word] = word_count[word]+1
    return dict(word_count)


# In[9]:


question4()


# In[10]:


from collections import Counter
def question5():
    sentence = "If code and data are not open source, who will source the code and data of the future?"
    cnt = Counter()
    words = sentence.split()
    for word in words:
        cnt[word] +=1
    for word,count in cnt.items():
        if cnt[word]>1:
            print(word,count)


# In[11]:


question5()


# In[12]:


def question6():
    list6 = [1, 4, 9, 27, 42, 55]
    for value in list6:
        if value%15 == 0:
            print("fizzybuzzy")
        elif value%5 == 0:
            print("buzzy")
        elif value%3 == 0:
            print("fizzy")
        else:
            print(value)


# In[13]:


question6()


# In[14]:


def question7():
    x = 4
    if x == None:
        print("x is set to None")
    elif x == 4:
        print("x is correctly set to 4")
    else:
        print("x is not set to None but not correctly set to 4")


# In[15]:


question7()


# In[16]:


def question8():
    A = "ATCQ"
    print(A[2:4])
    print(A[0:2])


# In[17]:


question8()


# In[18]:


def question9():
    list9 = []
    for value in range(1,6):
        list9.append(value*10)
    print(list9)


# In[19]:


question9()


# In[20]:


def question10():
    Z = list(range(0,6))
    if len(Z) == 6:
        print("The length of the list equals 6")
    else:
        print("The length of the list does not equal 6")


# In[21]:


question10()


# In[23]:


def main():
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()
    question10()


# In[24]:


if __name__ == "__main__":
    main()


# In[ ]:




