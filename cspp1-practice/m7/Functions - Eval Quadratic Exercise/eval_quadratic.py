"""# Exercise: eval quadratic"""
def eval_quadratic(a_in, b_in, c_in, x_in):
    """ quadratic function"""
    return a_in*(x_in**2) + b_in*x_in +c_in
def main():
    """ main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x_a in range(len(data)):
        temp = str(data[x_a]).split('.')
        if temp[1] == '0':
            data[x_a] = int(float(str(data[x_a])))
        else:
            data[x_a] = data[x_a]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()
