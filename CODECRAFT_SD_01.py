import streamlit as st

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    st.title("Temperature Converter: Celsius, Fahrenheit, Kelvin")
    value = st.number_input("Enter the temperature value:", value=0.0, format="%f")
    unit = st.selectbox("Select the unit:", ("Celsius (C)", "Fahrenheit (F)", "Kelvin (K)"))

    if unit == "Celsius (C)":
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        st.write(f"{value}°C = {f:.2f}°F, {k:.2f}K")
    elif unit == "Fahrenheit (F)":
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        st.write(f"{value}°F = {c:.2f}°C, {k:.2f}K")
    elif unit == "Kelvin (K)":
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        st.write(f"{value}K = {c:.2f}°C, {f:.2f}°F")

if __name__ == "__main__":
    main()
