
list = [1,2,3,4,5,6,7,8,0]
goal_list=[1,2,3,4,5,6,7,8,0]
for i in list:
    if list[i]==0:
        x=i
print(x)

count=0
check="false"
list_up=[]
list_down=[]
list_left=[]
list_right=[]
list_copy=[]
queue=[]
save_list=[]


up=x-3
down=x+3
left=x-1
right=x+1

if up>=0:

    list_up=list.copy()
    list_up[x]=list_up[up]
    list_up[up]=0
    u=up
    up=u-3
    count+=1
    queue.append(list_up)
    save_list.append(list_up)
    print (queue)
    if list_up==goal_list:
        #check=true
        print("problem solved with %d tries" %count)

if down<=8:
    list_down=list.copy()
    list_down[x]=list_down[down]
    list_down[down]=0
    count+=1
    d=down
    down=d+3
    queue.append(list_down)
    save_list.append(list_down)
    if list_down==goal_list:
        print("problem solved with %d tries" %count)

if left>=0:
    list_left=list.copy()
    list_left[x]=list_left[left]
    list_left[left]=0
    count+=1
    l=left
    left=l-1
    queue.append(list_left)
    save_list.append(list_left)
    if list_left==goal_list:
        print("problem solved with %d tries" %count)

if right<=8:
    list_right=list.copy()
    list_right[x]=list_right[right]
    list_right[right]=0
    count+=1
    r=right
    right=r+1
    queue.append(list_right)
    save_list.append(list_right)
    print("in if right")
    if list_right==goal_list:
        print("problem solved with %d tries" %count)
    #print(queue.pop(0))    


def go_up():
    global up
    global u
    global count
    global check
    global queue
    global list_up
    global save_list
    global goal_list
    print("in up def")
    for i in list_up:
        if list_up[i]==0:
            u=i
            up=u-3
    if up>=0:
        list_up[u]=list_up[up]
        list_up[up]=0
        count+=1
        #u=up
        #up=u-3
        queue.append(list_up)
        save_list.append(list_up)
        if list_up==goal_list:
            check="true"
            print("problem solved with %d tries" %count)
            print(save_list)


def go_down():
    global down
    global d
    global count
    global check
    global queue
    global list_down
    global save_list
    global goal_list
    for i in list_down:
        if list_down[i]==0:
            d=i
            down=d+3
    if down<=8:
        print("in down def")
        #list_down=list.copy()

        list_down[d]=list_down[down]
        list_down[down]=0
        count+=1
        d=down
        down=d+3
        queue.append(list_down)
        save_list.append(list_down)
        if list_down==goal_list:
            check="true"
            print("problem solved with %d tries" %count)
            print(save_list)


def go_left():
    global left
    global l
    global count
    global check
    global queue
    global list_left
    global save_list
    global goal_list
    for i in list_left:
        if list_left[i]==0:
            l=i
            left=l-1
    if left>=0:
       if l not in (0,3,6) :
        #if l==1|l==2|l==4|l==5|l==8|r==7:
           print("in left def")

           #list_left=list.copy()
           list_left[l]=list_left[left]
           list_left[left]=0
           count+=1
           l=left
           left=l-1
           queue.append(list_left)
           save_list.append(list_left)
           if list_left==goal_list:
               check="true"
               print("problem solved with %d tries" %count)
               print(save_list)


def go_right():
    global right
    global r
    global count
    global check
    global queue
    global list_right
    global save_list
    global goal_list
    for i in list_right:
        if list_right[i]==0:
            r=i
            right=r+1
    if right<=8:
        #if r not in[2,5,8]:
        if r not in (2, 5, 8):
         #if r==0|r==1|r==3|r==4|r==6|r==7:
            print("in right def")

            list_right[r]=list_right[right]
            list_right[right]=0
            count+=1
            r=right
            right=r+1
            queue.append(list_right)
            save_list.append(list_right)
            if list_right==goal_list:
                check="true"
                print("problem solved with %d tries" %count)
                print(save_list)



while check=="false":
    print("len queue is:")
    print(len(queue))
    if len(queue)>0:
        list_copy=queue.pop(0)
        print (len(queue))
        list_up=list_copy.copy()
        go_up();
        if check=="true":
            break


        list_down=list_copy.copy()
        go_down();
        if check=="true":
            break
        list_left=list_copy.copy()
        go_left();
        if check=="true":
            break
        list_right=list_copy.copy()
        go_right();
        if check=="true":
            break


print("out of while")
print (save_list)
print ()
