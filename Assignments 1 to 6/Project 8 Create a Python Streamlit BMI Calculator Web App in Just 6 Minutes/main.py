import streamlit as st

st.title('BMI Calculator')

st.write("This app calculates your Body Mass Index (BMI).")

# User input For Weight and Height
weight = st.number_input("Enter your weight (in kilograms)", min_value=1.0, value=70.0, step=0.1)
height = st.number_input("Enter your height (in inches)", min_value=1.0, value=68.0)

height = height * 0.0254

# BMI Calculate Function
def calculate_bmi(weight, height):
  return weight / (height **2)

if st.button("Calculate BMI"):
  if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
      st.write("Category: Underweight")
    elif bmi < 25:
      st.write("Category: Normal Weight")
    elif bmi < 30:
      st.write("Category: Overweight")
    else:
      st.write("Category: Obese")
else:
  st.write("Please enter valid values for weight and height.")

