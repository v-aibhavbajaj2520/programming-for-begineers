import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df=pd.read_csv('Movies analysis.csv')

#----------------------------------MAIN MENU----------------------------------------------------------------------------------------------
def menu():
    ans='y'
    while ans=='y':
        print('='*70)
        print('MOVIE WATCHERS ON VARIOUS OTT PLATFORMS ANALYSIS')
        print('='*70)
        print('1. DATA VISUALIZATION')
        print('2. ANALYSIS')
        print('3. MANIPULATION')
        print('4. EXIT')
        print('='*70)
        int=input('ENTER YOUR CHOICE:')  
        if int=='1':
                visual()
        elif int=='2':
                analy()
        elif  int=='3':
                manip()
        elif  int=='4':
                 ex= input('DO YOU REALLY WANT TO EXIT?(y/n)')
                 if ex=='y' or ex== 'Y':
                    break
                 else:
                    continue
        else:
            print('******INCORRECT SYNTAX*******')
            continue


#------------------------------DATA VISUALIZATION-----------------------------------------------------------------------------------    

#LINE GRAPH
def line_graph():
    print(df.OTTPLATFORM)
    ent=input('ENTER NAME OF OTT PLATFORM:')
    df1=df.loc[(df.OTTPLATFORM==ent)]
    print(df1)
    
    x=df1['MONTHS']
    y=df1['MOVIES WATCHED']
    plt.plot(x,y,marker='o')
    plt.xlabel('MONTHS',fontsize=12,color='blue')
    plt.ylabel('NO. OF MOVIES WATCHED (IN MILLIONS)',fontsize=12,color='blue')
    plt.title(f'MONTHLY MOVIES WATCHED ON {ent}',fontsize=18,color='red')
    plt.grid()
    plt.show()



#BARGRAPH
def bar_graph():
    df=pd.read_csv('Movies analysis.csv')
    print(df.OTTPLATFORM)
    ent=input('ENTER NAME OF OTT PLATFORM:')
    df1=df.loc[(df.OTTPLATFORM==ent)]
    print(df1)
    
    x=df['MONTHS']
    y=df['WEBSERIES WATCHED']
    plt.bar(x,y)
    plt.xlabel('MONTHS',fontsize=12,color='blue')
    plt.ylabel('NO. OF WEBSERIES WATCHED (IN MILLIONS)',fontsize=12,color='blue')
    plt.title (f'MONTHLY WEBSERIES WATCHED ON {ent}',fontsize=18,color='red')
    plt.grid()
    plt.show()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def visual():
     ans='y'
     while ans=='y' or ans=='Y':
         print('1.LINE GRAPH')
         print('2.BAR GRAPH')
         print('3. EXIT')
         inp1=input ('ENTER YOUR CHOICE:')
         if inp1=='1':
             line_graph()
         elif inp1=='2':
             bar_graph()
         elif inp1=='3':
             ex=input('DO YOU REALLY WANT TO EXIT??(y/n)')
             if ex== 'y' or ex=='Y':
                 break
             if ex=='n' or ex=='N':
                 continue
             else:
                 print ('******INCORRECT SYNTAX******')
         else:
             print ('******INCORRECT SYNTAX******')


#-----------------------------------ANALYSIS-----------------------------------------------------------------------------------------
def column_name():
    print(df.columns)
    n=input('ENTER THE NAME OF COLUMN:')
    print(df[n])


def top_rows():
    n=int(input('ENTER THE NUMBER OF ROWS YOU WANT TO SEE:'))
    print(df.head(n))


def bottom_rows():
    n=int(input('ENTER THE NUMBER OF ROWS YOU WANT TO SEE:'))
    print(df.tail(n))


def multiple_columns():
    print(df.columns)
    n=eval(input('MULTIPLE COLUMN NAMES (IN SQUARE BRACKET[]):'))
    print(df[n])

#-----------------------------------------------------------------------------------------------------

def analy():
     while True:
        print('1. A CERTAIN COLUMN')
        print('2. DISPLAY MULTIPLE COLUMNS')
        print('3. BOTTOM ROWS')
        print('4. TOP ROWS')
        print('5. EXIT')
        int2=int(input('ENTER YOUR CHOICE:'))
        if int2==1:
            column_name()
        elif int2==2:
            multiple_columns()
        elif int2==3:
            bottom_rows()
        elif int2==4:
            top_rows()
        elif int2==5:
            break  

        
#-------------------------------MANIPULATION----------------------------------------------------------------------------------------------------------
def insert():
    df2=pd.read_csv('Movies analysis.csv')
    n=input('Enter the name of column:')
    df3 = df2
    df3[n]= np.empty
    print(df3)

def deleting_row():
    df4=pd.read_csv('Movies analysis.csv')
    print(df4)
    n=int(input('ENTER ROW INDEX NUMBER YOU WANT TO DELETE:'))
    df4=df4.drop(n)
    print(f'ROW NUMBER {n+1} is deleted')
    print (df4)    


def deleting_column():
    df=pd.read_csv('Movies analysis.csv')
    print(df.columns)
    n=input('ENTER NAME OF THE COLUMN YOU WANT TO DELETE:')
    v=input(f'ARE YOU SURE YOU WANT TO DELETE {n}? (Y/N):')
    if v=='Y':
        del df[n]
        print(f'The Column {n} has been successfully deleted')
        df2=pd.DataFrame()
        df2=df
        print (df2)


def deleting_multiple_rows():
    df=pd.read_csv('Movies analysis.csv')
    print(df)
    n=eval(input('ENTER ROW INDEX NUMBERS YOU WANT TO DELETE (IN SQUARE BRAKETS[]):'))
    df=df.drop(n)
    n1=[x+1 for x in n]
    print(f'ROW NUMBER {n1} is deleted')
    print(df)

            
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def manip():
    while True:
            print('1. INSERTING COLUMN')
            print('2. DELETING A ROW')
            print('3. DELETING A COLUMN')
            print('4. DELETING MULTIPLE ROWS')
            print('5. EXIT')
            print('original dataframe')
            df3=pd.read_csv('Movies analysis.csv')
            print(df3)
            inp5=input('ENTER YOUR CHOICE:')
            if inp5=='1':
                insert()
            elif inp5=='2':
                deleting_row()
            elif inp5=='3':
                deleting_column()
            elif inp5=='4':
                deleting_multiple_rows()
            elif inp5=='5':
                    break
                

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
menu()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
