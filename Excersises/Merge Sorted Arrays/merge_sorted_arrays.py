def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        m = [1,2,0,0,0,0] n = [2,5,6,4]
                     i           j   
                     i = 3 j = 2 3 >= 2+2
                     i = 4 j = 3
        m = [1,2,5,6,7,0] n = [2,6,7]
                       i             j=n
             instead of putting the 4 at m
             
        """
        if m ==0: 
            for i in range(n):
                nums1[i] = nums2[i]
        if n != 0:
                i,j,shifts = 0,0,0
                
                if len(nums1) == n: 
                    for i in range(n):     
                        nums1[i] == nums2[i]
                else:
                    
                    while(i<m+n):
                        if nums1[i+shifts] == 0:
                            while(j<=n-1):
                                nums1[i] = nums2[j]
                                i+=1
                                j+=1
                            break   
                        # print("in while")     
                        print(i,j,nums1)
                        # print(nums1[i], nums2[j])
                        print( nums2[j])
                        print(nums1[i])
                        if nums1[i]<=nums2[j]:
                            # if i+1>=m+j:
                            #     nums1[m+j] = nums2[j]
                            #     j +=1
                            i +=1
                        else:
                            r=m-1
                            # nums1[i], nums2[j] = nums2[j], nums1[i]
                            while r>= i:
                                # print("moving", nums1[r])
                                nums1[r+1] = nums1[r]
                                r -=1
                            nums1[i] = nums2[j]
                            shifts +=1
                            # if nums1[m+j] ==nums1[i+j]==0:
                                
                            # else: 
                            #     print("entered else")
                            #     print(i)
                            #     for r in range(i + (m-i-1),m):
                            #         nums1[r+1] = nums1[r]
                            #     nums1[i+j]=nums1[i]
                            #     nums1[i] = nums2[j]
                            j +=1
                            i+=1
                        
                    #Now either i  has reached their respective ends
                # i = i-1
                # while j <= n-1:
                #     # print(i)
                #     # print(j)
                #     # print(nums1[i])
                #     # print(nums2[j])
                #     nums1[i] = nums2[j]
                #     i +=1
                #     j+=1
        nums1[-1] =nums2[-1]
        print(nums1)
def merge2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    if m ==0: 
        for i in range(n):
            nums1[i] = nums2[i]
    if n != 0:
            i,j,k = 0,0,0
            l1 = [-1 for l in range(m+n)]
            
            if len(nums1) == n: 
                for i in range(n):     
                    nums1[i] == nums2[i]
            else:
                while (i<=m):
                    if nums1[i]<=nums2[j]:
                        l1[k] = nums1[i]
                    else:
                        l1[k] = nums2[j]
                    i +=1
                    j +=1
                    k +=1
                while i<=m-1:
                    l1[k] = nums1[i]
                    i+=1
                    k+=1
                while j<=n-1:
                    l1[k] = nums2[j]
                    j+=1
                    k+=1
            for p in range(m+n):
                nums1[p] = l1[p] 
            print(nums1)
                    
                
                    

merge2([1,2,3,0,0,0], 3,[2,5,6],3)
#              i          j
        
        
        