def test(x):
  if x < 0:
    raise Exception("Sorry, no numbers below zero!")

#test(-10)

x = "hello"
assert x == "goodby", "x should be 'hello'"