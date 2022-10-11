import turtle

# Initially the background colour of graphic canvas is white. It can be changed by using the 
# below function.

turtle.bgcolor("yellow") 
seurat=turtle.Turtle()
from random import randint

dot_distance=25

width=5
height=7

seurat.penup()
list_color=["White","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]
#python3 program to print
#given matrix in spiral form
seurat.setpos(-250,250) # when you write (0,0) it means canvas pen start from the center.

def spiralPrint(m,n):
    k=0
    l=0
    f=0
    ''' 
    k= indiex of starting row
    l= index of starting column
    m=ending row index
    n=ending column index
    i= iterator
    '''
    col=randint(0, 10)
    seurat.color(list_color[col])
    while(k<m and l<n):
        
        if(f==1):
            seurat.right(90)
        #printing the first row from the remaining rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            
           # print(a[k][i],end=" ")
        k+=1
        f=1
        
        seurat.right(90)        
        #printing the last column from the remaining column
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
           #print(a[i][n-1],end=" ")
        
        n-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        
        if (k<m):
            #printing the last row from remaining rows
            for i in range(n-1,l-1,-1):
                seurat.dot()
                #print(a[m-1][i],end=" ")
                seurat.forward(dot_distance)
                
            m-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if (l<n):
            for i in range(m-1,k-1,-1):
                #print(a[i][l],end=" ")
                seurat.dot()
                seurat.forward(dot_distance)
                
            l+=1
    

R=20; C=20
spiralPrint(R,C)
turtle.done()
