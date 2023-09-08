def calculate_clock_angle(hour, minute):
    # 将小时转换为在12小时制下的位置
    hour = hour % 12

    # 计算时针和分针的夹角
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6

    # 计算夹角差值
    angle_diff = abs(hour_angle - minute_angle)

    # 如果夹角大于180度，则取360减去夹角
    if angle_diff > 180:
        angle_diff = 360 - angle_diff

    return angle_diff

# 输入钟表的小时和分钟
hour = int(input("请输入小时："))
minute = int(input("请输入分钟："))

angle = calculate_clock_angle(hour, minute)
print("时针和分针的夹角：", angle, "度")
