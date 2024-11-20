def check_speed(speed):
    if speed < 70:
        return "good"
    else:
        negative_points = (speed - 70) // 5
        
        if negative_points > 12:
            print("گواهینامه شما باطل شد")
        
        return negative_points

speed1 = 80
print(check_speed(speed1))  

speed2 = 120
print(check_speed(speed2))  

speed3 = 65
print(check_speed(speed3))  

                