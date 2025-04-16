import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter")

units_data = {
    "Length": {
        "units": ["Meter", "Kilometer", "Inch"],
        "values": {
            "Meter": 1,
            "Kilometer": 1000,
            "Inch": 0.0254
        }
    },
    "Mass": {
        "units": ["Kilogram", "Gram"],
        "values": {
            "Kilogram": 1,
            "Gram": 0.001
        }
    },
    "Speed": {
        "units": ["Meters per second", "Kilometers per hour", "Miles per hour"],
        "values": {
            "Meters per second": 1,
            "Kilometers per hour": 0.277778,
            "Miles per hour": 0.44704
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    }
}

# UI
category = st.selectbox("Choose category", ["Length", "Mass", "Speed", "Temperature"])

input_value = st.number_input("Enter value to convert")

if category != "Temperature":
    from_unit = st.selectbox("From", units_data[category]["units"])
    to_unit = st.selectbox("To", units_data[category]["units"])

    if st.button("Convert"):
        from_factor = units_data[category]["values"][from_unit]
        to_factor = units_data[category]["values"][to_unit]

        result = input_value * from_factor / to_factor
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")

else:
    from_temp = st.selectbox("From", units_data["Temperature"]["units"])
    to_temp = st.selectbox("To", units_data["Temperature"]["units"])

    if st.button("Convert"):
        def convert_temp(value, from_unit, to_unit):
            if from_unit == to_unit:
                return value
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    return value * 9 / 5 + 32
                elif to_unit == "Kelvin":
                    return value + 273.15
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    return (value - 32) * 5 / 9
                elif to_unit == "Kelvin":
                    return (value - 32) * 5 / 9 + 273.15
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    return value - 273.15
                elif to_unit == "Fahrenheit":
                    return (value - 273.15) * 9 / 5 + 32

        result = convert_temp(input_value, from_temp, to_temp)
        st.success(f"{input_value} {from_temp} = {result:.2f} {to_temp}")
