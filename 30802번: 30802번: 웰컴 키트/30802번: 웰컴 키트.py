#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30802                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dgsw18 <boj.kr/u/dgsw18>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30802                          #+#        #+#      #+#     #
#    Solved: 2025/04/03 10:58:29 by dgsw18        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
minimum_buy = int(input())
proposer_person_by_size = list(map(int, input().split()))
tshirt, pen = map(int, input().split())
shirts_bundle = 0
for i in proposer_person_by_size:
    if (i == 0):
        continue
    elif i <= tshirt:
        shirts_bundle += 1
    elif i % tshirt == 0:
        shirts_bundle += (i // tshirt)
    else:
        shirts_bundle += (i // tshirt) + 1

print(shirts_bundle)
print(minimum_buy//pen, minimum_buy%pen)