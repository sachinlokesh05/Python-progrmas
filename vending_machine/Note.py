class Note:
    def getChange(self,amount):
        notes=[2000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
        count_notes=[0,0, 0, 0, 0, 0, 0, 0, 0, 0]
        i=0
        while i<len(notes):
            if amount<0:
                return
            elif (amount >= notes[i]):
                    count_notes[i] = amount // notes[i]
                    amount = amount % notes[i]
            i+=1

        j=0
        while j<len(count_notes):
            if count_notes[j]!=0:
                print(notes[j],":",count_notes[j])
            j+=1
