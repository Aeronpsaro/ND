def getBestValley(valleys, north):
    result = []

    for i in range(len(valleys)):
        dif = valleys[i][1] - valleys[i][0] 
        if north > valleys[i][1] or north < valleys[i][0]:
            continue
        else:
            result.append((dif, i))
            
    result.sort(key = lambda x: x[0])
    return valleys[result[0][1]]
    
    
