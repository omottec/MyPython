import os
import datetime
import time


def print_fd():
    # get pid
    pid_lines = os.popen("adb shell ps | grep com.ss.android.lark.debug").readlines()
    pid_line = ""
    for line in pid_lines:
        if ":" not in line:
            pid_line = line
    print(pid_line.replace("\n", ""))
    pid = pid_line.split()[1]

    # get fd list and time
    fd_list = os.popen("adb shell su -c 'ls -al /proc/" + pid + "/fd'").readlines()[3:]
    fd_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # calculate fd
    socket_fd = 0
    for fd_line in fd_list:
        if "socket" in fd_line:
            socket_fd = socket_fd + 1
    total_fd = len(fd_list)
    print(fd_time + " total_fd:" + str(total_fd) + ", socket_fd:" + str(socket_fd))
    print


while True:
    print_fd()
    time.sleep(60)
