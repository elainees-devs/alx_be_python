# This program gives clothing recommendations based on the current weather input by the user.

current_weather = input("What's the weather like today? (sunny/rainy/cold): ")


if current_weather == "sunny":
    print("Wear a t-shirt and sunglasses.\n")
elif current_weather == "rainy":
    print("Don't forget to carry an umbrella and a raincoat.\n")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.\n")
else:
    print("Sorry, I don't have recommendations for this weather.\n")
