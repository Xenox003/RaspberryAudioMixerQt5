git pull origin

for file in ./.compileui/*.ui; do
    pureFileName=${file##*/}

    echo $PWD
    pyuic5 "$file" -o "app/modules/ui/${pureFileName//.ui/}_ui.py"
done