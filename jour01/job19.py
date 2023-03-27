def draw_rectangle(width, height):
        print("|" + "-"*(width) + "|")

        for i in range(height):
            if i >= 2 :
                print("|" + " "*(width+1) + "|")

        if height >= 2 :
         print("|" + "-"*(width) + "|")


draw_rectangle(2,2)
