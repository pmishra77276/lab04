def sorte():
    name=["Raman","Himadri","Jaya","Tejas","Ajay"]
    age=[41,38,51,30,45]
    salary=[5600,67500,82100,55000,44000]
    print("Sorting program \n1.Name \n2.Age \n3.Salary \n")
    ch=int(input("Enter your choice from menue ::"))
    if ch==1:
        a=sorted(name)
        print(a)
    elif ch==2:
        print(sorted(age))
    elif ch==3:
        print(sorted(salary))
sorte()