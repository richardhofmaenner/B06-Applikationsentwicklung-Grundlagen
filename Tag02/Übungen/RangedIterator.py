def next_item(xs, item):
    # check if item exists in given sequence
    if item in xs:
        print(xs)
        length = len(xs)
        index = xs.index(item)
        if index < 0 or index > length-2:
            return None
        index += 1
        return xs[index]
    else:
        return None
    
if __name__ == "__main__":
  xs = iter(range(1, 30000))
  for x in xs:
    print(x)
  #print(next_item(xs, 12))