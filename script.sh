curl http://ba.tune-it.ru/student/os/var/414525 >1
chmod 777 1
./1 &
export appPid=$(pidof 1)
mkdir "io"
iostat -m -d -p 1 100 >iostat.txt
python3 io.py
top -b -H -n 20 -p $appPid >threads_stat.txt
python3 threads.py
