#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1181                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dgsw18 <boj.kr/u/dgsw18>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1181                           #+#        #+#      #+#     #
#    Solved: 2025/04/03 10:16:52 by dgsw18        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input_count = int(input())

words = set()
for i in range(input_count):
    words.add(input())

same_word_length = {}

for i in words:
    try:
        if (not same_word_length[len(i)]):
            same_word_length[len(i)] = [i]
        else:
            same_word_length[len(i)].append(i)
    except KeyError:
        same_word_length[len(i)] = [i]

for i in range(1,max(same_word_length)+1):
    try:
        soreted_by_dict = sorted(list(same_word_length[i]))
        for i in soreted_by_dict:
            print(i)
    except KeyError:
        pass