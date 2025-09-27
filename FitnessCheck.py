speedper100 = float(input("Enter your running time of 100m"))
jumpheight  = float(input("Enter your jumping height"))


fitnessLeveL = speedper100 * 6 + jumpheight * 10

if fitnessLeveL < 50:
    print("You are not fit at all")
else:
    print("You are very fit")1