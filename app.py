import streamlit as st

st.title('Power Calculator  ⚡     ')
st.write('This app calculates the power of a number based on user input.')

# Get user input for base and exponent
base = st.number_input('Enter the base number:', value=1,step=1)

square =base ** 2
cube = base ** 3
power_4 = base ** 4
power_5 = base ** 5


# Display the results
st.write(f'The square of {base} is: {square}')
st.write(f'The cube of {base} is: {cube}')          
st.write(f'The 4th power of {base} is: {power_4}')
st.write(f'The 5th power of {base} is: {power_5}')