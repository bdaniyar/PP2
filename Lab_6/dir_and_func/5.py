def func(x,y):
  try:
    with open(x, 'a') as file:
      for i in y:
        file.write(str(i) + "\n")
      print("List written")

  except:
    print("error")


list1 = [1,2,"fdksd", "Apple", 3.12]
filename = input("Write a filename with .txt: ")

func(filename,list1)