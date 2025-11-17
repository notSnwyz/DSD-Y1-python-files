notifications = [34, 28, 55, 40, 60, 22, 18]
notifications2 = [22, 45, 30, 84, 20, 11, 38]

print(f"Day 1: {notifications[0]}\nDay 2: {notifications[1]}\nDay 3: {notifications[2]}\nDay 4: {notifications[3]}\nDay 5: {notifications[4]}\nDay 6: {notifications[5]}\nDay 7: {notifications[6]}")

print(max(notifications))
print(min(notifications))
print(sum(notifications))
print(sum(notifications)//len(notifications))

notifications.append(33)
print(notifications)

if notifications > notifications2:
    print("User 1 has more notifications than user 2")
else:
    print("User 2 has more notifications than user 1")