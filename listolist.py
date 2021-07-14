randomList = ["first","second", "last"];
print(randomList);
print(randomList[1]);
randomListTwo= ["third","fourth","beginning"]

#append whole list as one lsist element
mutatedListOne = randomList;
mutatedListOne.append(randomListTwo)
print(mutatedListOne);

#append whole list 
mutatedListTwo = randomList;
mutatedListTwo.extend(randomListTwo);
print(mutatedListTwo);
