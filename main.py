########################################   KENAN JAFAROV    ########################################

######################################## E X E R C I S E  1 ########################################
# allWords = []
# wordCounter = {}
# wordLength = int()
#
# while True:
#     try:
#         inpNumber = int(input("Number: "))
#         break
#     except:
#         print("Please enter number.")
#
# for num in range(inpNumber):
#     while True:
#         inpWord = input(f"Word {num + 1}: ")
#         if not inpWord.islower():
#             print("Words have to be composed in lowercase and minimum length of the word have to be 1.")
#         else:
#             wordLength += len(inpWord)
#             break
#
#     allWords.append(inpWord)
#     if inpWord in wordCounter:
#         wordCounter[inpWord] += 1
#     else:
#         wordCounter[inpWord] = 1
#
# if 1 <= wordLength <= pow(10,5):
#     print(f"Number of distinct words from the input: {len(wordCounter)}")
#
#     wrdNms = ' '.join([str(wordCounter[word]) for word in wordCounter])
#     print(f"Number of occurrences for each distinct word according to their appearance in the input: {wrdNms}")
# else:
#     print("The sum of the lengths of all the words can not exceed 10^5.")


######################################## E X E R C I S E  2 ########################################

# def bigger_Is_greater(word):
#     word = list(word[::-1])
#     for i in range(1,len(word)):
#         if word[i-1] > word[i]:
#             for j in range(i):
#                 if word[j] > word[i]:
#                     word[j],word[i] = word[i],word[j]
#                     word = sorted(word[:i])[::-1] + word[i:]
#                     print(f"The next largest word is: {''.join(word[::-1])}")
#                     break
#             break
#     else:
#         print("No answer.")
#
# while True:
#     try:
#         numOfTestCases = int(input("The number of test cases: "))
#         break
#     except:
#         print("Please enter number.")
#
# if 1 <= numOfTestCases <= pow(10,5):
#     for num in range(numOfTestCases):
#         while True:
#             word = input(f"Word {num + 1}: ")
#             if word.islower() and 1 <= len(word) <= 100:
#                 bigger_Is_greater(word)
#             else:
#                 print("Words have to be composed in lowercase and the length of the word have to be more than 1 and less than 100.")
# else:
#     print("The number of test cases have to be more than 1 and less than 10^5.")


