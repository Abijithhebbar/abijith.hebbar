

def oddTuples(aTup):
    tup=()
    for j in range(0, len(aTup), 2):
        tup = tup +(aTup[j],)
    return tup
def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += ((data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()