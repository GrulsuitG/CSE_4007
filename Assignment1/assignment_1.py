import bfs
import hc
import csp


def main():
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    for line in lines:
        s = line.split()
        if 'bfs' in s[1]:
            ans = bfs.bfs(int(s[0]))
            
            with open(s[0]+"_bfs_output.txt", 'w') as f:
                if ans == None :
                    f.write("no solution")
                else:
                    if len(ans) ==1 :
                        f.write("1")
                    for i in range(1, int(s[0])+1):
                        num = ans[i]
                        f.write(str(num) + " ")
            
        elif 'hc' in s[1]:
            ans = hc.hc(int(s[0]))
            
            with open(s[0]+"_hc_output.txt", 'w') as f:
                if ans == None :
                    f.write("no solution")
                else:
                    if len(ans) == 1 :
                        f.write("1")
                    else : 
                        for i in range(0, int(s[0])):
                            num = ans[i].index(1) + 1
                            f.write(str(num) + " ")

        elif 'csp' in s[1]:
            ans = csp.csp(int(s[0]))
            
            with open(s[0]+"_csp_output.txt", 'w') as f:
                if ans == None :
                    f.write("no solution")
                else:
                    if len(ans) ==1 :
                        f.write("1")
                    for i in range(1, int(s[0])+1):
                        num = ans[i]
                        f.write(str(num) + " ")
    
             

if __name__ == "__main__":
    main()


