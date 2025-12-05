import os
os.system('cls' if os.name == 'nt' else 'clear')



j = True




while j == True:
    choose = int(input("Type '1' for y = mx + c or Type '2' for vertical line:")) 
    if choose == 1:

        print("Y = MX + C")
        m = int(input("for m:"))
        c = int(input("for c:"))
        dot = "  "
        gs = 10
        
        if m > 0:
            sumpol = " /"
        
        elif m < 0:
            sumpol = " \\"
        else:
            sumpol = " -"
            
        for y in range(gs, -gs, -1):
            line = ""
            for x in range(-gs, gs + 1):
                if y == m*x + c :
                    line += sumpol
                elif y == 0 and x == 0:
                    line += " +"
                elif y == 0:
                    line += " -"
                elif x == 0:
                    line += " |"
                else:
                    line += dot

            print(line)
        print()

    if choose == 2:
        x0 = int(input("what is the x vaule\n"))
        sumpol = " |"
        dot = "  "
        gs = 10        
        for y in range(gs, -gs, - 1):
            line = ""
            for x in range(-gs, gs + 1):
                if x == x0:
                    line += sumpol
                elif y == 0 and x == 0:
                    line += " +"
                elif y == 0:
                    line += " -"
                elif x == 0:
                    line += " |"
                else:
                    line += dot

            print(line)
        print()
