
def bestValleys(valleys, north):
    
    result = []
    dist_seguridad = 10

    for i in range(len(valleys)):
        dif = valleys[i][1][0] - valleys[i][0][0]
        if north > valleys[i][1][0] or north < valleys[i][0][0]:
            continue
        elif dif <= dist_seguridad:
            continue
        else:
            result.append((dif, i))
    result.sort(key = lambda x: x[0])
    return valleys[result[0][1]]
