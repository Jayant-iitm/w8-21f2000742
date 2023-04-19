import streamlit as st

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    st.title("Find the largest among three given numbers")
    st.write("Enter three numbers below:")
    
    # Get user input
    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")
    
    # Find the largest number
    if st.button("Find the largest number"):
        largest_num = find_largest(a, b, c)
        st.write("The largest number is:", largest_num)

if __name__ == '__main__':
    main()
