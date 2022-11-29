from multiprocessing import Pool


def sort(array):
    if len(array)<=1:
        return array
    else:
        left, right = [], []
        pivot = array[0]
        for element in array:
            if element<=pivot:
                left.append(element)
            else:
                right.append(element)
        return [left, right]



def paralel():
    ans = [7, 5, 8, 9, 7, 5, 4, 8, 6, 3, 4, 5, 8, 9, 5, 4, 5, 2, 0]
    ans = sort(ans)
    print(ans)
    #while len(ans[0])>2 or len(ans[1])>2:
    #with Pool() as p:

    #print(ans)

if __name__ == "__main__":
    with Pool() as pool:

        ans = [[4, 5, 8, 9, 7, 5, 4, 8, 6, 3, 4, 5, 8, 9, 5, 4, 5, 2, 0]]
        print(len(ans[0]))
        answer = pool.map(sort, ans)[0]
        print(answer)
        answer = pool.map(sort, answer)[0]
        print(answer)
        answer = pool.map(sort, answer)[0]
        print(answer)
        answer = pool.map(sort, answer)[0]
        print(answer)
    print("Program finished!")
    print(answer)