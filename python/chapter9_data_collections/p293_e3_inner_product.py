# The inner product of two vectors is an important measure of similarity and is an essential core operation in modern AI systsmes based on artificail neural networks.
# Write and test a function innerProd(x, y) that computs the inener product of two (same length) lists. The inner product of x and y is computer as: (Book gives sigma notation form)
# innerProd([1, 2, 3], [4, 5, 6]) should product 32

def innerProd(x, y):
    if len(x) != len(y):
        raise Exception("x and y have different sizes")
    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]
    return result

def main():
    x = [1, 2, 3]
    y = [4, 5, 6]
    result = innerProd(x, y)
    print(result)

if __name__ == "__main__":
    main()