

for (( c=1; c<=200; c++ )); do 
  gdb ./ys13server && kill -9 `pgrep -f "ys13server"`
done