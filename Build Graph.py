def is_valid_graph(n):
    found=False
    for k in range(2,n):
        comp1=k
        comp2=n-k
        if comp1<2 or comp2<2:
            continue
        max_edges_comp1=comp1*(comp1-1)//2
        max_edges_comp2=comp2*(comp2-1)//2
        min_edges_comp1=comp1-1
        min_edges_comp2=comp2-1
        for e1 in range(min_edges_comp1,max_edges_comp1+1):
            for e2 in range(min_edges_comp2,max_edges_comp2):
                if e1+e2==n:
                    Found = True
                    print("Yes")
                    print("Component 1: ", comp1 , "vetices,",e1,"edges")
                    print("Component 2: ",comp2 ,"vertices,",e2,"edges")
print("No")