import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import sys 
 
 
 
df=pd.read_csv("Human_Resources_US.csv") 
 
 
ch1=1 
while(ch1==1): 
    print("---------------------------------------")     
    print("              ***MAIN MENU***          ")     
    print("---------------------------------------") 
    print("1. View the dataset")     
    print("2. View graphs of the dataset")     
    print("3. Analyse the dataset")     
    print("4. Manipulate the dataset")     
    print("5. Help Desk")     
    print("6. Exit")     
    print("---------------------------------------") 
    print("Enter your choice::") 
     
    ch=int(input()) 
     
    if ch==5: 
         
        ttt=1         
        while (ttt==1):             
            print("Please tell us your query below and will try to resolve it")             
            q=input() 
            delay=["slow","Slow","delay","Delay","time"]             
            error=["Output","output","error"]             
            wrong=["wrong","inaccurate"]             
            notfound=["found","available","exist"] 
            b=0             
            c=0             
            d=0             
            e=0             
            que=q.split( ) 
             
            for x in range(0,len(que)): 
                if que[x] in delay: 
                    print("\n") 
                    print("We recommend you to restart the kernel and try again") 
                    break                 
                else: 
                    b+=1         
            for x in range(0,len(que)):                 
                if que[x] in notfound: 
                    print("\n") 
                    print("Your input should be an integer value [1/2],try again with proper input") 
                    break                 
                else:                     
                    c+=1 
 
            for x in range(0,len(que)):                 
                if que[x] in error: 
                    print("\n") 
                    print("We recommend to check your input properly and run the program again :") 
                    break                 
                else:                     
                    d+=1 
 
            for x in range(0,len(que)):                 
                if que[x] in wrong: 
                    print("\n") 
                    print("This program has been designed after multiple tests,please try to check your input again") 
                    print("thankyou for cooperating") 
                    break                 
                else:                     
                    e+=1             
                    if b==c==d==e==len(que): 
                        print("Oops we could not understand your query") 
             
                 
                 
            print("\n")             
            print("Do you want to continue with help desk?")             
            print("1.Yes\n2.No")            
            ttt=int(input()) 
 
 
 
             
             
    if (ch==1):       
        print("Which type of Human_Resources_US dataset do you want to view?:") 
         
        print("1. Human_Resources_US.txt file") 
        print("2. Human_Resources_US.csv file") 
        print("\n")         
        a=int(input())         
        if a==1: 
            df=pd.read_csv("Human_Resources_US.txt")             
            print("THE DATASET OF YOUR CHOICE IS SHOWN BELOW:") 
            print(df)         
        elif a==2: 
            df0=pd.read_csv("Human_Resources_US.csv")             
            print("THE DATASET OF YOUR CHOICE IS SHOWN BELOW:") 
         
            print(df0)         
            print("\n")         
            print("Enter your choice to continue[Y/N]") 
        print("\n") 
         
        ch1=input() 
         
    elif (ch==2): 
        gg=1 
        while(gg==1):             
            print("\n") 
            print("Choose the graph no. you want to view:") 
            print("\n") 
            print("1. HISTOGRAM 0F SALARY") 
            print("2. LINE GRAPH OF NO. OF EMPLOYEES FROM EACH RECRUITMENT SOURCE") 
            print("3. HISTOGRAM OF ABSENCES")             
            print("4. BAR GRAPH OF NO. OF EMPLOYEES FROM EACH RACE") 
            print("5. HISTOGRAM OF NO. OF EMPLOYEES ACCORDING TO RANGE OF ENGAGEMENT_INDEX") 
            print("6. BAR GRAPH OF NO. OF PEOPLE FROM EACH MARITAL STATUS") 
            print("7. HISTOGRAM OF NO. OF EMPLOYEES ACCORDING TO EMPLOYEE_SATISFACTION") 
            print("8. BAR GRAPH GRAPH OF NO. OF MALES AND FEMALES") 
            print("9. LINE GRAPH OF NO. OF PEOPLE IN EACH DEPARTMENT") 
            print("\n")             
            print("\n") 
            graph_choice=int(input()) 
 
            print("The graph of your choice is shown below-") 
             
            print("\n")             
            if graph_choice==1: 
                print(" ")                 
                print(" ") 
                
                plt.hist(df["Salary"],bins=5,color="yellow",edgecolor="red",linewidth=3) 
                plt.xlabel("Salary",color='purple',fontsize=16)                 
                plt.ylabel("Count of Employees",color='purple',fontsize=20) 
                plt.title("Salary Frequency Distribution",color='purple',fontsize=22) 
                plt.show()                 
                print("Here is a takeway from the graph::") 
                
                print("Most employees have Salary between 50000 to 100000") 
                                
 
 
            elif graph_choice==3: 
                
                plt.hist(df["Absences"],bins=7,color="yellow",edgecolor="red",linewidth=3)                 
                plt.xlabel("No. of Absences",color='r',fontsize=16)                 
                plt.ylabel("Count of Employees",color='r',fontsize=20) 
                plt.title("Absences Frequency Distribution",color='r',fontsize=22)                 
                plt.xticks( np.arange(2,25,4)) 
                plt.yticks()                 
                plt.show() 
            elif graph_choice==5: 
                
                plt.hist(df["EmpSatisfaction"],bins=7,color="yellow",edgecolor="red",linewidth=3) 
                plt.xlabel("Index of Employee Satisfaction(max=5)",color='r',fontsize=16)                 
                plt.ylabel("Count of Employees",color='r',fontsize=20) 
                plt.title("Employee Satisfaction Frequency Distribution",color='r',fontsize=22) 
                plt.xticks() 
                plt.yticks()                 
                plt.show() 
            elif graph_choice==8: 
                w=df.groupby("Sex").count()                 
                f=w.EmpID 
                f 
                plt.bar(f.index,f,color="pink",linewidth=0.8,edgecolor='r')                 
                plt.xlabel("Gender Of Employee",color='r',fontsize=16)                 
                plt.ylabel("Count of Employees",color='r',fontsize=20)                 
                plt.title("Gender Frequency Distribution",color='r',fontsize=22) 
                plt.xticks()                 
                plt.yticks()                 
                plt.show()             
            elif graph_choice==2: 
                r=df.groupby("RecruitmentSource").count()                 
                e=r.EmpID                 
                plt.plot(e.index,e,color="r") 

                plt.xlabel("Recruitment Source",color='purple',fontsize=20) 
                plt.ylabel("No. of employees",color='purple',fontsize=20)                 
                plt.title("Count of employees according to Recruitment Source",color='purple',fontsize=20) 
                plt.xticks(rotation=45)                 
                plt.show()             
            elif graph_choice==5: 
                plt.hist(df["EngagementSurvey"],color="r") 
 
                
                plt.xlabel("Engagement_Index(max=5)",color='purple',fontsize=20)                 
                plt.ylabel("Count of employees",color='purple',fontsize=20) 
                plt.title("Count of employees according to Engagement_Index",color='purple',fontsize=20) 
                plt.xticks()                 
                plt.show() 
            elif graph_choice==4: 
                q=df.groupby("RaceDesc").count() 
                a=q.EmpID                 
                plt.bar(a.index,a,color="orange") 
 
                plt.xlabel("Race",color='r',fontsize=20) 
                plt.ylabel("No. of employees",color='r',fontsize=20) 
                plt.title("Count of employees according to Race",color='r',fontsize=20) 
                plt.xticks(rotation=45)                 
                plt.show() 
 
            elif graph_choice==9: 
                t=df.groupby("Department").count() 
 
                s=t.EmpID 
 
                m=s.index 
 
                plt.plot(m,s,color="r") 
 
                plt.xlabel("Name of the Department",color='purple',fontsize=20) 
                plt.ylabel("No. of employees",color='purple',fontsize=20) 
                plt.title("Count of employees according to department",color='purple',fontsize=20) 
                plt.xticks(rotation=45) 
                plt.show() 
 
            elif graph_choice==6: 
                v=df.groupby("MaritalDesc").count()                 
                r=v.EmpID                 
                plt.plot(r.index,r,color="r",)                 
                plt.xlabel("Marital Status Of Employees",color='r',fontsize=16)                 
                plt.ylabel("Count of Employees",color='r',fontsize=20) 
                plt.title("Marital Status Frequency Distribution",color='r',fontsize=22) 
                plt.xticks(rotation=45)                 
                plt.yticks()                 
                plt.show()             
                print("\n") 
 
            print("\n Do you want to view other graphs?[1/2]") 
            print("\n")             
            print("1. YES \n 2. NO")             
            gg=int(input()) 
         
 
 
 
             
    elif (ch==3): 
        print("The content of the dataset are:")         
        df=pd.read_csv("Human_Resources_US.csv") 
        aa=1         
        while(aa==1): 
            print("Choose one of the following options:")             
            print("1. Display top records")             
            print("2. Display bottom records") 
            print("3. Display particular column/columns depending on data like")             
            print("4. Display particular row/rows depending on data-like") 
 
            analyse_choice=int(input()) 
 
            if analyse_choice==1: 
                print("Select number of rows to print from top:") 
                x=int(input()) 
                df1=df.head(x)                 
                print(df1) 
 
            if analyse_choice==2: 
                print("Select number of rows to print from bottom:") 
                y=int(input())                 
                df2=df.tail(y)                 
                print(df2) 
 
            if analyse_choice==3: 
                ss=1                 
                while(ss==1): 
                    print("Choose any one of the following") 
                    print("1. Display Employee Names along with their PositionID:") 
                    print("2. Display Manager Names along with ManagerID and Employee Satisfaction:") 
                    print("3. Display Employee names along with Marital description:") 
                    print("4. Display Position of each employee along with their Race description:") 
                    print("OR")                     
                    print("5. Select which column(s) to view:") 
                    cl=int(input()) 
 
                    if cl==1: 
                        one=["Employee_Name", "PositionID"] 
                        df6 = pd.read_csv("Human_Resources_US.csv", usecols=one) 
                        print(df6) 
                    elif cl==2: 
                        two=["ManagerName", "ManagerID", "EmpSatisfaction"] 
                        df7=pd.read_csv("Human_Resources_US.csv", usecols=two) 
                        print(df7) 
 
                    elif cl==3: 
                        three=["Employee_Name", "MaritalDesc"] 
                        df8=pd.read_csv("Human_Resources_US.csv", usecols=three) 
                        print(df8) 
                    elif cl==4: 
                        four=["Position", "RaceDesc"] 
                        df9=pd.read_csv("Human_Resources_US.csv", usecols=four) 
                        print(df9) 
 
                    elif cl==5: 
                        print("The columns are: Employee_Name, EmpID, MarriedID, MarriedStatusID, GenderID, EmpStatus, DeptID, PerfScoreID, FromDiversityJobFairID, Salary, TermID, PositionID, Position, State, Zip, Sex, MaritalDesc, CitizenDesc, HispanicLatino, RaceDesc, TermReason, EmploymentStatus, Department, ManagerName, ManagerID, RecruitmentSource, PerformanceScore, EngagementSurvey, EmpSatisfaction, SpecialProjectsCount, DaysLateLast30, Absences") 
                        columns_list=[]                         
                        n = int(input("Enter number of columns : ")) 
                        for i in range (0,n): 
                            print("Enter column names of selected no. of columns") 
                            columns=input()                             
                            columns_list.append(columns)                         
                            print(columns_list) 
                        df5 = pd.read_csv("Human_Resources_US.csv", usecols=columns_list) 
                        print(df5) 
                    print("Do you want to continue analysation on columns?") 
                    print("1.Yes\n2.No")                     
                    ss=int(input()) 
                    #if ss==2: 
                        #print("Do you want to continue analysation?") 
                        #print("1.Yes\n2.No") 
                        #aa=int(input()) 
                           
                 
 
            if analyse_choice==4: 
                tt=1                 
                while(tt==1): 
                    print("Choose one of the following:") 
                    print("1. Display details of Employees with salary between two values:") 
                    print("2. Display details of Employees whose MarriedID is 1:") 
                    print("3. Display Manager Names of each employee according to department chosen:") 
                    print("4. Display all the names of female employees:") 
                    print("5. Display Employee names with Recruitment source as LinkedIn:") 
                    a=int(input()) 
                    if a==1: 
                        print("Enter the values")                         
                        salary1=int(input())                         
                        salary2=int(input())                         
                        df3=df[(df["Salary"]>salary1) & (df["Salary"]<salary2)] 
                        print(df3) 
                                                  
 
                    elif a==2: 
                        df4=df[(df["MarriedID"]==1)] 
                        print(df4) 
                    elif a==3: 
                        print("Choose the department from the following:")                         
                        print("1. Production")                         
                        print("2. IT/IS")                         
                        print("3. Software Engineering")                         
                        print("4. Admin Offices")                         
                        print("5. Sales")                         
                        dept=int(input()) 
 
                        if dept==1:                               
                            print(df[df.Department == 'Production']) 
                        if dept==2: 
                              print(df[df.Department == 'IT/IS']) 
                        if dept==3:                               
                            print(df[df.Department == 'Software Engineering']) 
                        if dept==4:                               
                            print(df[df.Department == 'Admin Offices']) 
                        if dept==5: 
                              print(df[df.Department == 'Sales']) 
                    elif a==4: 
                        df11=df[df["Sex"]=='F']                         
                        print(df11)                     
                    elif a==5: 
                        df12=df[df["RecruitmentSource"]=="LinkedIn"] 
                        print(df12) 
                    print("Do you want to continue analysation on rows?") 
                    print("1.Yes \n2.No")                     
                    tt=int(input()) 
            print("Do you want to continue with analysing data?[1/2]")             
            print("1. YES \n2. NO")             
            aa=int(input()) 
 
 
             
    elif (ch==4): 
        print("The content of the dataset are:") 
        df=pd.read_csv("Human_Resources_US")         
        df=pd.read_csv("Human_Resources_US.csv")         
        zz=1         
        while zz==1: 
            print("Choose one of the following:")             
            print("1. Insert Rows")             
            print("2. Delete Rows")             
            print("3. Update Information")             
            print("4. Add another dataframe file")             
            print("5. Sort data") 
         
         
            manipulate_choice=int(input()) 
 
            if manipulate_choice==1: 
                print("Choose one of the following:") 
                yy=1                 
                while yy==1: 
                    print("1.Inserting a new record at a Specific position")                     
                    print("2.Adding a new record at the End position") 
                    y=int(input())                     
                    if y==1: 
                        Position   =int(input("Enter the position where a new record is to be inserted")) 
                        Ename      =input("Enter Employee name::") 
                        E_ID       =int(input("Enter your Employee ID::")) 
                        M_ID       =int(input("Enter your Married ID")) 
                        MS_ID      =int (input("Enter your Marital staus ID::")) 
                        Gen_ID     =int(input("Enter your Gender ID::")) 
                        ES_ID      =int(input("Enter your Employee Status ID::")) 
                        P_ScoreID  =int(input("Enter your performance score ID::")) 
                        Jobfair_ID =int(input("Enter your Diversity Job Fair ID::")) 
                        Salary     =int(input("Enter your Salary::")) 
                        T_ID       =int(input("Enter your Term ID::")) 
                        P_ID       =int(input("Enter your Position ID::")) 
                        Pos        =input("Enter your Position::") 
                        St         =input("Enter your State::") 
                        Zip        =int(input("Enter Zip::")) 
                        Sex        =int(input("Enter your Sex::")) 
                        M_Desc     =input("Enter your Marital Desc::") 
                        C_Desc     =input("Enter your Citizen_Desc::") 
                        H          =input("Enter whether Hispaniclatino in Yes or No::") 
                        R_Desc     =input("Enter Race Desc::") 
                        T_R        =input("Enter Term::") 
                        E_Stat     =input("Enter Employee Status::") 
                        Dept       =input("Enter your Department::") 
                        M_name     =input("Enter the Manager's Name::") 
                        M_ID       =int(input("Enter the Manager ID")) 
                        R_So       =input("Enter your Recruitment Source::") 
                        P_Sc       =input("Enter your Performance Score::") 
                        E_Sur      =int(input("Enter Engagement Survey::")) 
                        E_Sat      =input("Enter Employee Statisfaction::") 
                        S_Pro      =int(input("Enter your number of completed Special Projects::")) 
                        Late       =int(input("Enter the number of days late in the last 30 Days::")) 
                        Ab         =int(input("Enter the number of days absent::")) 

                        Data=[E_ID, M_ID, MS_ID, Gen_ID, ES_ID, P_ScoreID, Jobfair_ID, Salary, T_ID, P_ID, Pos, St,Zip,Sex,M_Desc,C_Desc,H,R_Desc,T_R,E_Stat,Dept,M_na me,M_ID,R_So,P_Sc,E_Sur,E_Sat,S_Pro,Late,Ab]

                        Data=df.loc[Position-1] 
                        print(df) 
 
                    elif y==2: 
                        Ename      =input("Enter Employee name::") 
                        E_ID       =int(input("Enter your Employee ID::")) 
                        M_ID       =int(input("Enter your Married ID")) 
                        MS_ID      =int (input("Enter your Marital staus ID::")) 
                        Gen_ID     =int(input("Enter your Gender ID::")) 
                        ES_ID      =int(input("Enter your Employee Status ID::")) 
                        P_ScoreID  =int(input("Enter your performance score ID::")) 
                        Jobfair_ID =int(input("Enter your Diversity Job Fair ID::")) 
                        Salary     =int(input("Enter your Salary::")) 
                        T_ID       =int(input("Enter your Term ID::")) 
                        P_ID       =int(input("Enter your Position ID::")) 
                        Pos        =input("Enter your Position::") 
                        St         =input("Enter your State::") 
                        Zip        =int(input("Enter Zip::")) 
                        Sex        =int(input("Enter your Sex::")) 
                        M_Desc     =input("Enter your Marital Desc::") 
                        C_Desc     =input("Enter your Citizen_Desc::") 
                        H          =input("Enter whether Hispaniclatino in Yes or No::") 
                        R_Desc     =input("Enter Race Desc::") 
                        T_R        =input("Enter Term::") 
                        E_Stat     =input("Enter Employee Status::") 
                        E_Sat      =input("Enter Employee Statisfaction::") 
                        S_Pro      =int(input("Enter your number of completed Special Projects::")) 
                        Late       =int(input("Enter the number of days late in the last 30 Days::")) 
                        Ab         =int(input("Enter the number of days absent::")) 
 
                        
                        Data= [E_ID,M_ID,MS_ID,Gen_ID,ES_ID,P_ScoreID,Jobfair_ID,Salary,T_ID,P_ID,Pos,St,Zip,Sex,M_Desc,C_Desc,H,R_Desc,T_R,E_Stat,Dept,M_na me,M_ID,R_So,P_Sc,E_Sur,E_Sat,S_Pro,Late,Ab]
                        L=len(df.index) 
                        Data=df.loc[L]                         
                        print(df) 
                    print("Do you want to continue inserting rows ?")                     
                    print("1.YES \n 2.NO") 
                    yy=int(input()) 
