import sys
def  bestAverageGrade(scores):
    dict = {}
    maxi = -999999
    # for i in range(len(scores)):
    #     templist = scores[i]
    #     if templist[0] in scoresdict:
    #         tlist = scoresdict[templist[0]]
    #         tlist.append(int(templist[1]))
    #         scoresdict[templist[0]] = tlist
    #     else:
    #         scoresdict[templist[0]] = [int(templist[1])]
    for i in range(0, len(scores)):
        if scores[i][0] not in dict:
            dict[scores[i][0]] = [int(scores[i][1])]
        else:
            dict[scores[i][0]] +=  [int(scores[i][1])]
    print(dict)

    for key in scoresdict:

        maxi = max(sum(scoresdict[key]) / len(scoresdict[key]), maxi)

            # # print(key)
        # list = scoresdict[key]
        # sum = 0
        # for i in range(0, len(list)):
        #     sum += list[i]
        # avg = sum / len(list)
        # # print(avg)
        # maxi = max(avg, maxi)
    print("Maxi =" ,maxi)
    return maxi




scores = [["Bobby","87"],["Charles","100"],["Eric", "64"],["Charles","22"]]
bestAverageGrade(scores)




























#
# def  dotProduct(x, y):
#     sum= 0
#     if len(x)!= len(y) or len(x)==0 or len(y) == 0:
#         return 0
#     else:
#         for i in range(len(x)):
#             sum+= x[i]*y[i]
#     return sum